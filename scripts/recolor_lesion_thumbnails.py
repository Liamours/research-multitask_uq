"""Recolor the lesion mask thumbnails of the architecture diagrams to the hotspot palette.

The old thumbnails draw malignant hotspots in orange (213, 94, 0) and benign hotspots in sky blue (86, 180, 233).
They are recolored to malignant red (215, 25, 25) and benign green (30, 160, 60). Only the area around the
thumbnail pixels of those two colors is touched, so the skeleton thumbnails and the network drawings stay as they are.

    uv run --no-project --with pillow --with numpy --with tqdm python scripts/recolor_lesion_thumbnails.py --out <folder>
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image
from tqdm import tqdm

OLD_MALIGNANT, OLD_BENIGN = (213, 94, 0), (86, 180, 233)
NEW_MALIGNANT, NEW_BENIGN = (215, 25, 25), (30, 160, 60)
TOLERANCE = 12
PAD = 8
GROUP_GAP = 200
MIN_X = 3400
FILES = ["nnunet_plain_models.png", "nnunet_cbam_models.png", "segformer_models.png"]


def exact(img: np.ndarray, color: tuple[int, int, int]) -> np.ndarray:
    return (np.abs(img - np.array(color)) < TOLERANCE).all(axis=-1)


def thumbnail_boxes(mask: np.ndarray) -> list[tuple[int, int, int, int]]:
    ys, xs = np.where(mask)
    keep = xs >= MIN_X
    ys, xs = ys[keep], xs[keep]
    if not len(ys):
        return []
    order = np.argsort(ys)
    ys, xs = ys[order], xs[order]
    cuts = np.where(np.diff(ys) > GROUP_GAP)[0] + 1
    return [(g_x.min() - PAD, g_y.min() - PAD, g_x.max() + PAD, g_y.max() + PAD) for g_y, g_x in zip(np.split(ys, cuts), np.split(xs, cuts))]


def recolor_box(img: np.ndarray, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    area = img[y0:y1 + 1, x0:x1 + 1]
    spread = area.max(axis=-1) - area.min(axis=-1)
    orange = (spread > 25) & (area[..., 0] > area[..., 2])
    blue = (spread > 25) & (area[..., 2] > area[..., 0])
    for pixels, alpha, new in (
        (orange, (255 - area[..., 1]) / (255 - OLD_MALIGNANT[1]), NEW_MALIGNANT),
        (blue, (255 - area[..., 0]) / (255 - OLD_BENIGN[0]), NEW_BENIGN),
    ):
        a = np.clip(alpha, 0, 1)[..., None]
        blended = a * np.array(new) + (1 - a) * 255
        area[pixels] = blended[pixels]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--src", type=Path, default=Path(__file__).resolve().parents[1] / "figures" / "architecture")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for name in tqdm(FILES, desc="diagrams"):
        img = np.array(Image.open(args.src / name).convert("RGB")).astype(float)
        mask = exact(img, OLD_MALIGNANT) | exact(img, OLD_BENIGN)
        for box in thumbnail_boxes(mask):
            recolor_box(img, box)
        Image.fromarray(np.clip(img.round(), 0, 255).astype(np.uint8)).save(args.out / name)
    print(f"wrote {len(FILES)} files to {args.out}")


if __name__ == "__main__":
    main()
