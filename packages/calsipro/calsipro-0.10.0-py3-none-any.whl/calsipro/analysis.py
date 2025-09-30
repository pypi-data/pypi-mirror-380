import numpy as np
import polars as pl
import scipy.ndimage
import numba

def moving_average(a, n=3):
    if n == 0:
        return a
    ret = np.cumsum(a, axis=2, dtype=float)
    ret[:, :, n:] = ret[:, :, n:] - ret[:, :, :-n]
    return ret[:, :, n - 1:] / n


def normalize(data):
    m, mm = np.min(data), np.max(data)
    data = (data - m) / (mm - m)
    return data


def _calculate_bf_threshold_and_mask(data, min_size=30, border_size=5):

    calculation_needed = True
    pick = 1
    while calculation_needed and pick < 80:
        threshold = calculate_threshold(data, pick=pick)
        mask = calculate_mask(data, th=threshold, raw=True, larger=False)
        mask_size = mask.sum()
        if mask_size == 0:
            calculation_needed = False
        elif mask_size < min_size:
            pick += 1
        else:
            calculation_needed = False

    return mask


def calculate_mask(t, th=0.25, raw=False, labelling=True, larger=True):
    if not raw:
        t = np.max(t, axis=0)
        t = normalize(t)
    if larger:
        mask = t >= th
    else:
        mask = t <= th
    if not labelling:
        return mask
    image = np.ones(mask.shape)
    image[~mask] = 0
    image[mask] = 1
    label, count = scipy.ndimage.label(image)
    if count == 1:
        return mask
    else:
        sizes = []
        for k in range(1, count+1):
            size = np.sum(label[mask] == k)
            sizes.append(size)
        if len(sizes) > 0:
            biggest = np.argmax(sizes)+1
        else:
            biggest = 1
        return label == biggest


def calculate_threshold(data, pick=1):
    if np.min(data) == 0:
        offset = 1
    else:
        offset = 0
    try:
        counts, bins = np.histogram(np.log(data+offset), 80)
    except Exception as e:
        d1 = data+offset
        d2 = np.log(d1)
        print('data+offset', d1)
        print('log(data+offset)', d2)
        print('offset', offset)
        print('data min', np.min(data))
        print('data max', np.max(data))
        print('data+offset min', np.min(d1))
        print('data+offset max', np.max(d1))
        print('log(data+offset min)', np.min(d2))
        print('log(data+offset max)', np.max(d2))
        raise e


    for i in range(len(counts)):
        if counts[i] <= 0:
            counts[i] = 1
        else:
            break

    for i in range(1, len(counts)):
        if counts[-i] <= 0:
            counts[-i] = 1
        else:
            break


    freq = np.log(1+counts)
    left_flood = freq.copy()
    right_flood = freq.copy()
    flood = freq.copy()

    for i in range(1, len(freq)):
        left_flood[i] = max(left_flood[i], left_flood[i-1])

    for i in list(range(0, len(freq)-1))[::-1]:
        right_flood[i] = max(right_flood[i], right_flood[i+1])

    for i in range(0, len(freq)):
        flood[i] = min(left_flood[i], right_flood[i])

    f = flood - freq
    if pick != 1:
        idxs = np.argsort(flood-freq)
        idx = idxs[-pick]
    else:
        idx = np.argmax(flood-freq)

    rest = freq[idx:]
    low = freq[idx]
    high = np.max(rest)

    idx_offset = max(0, np.argmax(rest >= (low + (high-low)*0.10))-1)
    idx = idx + idx_offset


    pixels = np.sum(counts[idx:]) / np.sum(counts)
    if  pixels < 0.001:
        return np.max(data)+1
    if  0.999 < pixels:
        return np.max(data)+1
    if idx == 0:
        return np.max(data)+1
    return np.exp(bins[idx+1])-offset


def _find_biggest(mask):
    label, count = scipy.ndimage.label(mask)
    if count == 1:
        return mask
    else:
        sizes = list(np.bincount(label[mask]))
        assert sizes[0] == 0
        sizes = sizes[1:]
        assert len(sizes) == count
        if len(sizes) > 0:
            biggest = np.argmax(sizes)+1
        else:
            biggest = 1
        return label == biggest


