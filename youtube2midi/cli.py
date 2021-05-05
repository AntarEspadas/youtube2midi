from argparse import ArgumentParser
from .converter import download_and_convert, MASK88
from os.path import dirname, join
from datetime import datetime


def run():
    parser = _get_parser()

    args = parser.parse_args()

    args.mask = args.mask or MASK88

    download_and_convert(args.url, args.mask, args.output, _seconds(
        args.start), _seconds(args.end), args.transpose, [], args.keep)


def _seconds(timestamp: str):
    if timestamp is None:
        return None

    date_time = datetime.strptime(timestamp, "%M:%S")
    delta = date_time - datetime(1900, 1, 1)

    return delta.total_seconds()


def _get_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Download a Synesthesia video from YouTube and convert it to a MIDI file")

    parser.add_argument(
        "url", type=str, help="URL to a Synesthesia YouTube video")

    parser.add_argument("-o", "--output", type=str,
                        default=None, help="Name of output MIDI file")

    parser.add_argument("-m", "--mask", type=str, default=None,
                        help="Path to a BMP image file to be used as mask. See https://github.com/minyor/syn2midi for details")

    parser.add_argument("-t", "--transpose", type=int, default=0,
                        help="Transpose notes shift, can be negative. 0 is default")

    form = "mm:ss"

    parser.add_argument("-s", "--start", type=str, default=None,
                        help=f"Start timestamp for video in the form {form}")

    parser.add_argument("-e", "--end", type=str, default=None,
                        help=f"End timestamp for video in the from {form}")

    parser.add_argument("-k", "--keep-video", action="store_true", dest="keep",
                        help=f"Keep the downloaded YouTube video instead of deleting it when done")

    return parser
