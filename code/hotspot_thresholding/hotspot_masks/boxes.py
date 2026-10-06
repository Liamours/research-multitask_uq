"""Read the bounding boxes of BS-80K and group them by image."""
from __future__ import annotations

import bz2
import csv
from collections import defaultdict
from pathlib import Path

from .algorithm import BBox

BOX_FILE = "labels/whole_body-lesion-bb/bounding_boxes.csv"


def resolve(path: Path) -> Path:
    for candidate in (path, path.with_name(path.name + ".bz2")):
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(path)


def read_boxes(dataset_root: Path) -> dict[tuple[str, str], list[BBox]]:
    """Boxes in file order, keyed by (patient folder, view). Boxes without area are dropped."""
    path = resolve(dataset_root / BOX_FILE)
    opener = bz2.open if path.suffix == ".bz2" else open
    grouped: dict[tuple[str, str], list[BBox]] = defaultdict(list)
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            x, y = int(float(row["x"])), int(float(row["y"]))
            box = BBox(xmin=x, ymin=y, xmax=x + int(float(row["width"])), ymax=y + int(float(row["height"])), label=row["name"].strip())
            if box.is_valid:
                grouped[(row["patient_id"], row["view"])].append(box)
    return grouped
