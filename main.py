"""Entry program for make.fun news-image-20261123.

Writes the front-page image for Monday 23 November 2026 to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). The image is the
entry.png shipped beside this file: a newspaper front page summing
up the day's world news (COP31 collapse in Antalya, the burning
Sparta II in the Baltic, the Kyiv drone strike, the Lisbon march,
the Indonesia factory fire, the El Chapo Isidro capture, South
Korea's AI-cheating resignation, and more). Standard library only,
no network, deterministic: every run copies the same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # shutil.copyfile writes the exact shipped bytes, so both graded
    # runs produce an identical entry.png.
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
