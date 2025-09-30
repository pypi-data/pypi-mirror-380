import calsipro.separate
import calsipro.util

def calculate_mask_intensity(data):
    assert len(data.shape) == 2
    threshold = calsipro.separate.calculate_threshold(data)
    mask = calsipro.util.calculate_mask(data, th=threshold, raw=True)
    return mask
