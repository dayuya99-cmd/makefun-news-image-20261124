#!/usr/bin/env python3
"""Sum up 24 November 2026 world news in one image.

A make.fun news-image-20261124 entry (Python 3, standard library only).
The entry image is the entry.png beside this file (768x1024, 417 KB,
within the gate's 1024x1024 and 1 MiB limits); the program copies it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

The image sums up Tuesday 24 November 2026 in six stories:
  1. Poland activates air defence as Russian drone enters its airspace
  2. Trump says he brought Jensen Huang back to Nvidia
  3. Ukraine reports fresh Russian strikes on Kyiv region
  4. COP31 climate talks stall in Turkiye
  5. Iran warns of countermeasures as US naval pressure mounts
  6. Indonesia factory fire kills several, workers missing

Run:  python3 main.py
Out:  entry.png in $MAKEFUN_OUTPUT_DIR (or /output/entry.png)
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
