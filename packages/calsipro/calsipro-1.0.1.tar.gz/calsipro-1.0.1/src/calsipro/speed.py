import numpy as np
import polars as pl
import scipy.ndimage


def time_analysis(t, intensity_cutoff=0.5):
    t = t - np.min(t, axis=0).reshape((1, t.shape[1], t.shape[2]))
    t = t / np.max(t, axis=0).reshape((1, t.shape[1], t.shape[2]))

    time = np.argmax(t >= intensity_cutoff, axis=0)
    return time


def calculate_speed(time, mask):
    """calculates speed in pixels/frame"""
    m, mm = np.min(time[mask]), np.max(time[mask])

    ori_pos = np.array(find_ori_cluster(time, mask, as_index=True)).reshape((2, 1))

    timepoints = list(range(m+1, mm+1))
    locations = [np.stack([x, y]) for x, y in find_times(time, mask, timepoints, as_index=True)]

    dts = [0]
    speeds = [-1]
    ns = [np.sum(time == m)]
    total_speed = 0
    total_ns = 0
    for t, l in zip(timepoints, locations):
        dists = np.sqrt(np.sum((l - ori_pos)**2, axis=0))
        dt = t-m
        dl = np.sum(dists)
        n = dists.shape[0]
        if n == 0:
            continue
        total_speed += dl/dt
        total_ns += n
        speeds.append(dl/(n*dt))
        ns.append(n)
        dts.append(dt)
    if total_ns == 0:
        total_ns = 1

    r = (pl.DataFrame({'time': np.array(dts, dtype=np.int64),
                       'speed': np.array(speeds, dtype=np.float64),
                       'n': np.array(ns, dtype=np.int64)}),
         total_speed/total_ns)
    return r


def push_low_pixels(time, mask, threshold=30):
    m = np.min(time[mask])
    mm = np.max(time[mask])

    time[~mask] = mm+1

    for i in range(m, mm+1):
        if np.sum(time == i) < threshold:
            time[time == i] = i+1
            m = m+1
        else:
            break

    for i in range(m, mm+1)[::-1]:
        if np.sum(time == i) < threshold:
            time[time == i] = i-1
            mm = mm-1
        else:
            break
    time[~mask] = np.max(time)
    return time


def find_times(data, mask, times, as_index=True):
    data = data.copy()
    data[~mask] = np.min(data)-1
    if as_index:
        return [(data == time).nonzero() for time in times]
    else:
        return [(data == time) for time in times]


def find_ori_cluster(data, mask, as_index=False):
    cluster_mask = np.zeros(data.shape, dtype=np.bool_)
    ori_time = np.min(data[mask])
    cluster_mask[data == ori_time] = 1
    cluster_mask[~mask] = 0
    label, count = scipy.ndimage.label(cluster_mask, scipy.ndimage.generate_binary_structure(2, 2))

    if count > 1:
        sizes = []
        for k in range(1, count+1):
            size = np.sum(label[mask] == k)
            sizes.append(size)
        biggest = np.argmax(sizes)+1
        cluster_mask = (label == biggest)

    if as_index:
        xs, ys = cluster_mask.nonzero()
        return np.array((np.average(xs), np.average(ys))).reshape((2, 1))
    else:
        return cluster_mask
