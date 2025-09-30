from PIL import Image
import openpyxl
import numpy as np
import polars as pl
from calsipro.util import moving_average
from bioio import BioImage
import ffmpeg
import select

def read_image(img):
    if isinstance(img, BioImage):
        return img
    return BioImage(img, use_aicspylibczi=True)


def show_scenes(inp):
    img = read_image(inp)
    return img.scenes


def read_data(inp, scene=None, requested_frames=None, average=0):
    img = read_image(inp)

    if scene is None:
        scene = img.scenes[0]

    img.set_scene(scene)

    if requested_frames is None:
        frames = img.dims['T'][0]
        requested_frames = [(0, frames-average-1)]

    data = img.data
    images = []
    for frame_request in requested_frames:
        start, stop = frame_request
        if start < average:
            start_cut = average-start
        else:
            start_cut = average
        start, stop = start-start_cut, stop+average

        start = max(0, start)
        stop = max(min(frames-1, stop), start+1)

        image = data[start:stop, 0, 0, :, :]

        if average > 1:
            image = moving_average(image, n=average)
        image = image[start_cut:stop-start-average, :, :]
        images.append(image)
    if len(images) == 1:
        return images[0]
    return images


def write_table(df, path):
    df = pl.DataFrame(df)
    if path.endswith(".parquet"):
        df.write_parquet(path)
    elif path.endswith(".csv"):
        df.write_csv(path)
    else:
        raise KeyError("File Ending not supported")


def read_table(path):
    if path.endswith(".parquet"):
        return pl.read_parquet(path)
    elif path.endswith(".csv"):
        return pl.read_csv(path)
    else:
        raise KeyError("File Ending not supported")


WRITER_PACKAGES = {
    "OmeTiffWriter": "bioio-ome-tiff",
    "OmeZarrWriterV3": "bioio-ome-zarr",
    "TimeSeriesWriter": "bioio-imageio",
    "TwoDWriter": "bioio-imageio",
}


WRITERS = {
    ".ome.tiff": "OmeTiffWriter",
    ".ome.tif": "OmeTiffWriter",
    ".ome.zarr": "OmeZarrWriterV3",
    ".gif": "TimeseriesWriter",
    ".mp4": "TimeseriesWriter",
    ".mkv": "TimeseriesWriter",
    ".png": "TwoDWriter",
    ".bmp": "TwoDWriter",
    ".jpg": "TwoDWriter",
    }


def _get_writer(name):
    parts = name.split(".")
    potential_endings = []
    if len(parts) > 2:
        potential_endings.append("." + parts[-2] + "." + parts[-1])
    if len(parts) > 1:
        potential_endings.append("." + parts[-1])

    writer_name = None
    for ending in potential_endings:
        writer_name = WRITERS.get(ending)
        if writer_name:
            break

    if writer_name is None:
        raise KeyError(f"Could not identify writer for path `{name}`")

    import bioio.writers
    try:
        return getattr(bioio.writers, writer_name)
    except AttributeError:
        raise ValueError(f"Writer {writer_name} is not installed, install package {WRITER_PACKAGES[writer_name]}.")


def write_data(data, path):
    writer = _get_writer(path)
    writer.save(data, path)


def encode_video(data, width=100, height=100, fps=5, encoder="h264"):
    if encoder == "vp9":
        p = (ffmpeg
        .input('pipe:', format='rawvideo', pix_fmt='gray', s='{}x{}'.format(data.shape[-2], data.shape[-1]), r=fps)
        .output("pipe:1", format="webm", s=f"{width}x{height}", pix_fmt="yuv420p", deadline="realtime", crf="30", **{"row-mt": "1", "b:v": "2000k", "tile-columns": 3, "c:v": "libvpx-vp9"})
        .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True))
    elif encoder == "h264":
        p = (ffmpeg
        .input('pipe:', format='rawvideo', pix_fmt='gray', s='{}x{}'.format(data.shape[-2], data.shape[-1]), r=fps)
        .output("pipe:1", format="mp4", movflags="frag_keyframe+empty_moov", s=f"{width}x{height}", pix_fmt="yuv420p", preset="fast", tune="zerolatency", crf="22", **{"c:v": "libx264"})
        .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True))
    else:
        raise ValueError(f"Unknown encoder {encoder}, only supported are 'vp9' and 'h264'")

    b = data.tobytes()
    outs, errs = p.communicate(input=b)

    if len(outs) == 0:
        raise Exception("Video was not generated correctly\n\n"+errs.decode("utf8"))

    return outs

