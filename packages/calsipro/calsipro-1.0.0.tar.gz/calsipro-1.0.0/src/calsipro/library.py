import numpy as np

def mask_variance(data, background_correction=True):
    import calsipro.mask
    import calsipro.util
    assert len(data.shape) == 3
    if background_correction:
        import calsipro.background
        signal = calsipro.util.calculate_average_signal(data)
        background = calsipro.background.estimate_baseline(signal)
        data = calsipro.background.remove_background(data, background)
    mask = calsipro.mask.calculate_mask_variance(data)
    assert len(mask.shape) == 2
    return mask

def peaks(data, mask):
    import calsipro.util
    import calsipro.background
    import calsipro.peak_calling.statistics
    assert len(data.shape) == 3
    assert len(mask.shape) == 2
    signal = calsipro.util.calculate_average_signal(data, mask)
    background = calsipro.background.estimate_baseline(signal)
    signal = calsipro.background.remove_background(signal, background)

    peaks = calsipro.peak_calling.statistics.call_peaks(signal)
    return peaks

def estimate_size(data):
    import numpy as snp
    import sys
    try:
        from skimage.measure import regionprops
    except ModuleNotFoundError:
        print("estimate size requires the scikit-image package.")
        sys.exit(-1)
    assert len(data.shape) == 2
    assert data.dtype == np.bool
    data = data.astype(np.uint8)
    regions = regionprops(data)

    assert len(regions) == 1
    organoid = regions[0]
    return organoid.axis_major_length
