from youtube_dl import YoutubeDL
from os.path import join, dirname, splitext
from os import remove
import subprocess
import platform
from typing import List

MASK = join(dirname(__file__), "syn2midi", "mask.bmp")
MASK88 = join(dirname(__file__), "syn2midi", "mask88.bmp")


def download_and_convert(youtube_url: str, mask_path: str = MASK88, output_name: str = None, start_time: int = None, end_time: int = None, transpose: int = 0, additional_arguments: List[str] = [], keep_video: bool = False) -> None:
    """
    Download a Synthesia piano tutorial from YouTube and convert it to MIDI format.

    Parameters
    ----------
    youtube_url: str
        The YouTube URL for a Synthesia piano tutorial.
    mask_path: str
        Path to a BMP image file to be used as mask.
    output_name: str
        Path to output MIDI file.
    start_time: int | None
        Vide start time in seconds.
    end_time: int | None
        Vide end time in seconds.
    transpose: int
        Transpose notes shift, can be negative.
    additional_arguments: List[str]
        List of additional arguments to be passed to syn2midi.
    keep_video: bool
        If set to True, will keep the downloaded video instead of deleting it when done.
    """
    filename = _download(youtube_url)
    output_name = output_name or splitext(filename)[0] + ".mid"

    syn2midi = _get_syn2midi()
    args = [syn2midi, "-i", filename, "-o",
            output_name, "-m", mask_path, "-t", str(transpose)]
    args += ["-s", str(start_time)] if start_time is not None else []
    args += ["-e", str(end_time)] if end_time is not None else []
    args += additional_arguments

    print(output_name)

    subprocess.run(args)

    if not keep_video:
        print("Deleting video...")
        try:
            remove(filename)
        except Exception:
            print("Could not delete video.")
        else:
            print("Video deleted.")


def _download(url: str) -> str:
    with YoutubeDL() as ydl:
        format_id = _get_format_id(ydl, url)

    filename = []
    options = {
        "format": format_id,
        "progress_hooks": [_get_hook(filename)]
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

    return filename[0]


def _get_hook(result: list):
    def hook(progress):
        if progress["status"] == "finished":
            result.append(progress["filename"])

    return hook


def _get_format_id(ydl: YoutubeDL, url: str):
    meta = ydl.extract_info(url, download=False)
    formats = meta.get("formats", [meta])
    mp4_formats = [format for format in formats if format["ext"] == "mp4"]
    mp4_720 = [format["format_id"]
               for format in mp4_formats if format["height"] == 720]
    if mp4_720:
        return mp4_720[0]

    mp4_formats.sort(key=lambda format: format["height"])
    return mp4_formats[-1]


def _get_syn2midi():
    systems = {
        "Windows": join("windows", "syn2midi.exe")
    }

    os = platform.system()

    if os not in systems:
        raise OSError("Operating system not supported")

    executable = systems[os]

    return join(dirname(__file__), "syn2midi", executable)


SYN2MIDI = _get_syn2midi()
