import numpy as np


def moving_average(a, n=3):
    if n == 0:
        return a
    ret = np.cumsum(a, axis=2, dtype=float)
    ret[:, :, n:] = ret[:, :, n:] - ret[:, :, :-n]
    return ret[:, :, n - 1:] / n


def max_projection(data):
    data = data[1:, :, :]
    data = np.max(data, axis=0)
    return data


def normalize(data):
    m, mm = np.min(data), np.max(data)
    data = (data - m) / (mm - m)
    return data


def normalize_to_dtype(data, dtype=np.uint8):
    m, mm = np.min(data), np.max(data)
    data = (data - m) / (mm - m)
    data = np.iinfo(np.uint8).max * data
    data = data.astype(dtype)
    return data


def calculate_mask(t, th=0.25, raw=False, labelling=True, larger=True):
    """Find the biggest connected component with t > th"""
    if not raw:
        t = np.max(t, axis=0)
        t = normalize(t)
    if larger:
        mask = t >= th
    else:
        mask = t <= th
    if not labelling:
        return mask
    import scipy.ndimage
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


def calculate_average_signal(data, mask=None):
    if mask is not None:
        signal = np.mean(data[:, mask], axis=(1))
    else:
        signal = np.mean(data, axis=(1,2))
    return signal
