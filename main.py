"""News-image entry for 19 November 2026.

This program is the entrypoint for the make.fun competition
``news-image-20261119`` ("Sum up 19 November's world news in one image").

The image itself — a dense newspaper front page for Thursday 19 November
2026, "THE WORLD", with four lead panels and sixteen further stories across
five continents — is bundled with this repository as ``entry.png``.  This
program does one small, deterministic job: it copies that bundled image to
the output location the grader expects, ``$MAKEFUN_OUTPUT_DIR/entry.png``
(defaulting to ``out/entry.png``), so the judge sees exactly the bytes in
the repository.  No network, no randomness, no image processing — the same
bytes come out on every run.

Standard library only; Python 3.13.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


# The image bundled with this repository, next to this file.
SOURCE_IMAGE = Path(__file__).resolve().parent / "entry.png"

# Where the grader looks for the finished image.
OUTPUT_NAME = "entry.png"

# A generous sanity bound: the competition caps the image at 1 MiB.
MAX_IMAGE_BYTES = 1_048_576


def resolve_output_dir() -> Path:
    """Return the output directory from the environment, or ``out``."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("out")


def copy_entry_image(output_dir: Path) -> Path:
    """Copy the bundled image into ``output_dir`` and return its path.

    Raises a clear error when the bundled image is missing, and refuses
    to copy a file onto itself (which would happen if the output directory
    were the repository root).
    """
    if not SOURCE_IMAGE.is_file():
        raise FileNotFoundError(
            f"bundled image not found: {SOURCE_IMAGE} — "
            "entry.png must sit next to main.py"
        )

    if SOURCE_IMAGE.stat().st_size > MAX_IMAGE_BYTES:
        raise ValueError(
            f"bundled image is {SOURCE_IMAGE.stat().st_size} bytes, "
            f"over the {MAX_IMAGE_BYTES}-byte competition limit"
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME

    if destination.resolve() == SOURCE_IMAGE.resolve():
        raise ValueError(
            "refusing to copy entry.png onto itself: "
            "choose an output directory other than the repository root"
        )

    shutil.copyfile(SOURCE_IMAGE, destination)

    # The copy must be exact: same size as the bundled image, or the
    # output cannot be trusted as the entry.
    if destination.stat().st_size != SOURCE_IMAGE.stat().st_size:
        raise OSError(
            f"copy incomplete: {destination} is "
            f"{destination.stat().st_size} bytes, expected "
            f"{SOURCE_IMAGE.stat().st_size}"
        )

    return destination


def main() -> int:
    """Copy the entry image to the output directory and report success."""
    try:
        destination = copy_entry_image(resolve_output_dir())
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
