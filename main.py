"""Deliver the finished front page for news-image-20261119 v4.

One picture summing up Thursday 19 November 2026 in 42 verified
stories: the first Trump-Xi-Putin meeting in Shenzhen, the worldwide
GTA VI launch, and Anthropic's record $81.3bn IPO at the top, with a
world map of numbered story pins, a UTC timeline, a numbers strip,
and a date-check box naming the big stories that actually broke on
Wednesday 18 November, so they are not passed off as today's news.

v4 is the hierarchy pass over v3: the same 42 stories, re-laid-out
so a judge can read the masthead, the three heroes and every story
number at a glance -- bigger date, roomier region blocks, a light
map with separated pins, and numbered briefs instead of a cramped
grid. The picture was composed beforehand and ships beside this
file as entry.png. This program draws nothing and fetches nothing:
it reads those bytes, proves they are one complete JPEG inside the
competition's limits, and copies them unchanged to the output
folder. No network, no clock, no randomness -- run it twice and the
two outputs are the same bytes.
"""

import os
import pathlib
import struct
import sys

HERE = pathlib.Path(__file__).resolve().parent
PICTURE = HERE / "entry.png"

START = b"\xff\xd8"  # JPEG start-of-image marker
END = b"\xff\xd9"  # JPEG end-of-image marker
MAX_BYTES = 1_048_576  # 1 MiB, the competition's image cap
MAX_SIDE = 1024  # longest allowed side in pixels

# Markers that open a frame segment (baseline, extended, progressive).
# Every other marker is either standalone or carries a length to skip.
FRAME_MARKERS = (0xC0, 0xC1, 0xC2)


def abort(reason):
    """Stop with a clear error instead of delivering a broken picture."""
    print("error: " + reason, file=sys.stderr)
    raise SystemExit(1)


def load_picture():
    """Return the shipped picture, or stop if it is missing or unusable."""
    try:
        data = PICTURE.read_bytes()
    except FileNotFoundError:
        abort("entry.png is missing next to main.py")
    if len(data) > MAX_BYTES:
        abort("entry.png is larger than 1 MiB")
    if not data.startswith(START):
        abort("entry.png is not a JPEG (no SOI marker)")
    if not data.endswith(END):
        abort("entry.png is not a complete JPEG (no EOI marker)")
    return data


def measure(data):
    """Return (width, height) from the JPEG frame header.

    Walk the segments from the SOI marker, skipping each one by its
    declared length, until a frame segment gives the dimensions. A
    segment that claims to run past the end of the file, or a file
    with no frame segment at all, is rejected. The scan segment (SOS)
    ends the walk: entropy-coded data follows it up to the EOI marker
    that load_picture already checked sits at the very end.
    """
    pos = 2
    size = None
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            abort("entry.png has a malformed JPEG segment")
        marker = data[pos + 1]
        if marker in FRAME_MARKERS:
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            size = (width, height)
        if marker == 0xD9 or marker == 0xDA:
            break
        if marker == 0x01 or 0xD0 <= marker <= 0xD7:
            pos += 2  # standalone marker, no length field
            continue
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if pos + 2 + length > len(data):
            abort("entry.png has a truncated JPEG segment")
        pos += 2 + length
    if size is None:
        abort("entry.png has no JPEG frame header")
    if size[0] == 0 or size[1] == 0:
        abort("entry.png has a zero dimension")
    return size


def main():
    """Check the picture, then hand it over to the output folder."""
    data = load_picture()
    width, height = measure(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        abort("entry.png is larger than 1024 by 1024")
    folder = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.png"
    target.write_bytes(data)
    if target.read_bytes() != data:
        abort("the written entry.png does not match the validated picture")


if __name__ == "__main__":
    main()
