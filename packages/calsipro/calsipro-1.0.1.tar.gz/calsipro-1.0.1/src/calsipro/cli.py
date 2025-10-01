import click
import sys

@click.group()
def cli():
    pass

@cli.command()
@click.argument("path")
def scenes(path):
    import calsipro.io
    for scene in calsipro.io.show_scenes(path):
        print(scene)

@cli.command()
@click.argument("path")
@click.argument("scene")
@click.argument("out", type=click.Path(writable=True, readable=False))
@click.option("--frame", default=0)
def show(path, scene, out, frame):
    import calsipro.io
    data = calsipro.io.read_data(path, scene)[0, :, :]
    data = calsipro.util.normalize_to_dtype(data)
    calsipro.io.write_data(data, out)

@cli.command()
@click.argument("path")
@click.argument("scene")
@click.argument("out", type=click.Path(writable=True, readable=False))
@click.option("--width", default=100)
@click.option("--height", default=100)
@click.option("--background-correction/--no-background-correction", default=True)
def video(path, scene, out, width, height, background_correction):
    import calsipro.io
    if out.endswith(".webm"):
        encoder = "vp9"
    elif out.endswith(".mp4"):
        encoder = "h264"
    else:
        print("Only .webm or .mp4 output files are supported")
        sys.exit(-1)


    image = calsipro.io.read_image(path)
    data = calsipro.io.read_data(image, scene)

    metadata = image.standard_metadata
    duration = metadata.total_time_duration.total_seconds()
    frames = metadata.image_size_t

    if background_correction:
        import calsipro.background
        signal = calsipro.util.calculate_average_signal(data)
        background = calsipro.background.estimate_baseline(signal)
        data = calsipro.background.remove_background(data, background)

    data = calsipro.util.normalize_to_dtype(data)
    fps = frames / duration

    bytes = calsipro.io.encode_video(data, width=width, height=height, fps=fps, encoder=encoder)
    with open(out, mode="wb") as f:
        f.write(bytes)


@cli.command(name="max")
@click.argument("path")
@click.argument("scene")
@click.argument("out")
def max_(path, scene, out):
    import calsipro.io
    import calsipro.library
    data = calsipro.io.read_data(path, scene)
    data = calsipro.util.max_projection(data)
    data = calsipro.util.normalize_to_dtype(data)
    calsipro.io.write_data(data, out)


@cli.command()
@click.argument("path")
@click.argument("scene")
@click.argument("out")
@click.option("--algorithm", type=click.Choice(["variance", "reach", "intensity"]), default="variance")
@click.option("--shrink", default=5, help="Shrinks the mask from the outside by that many pixels")
@click.option("--background-correction/--no-background-correction", default=True)
def mask(path, scene, out, algorithm, background_correction, shrink):
    import calsipro.io
    import calsipro.library
    import calsipro.mask
    image = calsipro.io.read_image(path)
    data = calsipro.io.read_data(image, scene)
    if algorithm == "variance":
        mask = calsipro.library.mask_variance(data, background_correction=background_correction)
    elif algorithm == "reach":
        mask = calsipro.mask.calculate_mask_reach(data[0, :, :])
    elif algorithm == "intensity":
        mask = calsipro.mask.calculate_mask_intensity(data[0, :, :])
    if shrink > 0:
        mask = calsipro.mask.shrink_mask(mask, shrink)
    calsipro.io.write_data(mask, out)


@cli.command()
@click.argument("path")
@click.argument("scene")
@click.option("--mask")
def size(path, scene, mask):
    import calsipro.library
    import calsipro.io
    if mask is None:
        mask = calsipro.library.mask_variance(data)
    else:
        mask = calsipro.io.read_data(mask, None)[0, :, :]

    size_in_pixels = calsipro.library.estimate_size(mask)
    image = calsipro.io.read_image(path)
    size_in_μm = image.standard_metadata.pixel_size_x * size_in_pixels

    print(size_in_μm)


@cli.command()
@click.argument("path")
@click.argument("scene")
@click.argument("out")
@click.option("--mask")
def peaks(path, scene, out, mask):
    import calsipro.io
    import calsipro.library
    if not (out.endswith(".parquet") or out.endswith(".csv")):
        print("out-peaks must be a parquet or csv file")
        sys.exit(-1)
    image = calsipro.io.read_image(path)
    data = calsipro.io.read_data(image, scene)

    if mask is None:
        mask = calsipro.library.mask_variance(data)
    else:
        mask = calsipro.io.read_data(mask, None)[0, :, :]

    peaks = calsipro.library.peaks(data, mask)
    table = {"peak_start": [peak[0] for peak in peaks], "peak_end": [peak[1] for peak in peaks]}
    calsipro.io.write_table(table, out)


