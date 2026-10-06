from __future__ import annotations

import math
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "tables"
FIGURES = ROOT / "figures"

BENIGN_RGB = (30, 160, 60)
MALIGNANT_RGB = (215, 25, 25)

CHECKPOINTS = [
    ("nnunet_single", "nnU-Net", "single-task"),
    ("nnunet_early", "nnU-Net", "Early"),
    ("nnunet_earlymid", "nnU-Net", "Early-Mid"),
    ("nnunet_mid", "nnU-Net", "Mid"),
    ("nnunet_late", "nnU-Net", "Late"),
    ("nnunetcbam_single", "nnU-Net + CBAM", "single-task"),
    ("nnunetcbam_multidecoder", "nnU-Net + CBAM", "Early"),
    ("nnunetcbam_earlymid", "nnU-Net + CBAM", "Early-Mid"),
    ("nnunetcbam_mid", "nnU-Net + CBAM", "Mid"),
    ("nnunetcbam_multihead", "nnU-Net + CBAM", "Late"),
    ("segformer_single", "SegFormer", "single-task"),
    ("segformer_early", "SegFormer", "Early"),
    ("segformer_mid", "SegFormer", "Mid"),
    ("segformer_late", "SegFormer", "Late"),
]
MODEL_ORDER = [name for name, _, _ in CHECKPOINTS]
BACKBONE = {name: backbone for name, backbone, _ in CHECKPOINTS}
FISSION = {name: fission for name, _, fission in CHECKPOINTS}
PROPOSED = "nnunetcbam_multidecoder"
MULTITASK = [name for name in MODEL_ORDER if FISSION[name] != "single-task"]

METHOD_NAMES = {
    "mean_normalized_entropy": "Predictive entropy",
    "lguq": "Local gradient UQ",
    "metaseg": "MetaSeg",
    "standardized_max_logit": "Standardized max logit",
    "one_minus_mean_max_softmax": "Max-softmax",
    "mahalanobis": "Mahalanobis distance",
    "inverse_area": "Inverse area (control)",
    "random_removal": "Random removal",
    "no_uq": "No UQ",
}
PAPER_METHODS = ["mean_normalized_entropy", "lguq", "metaseg", "standardized_max_logit"]
EXTRA_METHODS = ["one_minus_mean_max_softmax", "mahalanobis", "inverse_area"]
ALL_METHODS = PAPER_METHODS + EXTRA_METHODS

TARGETS = ["malignant", "benign"]
BONE_REGIONS = [
    "Skull", "Cervical vertebrae", "Thoracic vertebrae", "Ribs", "Sternum", "Clavicle",
    "Scapula", "Humerus", "Lumbar vertebrae", "Sacrum", "Pelvis", "Femur",
]

DICE_UQ_RUN = (
    "Dice is the mean over the test images whose ground truth contains the class "
    "(203 malignant, 473 benign), computed on the predictions of the UQ run, one full-image forward pass per view."
)


def project_folder(project: Path, name: str) -> Path:
    """The one folder draft/<paper>/<name> of the project, found without naming the paper."""
    matches = sorted(project.glob(f"draft/*/{name}"))
    if len(matches) != 1:
        raise FileNotFoundError(f"expected one draft/*/{name} folder in {project}, found {len(matches)}")
    return matches[0]


def read_table(name: str) -> pd.DataFrame:
    return pd.read_csv(TABLES / name)


def label(model: str) -> str:
    return f"{BACKBONE[model]}, {FISSION[model]}"


def order_models(frame: pd.DataFrame, column: str = "model") -> pd.DataFrame:
    rank = {name: index for index, name in enumerate(MODEL_ORDER)}
    return frame.assign(_rank=frame[column].map(rank)).sort_values("_rank", kind="stable").drop(columns="_rank")


def num(value, digits: int = 4, signed: bool = False) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"
    return f"{value:+.{digits}f}" if signed else f"{value:.{digits}f}"


def pval(value) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "-"
    return "<0.001" if value < 0.001 else f"{value:.3f}"


def interval(low, high, digits: int = 4, signed: bool = True) -> str:
    return f"[{num(low, digits, signed)}, {num(high, digits, signed)}]"


def md_table(header: list[str], rows: list[list[str]], align: str | None = None) -> str:
    align = align or ("l" + "r" * (len(header) - 1))
    rule = "|".join(":---" if a == "l" else "---:" for a in align)
    lines = ["| " + " | ".join(header) + " |", "|" + rule + "|"]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines)


def write_section(name: str, parts: list[str]) -> Path:
    path = ROOT / name
    path.write_text("\n\n".join(part.strip("\n") for part in parts) + "\n", encoding="utf-8", newline="\n")
    return path
