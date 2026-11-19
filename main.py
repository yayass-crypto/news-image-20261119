#!/usr/bin/env python3
"""news-image-20261119 round 2 — entrypoint.

The entry image is a dense newspaper front page summing up Thursday
19 November 2026: 42 stories across 6 continents, four illustrated leads
(Anthropic's record $81.3bn IPO, the Trump-Xi-Putin summit in Shenzhen,
US-Iran fire in the Gulf, Hakeem Jeffries set to become the first Black
Speaker), a world map with 12 numbered story markers, a six-continent
region column, 26 briefs and a footer ticker. The image was composed
offline with PIL; this program only copies the finished file to the
output directory, so both runs write byte-identical output.

Python 3.13 standard library only. No network, no arguments.
"""

import os
import shutil
import sys

# The finished front page lives beside this file in the repository.
SOURCE_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_NAME = "entry.png"

# The competition gate: at most 1 MiB and at most 1024x1024 px.
MAX_IMAGE_BYTES = 1048576


def resolve_output_dir():
    """Return the directory the image must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "out")


def copy_entry_image():
    """Copy entry.png to the output directory and return its path."""
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, OUTPUT_NAME)
    if os.path.abspath(dest) == os.path.abspath(SOURCE_IMAGE):
        return dest
    shutil.copyfile(SOURCE_IMAGE, dest)
    return dest


def check_image_size(path):
    """Fail loudly if the copied image breaks the 1 MiB gate."""
    size = os.path.getsize(path)
    if size > MAX_IMAGE_BYTES:
        raise ValueError(
            "entry.png is %d bytes, over the %d-byte limit" % (size, MAX_IMAGE_BYTES)
        )
    return size


def check_png_magic(path):
    """Fail loudly if the copied file is not a whole PNG."""
    with open(path, "rb") as handle:
        magic = handle.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png does not start with the PNG signature")
    return True


def main():
    dest = copy_entry_image()
    size = check_image_size(dest)
    check_png_magic(dest)
    print("wrote %s (%d bytes)" % (dest, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