@cli.command()
@click.argument("path")
@click.argument("scene")
@click.argument("beat", type=int)
@click.argument("out")
@click.option("--peaks")
@click.option("--mask")
def beat(path, scene, out, beat, peaks, mask):
    import calsipro.io
    import calsipro.mask
    import calsipro.background
    import calsipro.library
    import calsipro.util
    import calsipro.speed
    import numpy as np
    from matplotlib import cm

    image = calsipro.io.read_image(path)
    data = calsipro.io.read_data(image, scene)

    if mask is None:
        mask = calsipro.library.mask_variance(data)
    else:
        mask = calsipro.io.read_data(mask, None)[0, :, :]

    if peaks is None:
        peaks = calsipro.library.peaks(data, mask)
    else:
        peaks = calsipro.io.read_table(peaks)
        peaks = [(start, end) for start, end in zip(peaks["peak_start"], peaks["peak_end"])]

    start, end = peaks[beat]
    data = data[start:end, :, :]

    signal = calsipro.util.calculate_average_signal(data, mask)
    background = calsipro.background.estimate_baseline(signal)
    beat_signal = calsipro.background.remove_background(data, background)

    time = calsipro.speed.time_analysis(beat_signal)

    # get a beat specific variance mask
    variance_mask = calsipro.mask.calculate_mask_variance(beat_signal)
    beat_mask = mask & variance_mask

    if beat_mask.any():
        time = calsipro.speed.push_low_pixels(time, beat_mask)

    time = calsipro.util.normalize(time)
    time = 1-time
    time = cm.inferno(time)
    time[:,:,3][~beat_mask] = 0

    time = calsipro.util.normalize_to_dtype(time)
    calsipro.io.write_data(time, out)

@cli.command()
@click.argument("path")
@click.argument("scene")
@click.argument("out")
@click.argument("flurophores", nargs=-1)
@click.option("--mask")
@click.option("--peaks")
def speed(path, scene, out, flurophores, mask, peaks):
    if len(flurophores) % 2 == 1:
        print("Uneven number of flurophore arguments, need name and path for each flurophore")
        sys.exist(-1)

    from itertools import pairwise
    import calsipro.io
    import calsipro.background
    import calsipro.mask
    import calsipro.library
    import calsipro.mask
    import calsipro.speed
    from decimal import Decimal

    image = calsipro.io.read_image(path)

    metadata = image.standard_metadata
    assert metadata.pixel_size_x == metadata.pixel_size_y
    resolution = metadata.pixel_size_x # unit: micrometer per pixel
    duration = metadata.total_time_duration.total_seconds()
    frames = metadata.image_size_t
    # speed is first calculated in pixels per frame and needs to be translated to micrometer per second
    ppf_to_μmps = resolution * frames/duration

    data = calsipro.io.read_data(image, scene)

    if mask is None:
        mask = calsipro.library.mask_variance(data)
    else:
        mask = calsipro.io.read_data(mask, None)[0, :, :]

    if peaks is None:
        peaks = calsipro.library.peaks(data, mask)
    else:
        peaks = calsipro.io.read_table(peaks)
        peaks = [(start, end) for start, end in zip(peaks["peak_start"], peaks["peak_end"])]

    fluros_names = []
    masks = []
    fluros = []
    for name, path in pairwise(flurophores):
        fluros_names.append(name)
        f_signal = calsipro.io.read_data(path, None)[0, :, :]
        f_mask = calsipro.mask.calculate_mask_intensity(f_signal)
        masks.append(f_mask)

        m, mm = np.min(f), np.max(f)
        f_norm = ((f_signal-m) / (mm-m))
        f_norm[~f_mask] = 0.0
        fluros.append(f_norm)

    unlabelled_mask = mask
    for f_mask in masks:
        unlabelled_mask = unlabelled_mask & (~f_mask)

    fluros_names.append("unlabelled")
    masks.append(unlabelled_mask)

    signal = calsipro.util.calculate_average_signal(data, mask)
    background = calsipro.background.estimate_baseline(signal)
    signal = calsipro.background.remove_background(data, background)

    results = {"beat": [], "speed": [], "origin": []}
    if len(fluros_names) > 1:
        for f_name in fluros_names:
            results[f_name + "_speed"] = []

    if mask.any():
        for peak_index, peak in enumerate(peaks):
            results["beat"].append(peak_index)
            start, end = peak
            s = signal[start:end]

            # get a beat specific variance mask
            variance_mask = calsipro.mask.calculate_mask_variance(s)
            beat_mask = mask & variance_mask

            fluros_speed = []
            ori = None
            if beat_mask.any():
                time = calsipro.speed.time_analysis(s)
                time = calsipro.speed.push_low_pixels(time, mask)
                df, speed = calsipro.speed.calculate_speed(time, mask)
                speed = ppf_to_μmps * speed

                results["speed"].append(speed)
                if len(fluros_names) > 1:
                    ori_mask = calsipro.speed.find_ori_cluster(time, mask, as_index=False)
                    f = [np.sum(fmask[ori_mask]) for fmask in fluros_mask]
                    m = np.argmax(f)
                    ori = fluros_meta[np.argmax(f)]
                    results["origin"].append(ori)

                    for fluro_name, fluro_mask in zip(fluros_names, masks):
                        if fluro_mask.any():
                            df, fluro_speed = calsipro.speed.calculate_speed(time, mask & (fluro_mask | ori_mask))
                            fluro_speed = ppf_to_μmps * fluro_speed

                            results[fluro_name + "_speed"].append(Decimal(fluro_speed).quantize(Decimal("0.01")))
                        else:
                            results[fluro_name + "_speed"].append(None)
                else:
                    results["origin"].append(None)
            else:
                results["speed"].append(None)
                results["origin"].append(None)
                if len(fluros_names) > 1:
                    for fluro_name in fluros_names:
                        results[fluro_name + "_speed"].append(None)
    calsipro.io.write_table(results, out)
