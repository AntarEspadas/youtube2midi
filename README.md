# youtube2midi

A Python module with a small cli, used to automatically download a Synthesia piano tutorial from a YouTube URL and convert it to a MIDI file. It uses [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [syn2midi](https://github.com/minyor/syn2midi).

## Installation

**youtube2midi** can be installed from PyPi using pip

`$ pip install youtube2midi`

Or from source by cloning the repo and running the command

`$ python setup.py install`

## Usage

### Command line interface

The CLI has two possible entry points

`$ youtube2midi`

and

`$ python -m youtube2midi`

Example uses:

`$ youtube2midi https://www.youtube.com/watch?v=0hhMl2W7F8U`

`$ youtube2midi https://www.youtube.com/watch?v=0hhMl2W7F8U -s 0:05 -e 3:35`

`$ youtube2midi https://www.youtube.com/watch?v=0hhMl2W7F8U -o rickroll.mid -m "path/to/my/custom/mask/file.bmp"`

Some pre-made masks can be found in the package folder, `syn2midi/mask.bmp` and `syn2midi/mask88.bmp`

Command line reference:

```
youtube2midi [-h] [-o OUTPUT] [-m MASK] [-t TRANSPOSE] [-s START] [-e END] [-k] url

positional arguments:
  url                   URL to a Synthesia youtube video

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of output MIDI file
  -m MASK, --mask MASK  Path to a BMP image file to be used as mask. See https://github.com/minyor/syn2midi for details
  -t TRANSPOSE, --transpose TRANSPOSE
                        transpose notes shift, can be negative. 0 is default
  -s START, --start START
                        Start timestamp for video in the form mm:ss
  -e END, --end END     End timestamp for video in the form mm:ss
  -k, --keep-video      Keep the downloaded YouTube video instead of deleting it when done
```

### Python module

The python module exposes a single function `download_and_convert`

```python
>>> from youtube2midi import download_and_convert, MASK88
>>> download_and_convert('https://www.youtube.com/watch?v=0hhMl2W7F8U',
                        MASK88, output_name='rickroll.mid', start_time=5, end_time=3 * 60 + 35)
```