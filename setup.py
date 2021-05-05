from setuptools import setup, find_packages
from os.path import dirname, join

VERSION = '0.1.1'
DESCRIPTION = "A Python module with a small cli, used to automatically download a Synthesia piano tutorial from a YouTube URL and convert it to a MIDI file."

try:
    with open(join(dirname(__file__), "README.md")) as readme:
        LONG_DESCRIPTION = readme.read()
except Exception:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name="youtube2midi",
    license="MIT",
    url="https://github.com/Naratna/youtube2midi",
    download_url="https://github.com/Naratna/youtube2midi/archive/refs/tags/v0.1.1.tar.gz",
    version=VERSION,
    author="Naratna",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "youtube-dl"
    ],
    entry_points={
        "console_scripts": [
            "youtube2midi = youtube2midi.cli:run"
        ]
    },

    keywords=['python', 'midi', 'youtube'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ]
)
