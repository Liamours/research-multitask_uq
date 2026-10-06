"""Package the hotspot and skeleton masks for a data record.

    uv run --no-project --with pandas --with tqdm python scripts/package_zenodo_record.py --dataset-root <BS-80K folder> --output-dir <folder>

Writes hotspot_masks.zip, skeleton_masks.zip, manifest.csv, SHA256SUMS.txt, and README.md. The masks are zipped because the record
accepts at most 100 files.
"""
from __future__ import annotations

import argparse
import bz2
import hashlib
import io
import zipfile
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from common import ROOT, TABLES

HOTSPOT_DIR = "labels/whole_body-lesion-segmentation/otsu_morphology-guarded_smooth"
SKELETON_DIR = "labels/bone_region-segmentation/pseudo_label-2607"
SKELETON_MANIFEST = "labels/bone_region-segmentation/manifest.csv.bz2"

README = """# BS-80K hotspot and skeleton masks

Masks for the whole-body bone scintigrams of BS-80K (3,247 patients, an anterior and a posterior view each). The scans are not included, they are available with the BS-80K dataset (Huang et al., Computers in Biology and Medicine 151, 2022, 106221).

## Files

| File | Content |
|:---|:---|
| `hotspot_masks.zip` | {n_hotspot:,} hotspot masks |
| `skeleton_masks.zip` | {n_skeleton:,} skeleton masks, one for every view |
| `manifest.csv` | One row per mask: mask set, patient, study, view, path in the archive, source, split, SHA-256, size in bytes |
| `SHA256SUMS.txt` | SHA-256 of the two archives |

Every mask is an 8-bit PNG of 1024 x 256 pixels, stored as `<mask set>/<patient>/<study>/<view>.png`, with the pixels of the scan of the same patient, study, and view.

## Hotspot masks

Pixel values: 0 background, 1 benign hotspot, 2 malignant hotspot. BS-80K gives one bounding box for each hotspot, marked normal (benign) or abnormal (malignant). Inside each box the mask is made by Otsu thresholding, closing and opening with a 7 x 7 elliptical kernel, and a fallback to the 75th percentile of the smoothed box when the Otsu mask is empty, covers more than 85% of the box, or touches the border of the box on more than 65% of its pixels. A view without hotspot boxes has no file. The code is in the code repository of the paper, and its output is identical to these masks.

## Skeleton masks

Pixel values: 0 background, 1 skull, 2 cervical vertebrae, 3 thoracic vertebrae, 4 ribs, 5 sternum, 6 clavicle, 7 scapula, 8 humerus, 9 lumbar vertebrae, 10 sacrum, 11 pelvis, 12 femur. The column `source` of the manifest tells how a mask was made: `manual` for the {n_manual:,} views annotated by hand, `predicted` for the {n_predicted:,} views predicted by an nnU-Net trained on the manual masks.

## Splits

The column `split` is the case split of the paper: {split_counts}. Patients that are not among the {n_cases:,} cases of the paper have the value `unused`. The split is a random 80/10/10 division of the case identifiers with seed 42, and both views of a case are in the same split.

## License

CC BY 4.0.
"""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def split_of_patient() -> dict[str, str]:
    assignment = pd.read_csv(TABLES / "split_assignment.csv")
    return {f"patient_{int(case.split('_')[1]):05d}": split for case, split in zip(assignment.case, assignment.split)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    root, out = args.dataset_root.resolve(), args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    splits = split_of_patient()
    with bz2.open(root / SKELETON_MANIFEST, "rt", encoding="utf-8") as handle:
        table = pd.read_csv(io.StringIO(handle.read()))
    skeleton_source = {(r.patient_id, r.study_id, r.view): ("manual" if r.source == "manual" else "predicted") for r in table[table.dataset == "pseudo_label"].itertuples()}
    rows = []
    for mask_set, folder in (("hotspot_masks", HOTSPOT_DIR), ("skeleton_masks", SKELETON_DIR)):
        files = sorted((root / folder).glob("patient_*/study_*/*.png"))
        with zipfile.ZipFile(out / f"{mask_set}.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in tqdm(files, desc=mask_set, unit="file"):
                patient, study, view = path.parent.parent.name, path.parent.name, path.stem
                name = f"{mask_set}/{patient}/{study}/{view}.png"
                archive.write(path, name)
                source = "thresholded from the bounding boxes" if mask_set == "hotspot_masks" else skeleton_source[(patient, study, view)]
                rows.append({"mask_set": mask_set, "patient_id": patient, "study_id": study, "view": view, "file": name, "source": source,
                             "split": splits.get(patient, "unused"), "sha256": sha256(path), "size_bytes": path.stat().st_size})
    manifest = pd.DataFrame(rows)
    manifest.to_csv(out / "manifest.csv", index=False, encoding="utf-8", lineterminator="\n")
    (out / "SHA256SUMS.txt").write_text("".join(f"{sha256(out / f'{name}.zip')}  {name}.zip\n" for name in ("hotspot_masks", "skeleton_masks")), encoding="utf-8", newline="\n")
    skeleton = manifest[manifest.mask_set == "skeleton_masks"]
    cases = pd.read_csv(TABLES / "split_assignment.csv")
    counts = ", ".join(f"{int(n):,} {name}" for name, n in cases.split.value_counts().reindex(["train", "validation", "test"]).items())
    (out / "README.md").write_text(README.format(
        n_hotspot=int((manifest.mask_set == "hotspot_masks").sum()), n_skeleton=len(skeleton), n_manual=int((skeleton.source == "manual").sum()),
        n_predicted=int((skeleton.source == "predicted").sum()), split_counts=counts + " cases", n_cases=len(cases)), encoding="utf-8", newline="\n")
    print(manifest.groupby(["mask_set", "source"]).size().to_string())
    print(manifest.groupby(["mask_set", "split"]).size().to_string())


if __name__ == "__main__":
    main()
