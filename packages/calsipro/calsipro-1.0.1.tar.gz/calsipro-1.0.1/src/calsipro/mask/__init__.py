from .variance import calculate_mask_variance
from .reach import calculate_mask_reach
from .intensity import calculate_mask_intensity
import numpy as np


def shrink_mask(mask, n):
    for i in range(n):
        d1 = np.diff(mask, axis=0)
        d2 = np.diff(mask, axis=1)
        mask[:-1, :][d1 != 0] = 0
        mask[1:, :][d1 != 0] = 0
        mask[:, 1:][d2 != 0] = 0
        mask[:, :-1][d2 != 0] = 0
    return mask
