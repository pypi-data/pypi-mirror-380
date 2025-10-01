import calsipro.separate
import calsipro.util
import numpy as np

def calculate_mask_variance(data):
    d = np.var(data, axis=0)
    threshold = calsipro.separate.calculate_threshold(d)
    mask = calsipro.util.calculate_mask(d, th=threshold, raw=True)
    return mask
