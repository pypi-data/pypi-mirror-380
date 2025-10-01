import numpy as np
import logging


def calculate_threshold(data, pick=1):

    if np.min(data) == 0:
        offset = 1
        logging.debug('Calculating threshold, min of data is 0, setting offset to 1.')
    else:
        offset = 0

    freq, counts, bins = calculate_histogram(data)
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
    logging.debug(f'Calculating threshold, index is {idx}')

    rest = freq[idx:]
    low = freq[idx]
    high = np.max(rest)

    idx_offset = max(0, np.argmax(rest >= (low + (high-low)*0.10))-1)
    idx = idx + idx_offset

    logging.debug(f'Calculating threshold, index was pushed to {idx}')


    pixels = np.sum(counts[idx:]) / np.sum(counts)
    if  pixels < 0.001:
        logging.debug('Calculating threshold, threshold is lower than 0.001 percentile, invalidating threshold')
        return np.max(data)+1
    if  0.999 < pixels:
        logging.debug('Calculating threshold, threshold is higher than 0.999 percentile, invalidating threshold')
        return np.max(data)+1
    if idx == 0:
        logging.debug('Calculating threshold, threshold is 0, invalidating threshold')
        return np.max(data)+1
    threshold = np.exp(bins[idx+1])-offset
    logging.debug('Calculating threshold, final threshold is %s', threshold)
    return threshold


def calculate_histogram(data):
    N = 80
    zero_bins = 80
    while zero_bins > 4:
        freq, counts, bins = _calculate_histogram(data, N)
        zero_bins = np.sum(counts == 0)
        N = int(N/2)
    return freq, counts, bins


def _calculate_histogram(data, N):
    if data.dtype == np.uint8 or data.dtype == np.uint16:
        data = data.astype(np.int32)
    if np.min(data) == 0:
        offset = 1
    else:
        offset = 0
    try:
        counts, bins = np.histogram(np.log(data+offset), N)
    except Exception as e:
        d1 = data+offset
        d2 = np.log(d1)
        logging.error({'data+offset': d1, 'log(data+offset)': d2, 'offset': offset, 'data min': np.min(data), 'data max': np.max(data), 'data+offset min': np.min(d1), 'data+offset max': np.max(d1), 'log(data+offset min)': np.min(d2), 'log(data+offset max)': np.max(d2)})
        raise e

    for i in range(len(counts)):
        if counts[i] <= 10:
            counts[i] = 1
        else:
            break

    for i in range(1, len(counts)):
        if counts[-i] <= 10:
            counts[-i] = 1
        else:
            break
    freq = np.log(1+counts)
    return freq, counts, bins
