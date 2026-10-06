"""Turn the bounding boxes of every image into one class mask (1 benign, 2 malignant)."""
from __future__ import annotations

import json
import logging
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm

from .algorithm import BBox, box_mask
from .boxes import read_boxes
from .owner_map import _build_owner_map, _finalize_owner_map, _owner_to_class_mask


def image_mask(image: np.ndarray, boxes: list[BBox], config: dict) -> tuple[np.ndarray, list[str]]:
    specs, paths = [], []
    for index, box in enumerate(boxes):
        roi_mask, path = box_mask(image, box, config["algorithm"])
        paths.append(path)
        label_value = int(config["labels"][box.label.lower()])
        full = np.zeros(image.shape, dtype=np.uint8)
        full[box.ymin:box.ymax, box.xmin:box.xmax] = roi_mask
        binary = (full > 0).astype(np.uint8)
        specs.append({"bbox_index": index, "owner_id": index + 1, "bbox": box, "label_value": label_value,
                      "fallback_roi": (roi_mask > 0).astype(np.uint8), "full_mask": binary * label_value, "full_binary": binary})
    owner, _ = _finalize_owner_map(_build_owner_map(image.shape, specs), specs)
    return _owner_to_class_mask(owner, specs), paths


def run(dataset_root: Path, output_dir: Path, config: dict, views: list[str], limit: int | None, overwrite: bool, log_path: Path) -> None:
    logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s %(message)s", encoding="utf-8")
    boxes = read_boxes(dataset_root)
    keys = sorted(key for key in boxes if key[1] in views)[:limit]
    shares = {"otsu": 0, "percentile": 0, "ellipse": 0, "empty": 0}
    for patient, view in tqdm(keys, desc="images", unit="img"):
        study = sorted((dataset_root / config["raw_dir"] / patient).glob("study_*"))[0].name
        target = output_dir / patient / study / f"{view}.png"
        if target.is_file() and not overwrite:
            continue
        image = cv2.imread(str(dataset_root / config["raw_dir"] / patient / study / f"{view}.png"), cv2.IMREAD_GRAYSCALE)
        if image is None or list(image.shape) != config["image_shape"]:
            raise ValueError(f"unexpected image {patient} {view}")
        mask, paths = image_mask(image, boxes[(patient, view)], config)
        target.parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(target), mask)
        for path in paths:
            shares[path] += 1
        logging.info("%s %s boxes=%d", patient, view, len(paths))
    total = sum(shares.values())
    summary = {"boxes": total, **{f"{name}_boxes": count for name, count in shares.items()}}
    (output_dir / "path_shares.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(summary)
