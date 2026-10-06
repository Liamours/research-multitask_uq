"""Compare generated masks with a reference label folder of the same layout.

    uv run --no-project --with numpy --with opencv-python-headless --with tqdm python verify_against_labels.py \
        --generated <masks> --reference <labels folder>
"""
from __future__ import annotations

import argparse
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generated", type=Path, required=True)
    parser.add_argument("--reference", type=Path, required=True)
    args = parser.parse_args()
    files = sorted(args.generated.glob("patient_*/study_*/*.png"))
    identical, different = 0, []
    for path in tqdm(files, desc="compare", unit="img"):
        reference = cv2.imread(str(args.reference / path.relative_to(args.generated)), cv2.IMREAD_UNCHANGED)
        generated = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
        if reference is not None and reference.shape == generated.shape and np.array_equal(reference, generated):
            identical += 1
        else:
            different.append(path.relative_to(args.generated).as_posix())
    print(f"{identical} of {len(files)} masks are identical to the reference")
    for name in different[:20]:
        print("different:", name)


if __name__ == "__main__":
    main()