def time_analysis(t, intensity_cutoff=0.5):
    t = t - np.min(t, axis=0).reshape((1, t.shape[1], t.shape[2]))
    t = t / np.max(t, axis=0).reshape((1, t.shape[1], t.shape[2]))

    time = np.argmax(t >= intensity_cutoff, axis=0)
    return time


def push_low_pixels(time, mask):

    m = np.min(time[mask])
    mm = np.max(time[mask])

    time[~mask] = mm+1

    for i in range(m, mm+1):
        if np.sum(time == i) < 30:
            time[time == i] = i+1
            m = m+1
        else:
            break

    for i in range(m, mm+1)[::-1]:
        if np.sum(time == i) < 30:
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


def calculate_speed(time, mask):
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


def calculate_speed_better(time, mask):
    ori_pos = find_ori_cluster(time, mask, as_index=True)

    x_dist = np.repeat((np.arange(time.shape[0]) - ori_pos[0]).reshape((time.shape[0], 1)), time.shape[1], axis=1)
    y_dist = np.repeat((np.arange(time.shape[1]) - ori_pos[1]).reshape((1, time.shape[1])), time.shape[0], axis=0)

    dists = np.sqrt(x_dist**2 - y_dist**2)

    time = time - np.min(time)
    speed = dists / time
    speed[time == 0] = 0

    return speed


def tabularize_speed(time, speed, mask):
    m, mm = np.min(time), np.max(time)
    timepoints = list(range(m+1, mm+1))

    time[mask] = mm+1

    ns = [np.sum(time == timepoint) for timepoint in timepoints]
    speed = [np.average(speed[time == timepoint]) for timepoint in timepoints]

    r = (pl.DataFrame({'time': np.array(timepoints, dtype=np.int64),
                       'speed': np.array(speed, dtype=np.float64),
                       'n': np.array(ns, dtype=np.int64)}),
         np.average(speed[mask]))
    return r


def reachability(data, threshold=0.02):
    data = normalize(data)
    mask = np.zeros(shape=data.shape, dtype=np.bool_)
    scheduled = np.zeros(shape=data.shape, dtype=np.bool_)
    _reachability(data, scheduled, mask, threshold, 1, 1)
    return mask


@numba.njit(cache=True)
def _reachability(data, scheduled, mask,  threshold, dx, dy):
    next = []
    x_len, y_len = data.shape
    for y in range(y_len-1):
        x = 0
        mask[x, y] = True
        next.append((x, y))
        scheduled[x, y] = True

        x = x_len-1
        mask[x, y] = True
        next.append((x, y))
        scheduled[x, y] = True

    for x in range(x_len-1):
        y = 0
        mask[x, y] = True
        next.append((x, y))
        scheduled[x, y] = True

        y = y_len-1
        mask[x, y] = True
        next.append((x, y))
        scheduled[x, y] = True

    while (len(next) != 0):
        x, y = next.pop(0)
        b_v = data[x,y]

        nx, ny = x+dx, y
        if 0 <= nx < x_len:
            v = data[nx, ny]
            if abs(v-b_v) <= threshold:
                mask[nx, ny] = True
                if not scheduled[nx, ny]:
                    scheduled[nx, ny] = True
                    next.append((nx, ny))

        nx, ny = x-dx, y
        if 0 <= nx < x_len:
            v = data[nx, ny]
            if abs(v-b_v) <= threshold:
                mask[nx, ny] = True
                if not scheduled[nx, ny]:
                    scheduled[nx, ny] = True
                    next.append((nx, ny))

        nx, ny = x, y+dy
        if 0 <= ny < y_len:
            v = data[nx, ny]
            if abs(v-b_v) <= threshold:
                mask[nx, ny] = True
                if not scheduled[nx, ny]:
                    scheduled[nx, ny] = True
                    next.append((nx, ny))

        nx, ny = x, y-dy
        if 0 <= ny < y_len:
            v = data[nx, ny]
            if abs(v-b_v) <= threshold:
                mask[nx, ny] = True
                if not scheduled[nx, ny]:
                    scheduled[nx, ny] = True
                    next.append((nx, ny))


def calculate_bf_mask(data):
    data = data.copy()
    reachability_mask = reachability(data)
    data[reachability_mask] = np.mean(data[reachability_mask])
    mask = _calculate_bf_threshold_and_mask(data)
    return mask
