"""Threshold the BS-80K hotspot bounding boxes into masks.

    uv run --no-project --with numpy --with opencv-python-headless --with tqdm python generate_hotspot_masks.py \
        --dataset-root <BS-80K folder> --output-dir <folder for the masks>

The dataset folder holds data/whole_body-raster-raw/ and labels/whole_body-lesion-bb/bounding_boxes.csv(.bz2).
Masks are written as <output>/<patient>/<study>/<view>.png with 1 for benign and 2 for malignant. A rerun skips
the images already written. Settings are in config.json.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from hotspot_masks.runner import run


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.json"))
    parser.add_argument("--views", nargs="+", default=["anterior", "posterior"])
    parser.add_argument("--limit", type=int, default=None, help="process only the first N images")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    run(args.dataset_root, args.output_dir, config, args.views, args.limit, args.overwrite, args.output_dir / "run.log")


if __name__ == "__main__":
    main()
