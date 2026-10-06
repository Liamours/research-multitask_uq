"""Build the labeled figures of the supplementary sections.

    uv run --no-project --with pandas --with numpy --with pillow --with matplotlib --with tqdm python scripts/make_figures.py <command> --project <project root>

Commands: uq_examples (S5), comparison (S7), curves (S9), hotspot (S11), all.
`comparison` needs the saved test predictions of the fourteen checkpoints. Nothing is trained or re-run.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm

from common import BACKBONE, PROPOSED, project_folder, BENIGN_RGB, FIGURES, FISSION, MALIGNANT_RGB, MODEL_ORDER, ROOT, TABLES, label, read_table

plt.rcParams.update({"font.family": "serif", "font.size": 8, "axes.linewidth": 0.5})

UQ_COLUMNS = [("raw_inverted", "Scan"), ("ground_truth", "Ground truth"), ("prediction", "Prediction"),
              ("mean_normalized_entropy", "Predictive entropy"), ("lguq", "Local gradient UQ"), ("metaseg", "MetaSeg"),
              ("standardized_max_logit", "Standardized max logit")]
RAW_DIR = "datasets/source/bs80k/data/whole_body-raster-raw"
LESION_DIR = "datasets/source/bs80k/labels/whole_body-lesion-segmentation/otsu_morphology-guarded_smooth"
INFERENCE = {
    "nnunet": "results/inferences/nnunet",
    "segformer": "results/inferences/segformer",
}
SEGFORMER_RUN = {"segformer_single": "single_task", "segformer_early": "dual_decoder", "segformer_mid": "dual_fuse", "segformer_late": "dual_head"}
CATEGORIES = [("easy", 2), ("hard", 2), ("failure", 2), ("missed", 2)]


def read_gray(path: Path) -> np.ndarray:
    for candidate in (path, path.with_name(path.name + ".png"), path.with_suffix(".png")):
        if candidate.is_file():
            array = np.asarray(Image.open(candidate))
            return array[..., 0] if array.ndim == 3 else array
    raise FileNotFoundError(path)


def window(mask: np.ndarray, shape: tuple[int, int], margin: int, minimum: int) -> tuple[int, int, int, int]:
    rows, cols = np.where(mask)
    if rows.size == 0:
        return 0, shape[0], 0, shape[1]
    top, bottom, left, right = rows.min() - margin, rows.max() + margin, cols.min() - margin, cols.max() + margin
    height, width = bottom - top, right - left
    if height < minimum:
        top, bottom = top - (minimum - height) // 2, bottom + (minimum - height + 1) // 2
    if width < minimum:
        left, right = left - (minimum - width) // 2, right + (minimum - width + 1) // 2
    top, left = max(top, 0), max(left, 0)
    bottom, right = min(bottom, shape[0]), min(right, shape[1])
    return top, bottom, left, right


def uq_examples(project: Path) -> None:
    out = FIGURES / "uq_examples"
    out.mkdir(parents=True, exist_ok=True)
    folders = sorted((project_folder(project, "components") / "supplementary/uq_examples/uq_agreement").iterdir())
    for folder in tqdm(folders, desc="uq examples"):
        views = []
        for view in ("anterior", "posterior"):
            images = {key: np.asarray(Image.open(folder / f"{view}_{key}.png").convert("RGB")) for key, _ in UQ_COLUMNS}
            changed = np.zeros(images["raw_inverted"].shape[:2], dtype=bool)
            for key, _ in UQ_COLUMNS[1:]:
                changed |= np.any(images[key] != images["raw_inverted"], axis=2)
            if changed.any():
                views.append((view, images, window(changed, changed.shape, 24, 96)))
        fig, axes = plt.subplots(len(views), len(UQ_COLUMNS), figsize=(10.5, 1.9 * len(views) + 0.4), squeeze=False)
        for row, (view, images, (top, bottom, left, right)) in enumerate(views):
            for column, (key, title) in enumerate(UQ_COLUMNS):
                axis = axes[row][column]
                axis.imshow(images[key][top:bottom, left:right])
                axis.set_xticks([]), axis.set_yticks([])
                for spine in axis.spines.values():
                    spine.set_linewidth(0.4)
                if row == 0:
                    axis.set_title(title, fontsize=8)
                if column == 0:
                    axis.set_ylabel(view.capitalize(), fontsize=8)
        fig.tight_layout(pad=0.4)
        fig.savefig(out / f"{folder.name}.png", dpi=200)
        plt.close(fig)


def dataset_paths(project: Path, case: str, view: str) -> tuple[Path, Path]:
    patient = f"patient_{int(case.split('_')[1]):05d}"
    study = sorted((project / RAW_DIR / patient).glob("study_*"))[0].name
    return project / RAW_DIR / patient / study / f"{view}.png", project / LESION_DIR / patient / study / f"{view}.png"


def truth_classes(project: Path, case: str, view: str) -> np.ndarray:
    """Ground-truth lesion labels (1 benign, 2 malignant). A view without a label file has no hotspot."""
    try:
        return read_gray(dataset_paths(project, case, view)[1])
    except FileNotFoundError:
        return np.zeros((1024, 256), dtype=np.uint8)


def prediction(project: Path, model: str, case: str, view: str) -> tuple[np.ndarray, np.ndarray]:
    """Boolean benign and malignant masks of one checkpoint on one test image, from the standard prediction pipeline."""
    if model.startswith("segformer"):
        folder = project / INFERENCE["segformer"] / SEGFORMER_RUN[model] / "test" / case
        classes = read_gray(folder / f"lesion_{view}.png")
        malignant = (read_gray(folder / f"lesion_malignant_{view}.png") > 0) | (classes == 2)
        return (classes == 1) & ~malignant, malignant
    classes = read_gray(project / INFERENCE["nnunet"] / model / "test" / "lesion" / view / f"{case}.png")
    return classes == 1, classes == 2


def dice(pred: np.ndarray, truth: np.ndarray) -> float:
    total = pred.sum() + truth.sum()
    return 1.0 if total == 0 else 2.0 * float((pred & truth).sum()) / float(total)


def select(table: pd.DataFrame) -> pd.DataFrame:
    values = table[MODEL_ORDER]
    table = table.assign(mean_dice=values.mean(axis=1), best_dice=values.max(axis=1),
                         checkpoints_found=(values >= 0.3).sum(axis=1), proposed_dice=table["nnunetcbam_multidecoder"])
    table = table.sort_values(["case", "view"]).reset_index(drop=True)
    chosen = []
    pools = {
        "easy": table.sort_values("mean_dice", ascending=False, kind="stable"),
        "hard": table[table.best_dice >= 0.5].sort_values("mean_dice", kind="stable"),
        "failure": table[table.best_dice == 0].sort_values("truth_pixels", ascending=False, kind="stable"),
        "missed": table[(table.proposed_dice == 0) & (table.checkpoints_found >= 7)].sort_values("checkpoints_found", ascending=False, kind="stable"),
    }
    for name, count in CATEGORIES:
        for position, (_, row) in enumerate(pools[name].head(count).iterrows(), start=1):
            chosen.append({"category": name, "example": position, **row.to_dict()})
    return pd.DataFrame(chosen)


def overlay(raw: np.ndarray, benign: np.ndarray, malignant: np.ndarray, alpha: float = 0.85) -> np.ndarray:
    canvas = np.repeat((255 - raw)[..., None], 3, axis=2).astype(np.float32)
    for mask, colour in ((benign, BENIGN_RGB), (malignant, MALIGNANT_RGB)):
        canvas[mask] = (1 - alpha) * canvas[mask] + alpha * np.array(colour, dtype=np.float32)
    return canvas.astype(np.uint8)


def comparison(project: Path) -> None:
    split = read_table("split_assignment.csv")
    cases = sorted(split[split.split == "test"].case)
    rows = []
    for case in tqdm(cases, desc="malignant Dice per image"):
        for view in ("anterior", "posterior"):
            truth = truth_classes(project, case, view) == 2
            if not truth.any():
                continue
            row = {"case": case, "view": view, "truth_pixels": int(truth.sum())}
            for model in MODEL_ORDER:
                row[model] = dice(prediction(project, model, case, view)[1], truth)
            rows.append(row)
    dice_table = pd.DataFrame(rows)
    dice_table.to_csv(TABLES / "malignant_dice_by_image.csv", index=False, encoding="utf-8")
    check = read_table("dice_by_model.csv")
    check = check[check.target == "malignant"].set_index("model")["published_run_dice_lesion_bearing"]
    print(f"{len(dice_table)} images with a malignant hotspot")
    for model in MODEL_ORDER:
        print(f"{model:26s} here {dice_table[model].mean():.4f}  csv {check[model]:.4f}")
    chosen = select(dice_table)
    chosen.to_csv(TABLES / "comparison_examples.csv", index=False, encoding="utf-8")
    out = FIGURES / "comparison"
    out.mkdir(parents=True, exist_ok=True)
    for _, row in tqdm(chosen.iterrows(), total=len(chosen), desc="comparison figures"):
        case, view = row["case"], row["view"]
        raw = read_gray(dataset_paths(project, case, view)[0])
        classes = truth_classes(project, case, view)
        panels = [("Ground truth", classes == 1, classes == 2)]
        union = classes == 2
        for model in MODEL_ORDER:
            benign, malignant = prediction(project, model, case, view)
            panels.append((f"{label(model)}\nDice {row[model]:.3f}", benign, malignant))
        top, bottom, left, right = window(union, raw.shape, 40, 120)
        fig, axes = plt.subplots(3, 5, figsize=(9.0, 3 * 2.35))
        for axis, (title, benign, malignant) in zip(axes.ravel(), panels):
            axis.imshow(overlay(raw, benign, malignant)[top:bottom, left:right])
            axis.set_title(title, fontsize=7)
            axis.set_xticks([]), axis.set_yticks([])
            for spine in axis.spines.values():
                spine.set_linewidth(0.4)
        fig.tight_layout(pad=0.4)
        fig.savefig(out / f"{row['category']}_{row['example']}_{case}_{view}.png", dpi=170)
        plt.close(fig)


def curves(project: Path) -> None:
    out = FIGURES / "training_curves"
    fig, axis = plt.subplots(figsize=(5.2, 3.0))
    for model, style in zip(("segformer_single", "segformer_early", "segformer_mid", "segformer_late"), ("-", "--", "-.", ":")):
        data = read_table(f"curve_{model}.csv")
        axis.plot(data.epoch, data.validation_foreground_mean_dice, style, color="black", linewidth=1.0, label=label(model))
    axis.set_xlabel("Epoch"), axis.set_ylabel("Validation foreground mean Dice")
    axis.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    fig.savefig(out / "segformer_validation_dice.png", dpi=200)
    plt.close(fig)


def hotspot(project: Path) -> None:
    steps = [("scan_box", "Scan and box"), ("otsu", "Otsu threshold"), ("closed_opened", "Closing, then opening"),
             ("percentile", "75th percentile of smoothed box"), ("final", "Hotspot mask")]
    rows = [("otsu", "Otsu path"), ("percentile", "Percentile path")]
    fig, axes = plt.subplots(2, 5, figsize=(8.0, 3.6))
    for row, (path, title) in enumerate(rows):
        for column, (key, caption) in enumerate(steps):
            axis = axes[row][column]
            axis.set_xticks([]), axis.set_yticks([])
            if path == "otsu" and key == "percentile":
                axis.text(0.5, 0.5, "not applied", ha="center", va="center", fontsize=7, transform=axis.transAxes)
            else:
                axis.imshow(Image.open(FIGURES / "hotspot_steps" / f"{path}_{key}.png").convert("RGB"))
            if row == 0:
                axis.set_title(caption, fontsize=7)
            if column == 0:
                axis.set_ylabel(title, fontsize=8)
    fig.tight_layout(pad=0.4)
    fig.savefig(FIGURES / "hotspot_steps" / "hotspot_mask_steps.png", dpi=200)
    plt.close(fig)


def summary_values() -> pd.DataFrame:
    dice = read_table("dice_by_model.csv")
    malignant = dice[dice.target == "malignant"].set_index("model").uq_run_dice_lesion_bearing
    config = read_table("uq_discrimination_by_config.csv")
    auc = config[config.method == "metaseg"].groupby("model").auroc.mean()
    return pd.DataFrame({"dice": malignant, "auc": auc}).reindex(MODEL_ORDER)


def summary(project: Path) -> None:
    values = summary_values()
    rows, ticks, position = [], [], 0
    for index, model in enumerate(MODEL_ORDER):
        if index and BACKBONE[model] != BACKBONE[MODEL_ORDER[index - 1]]:
            position += 1
        rows.append(position)
        ticks.append(f"{FISSION[model]}")
        position += 1
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 4.6), sharey=True)
    for axis, column, title in zip(axes, ("dice", "auc"), ("Malignant Dice", "MetaSeg region AUC")):
        colors = ["black" if model == PROPOSED else "#a8a8a8" for model in MODEL_ORDER]
        axis.barh(rows, values[column], color=colors, height=0.72)
        for y, value in zip(rows, values[column]):
            axis.text(value + 0.006, y, f"{value:.4f}", va="center", fontsize=6.5)
        axis.set_xlim(0, 0.95), axis.set_title(title, fontsize=9)
        axis.spines[["top", "right"]].set_visible(False)
    axes[0].invert_yaxis()
    axes[0].set_yticks(rows, ticks, fontsize=7.5)
    for backbone in dict.fromkeys(BACKBONE[m] for m in MODEL_ORDER):
        members = [row for row, model in zip(rows, MODEL_ORDER) if BACKBONE[model] == backbone]
        axes[0].text(-0.30, sum(members) / len(members), backbone, ha="right", va="center", fontsize=8, fontweight="bold", transform=axes[0].get_yaxis_transform())
    fig.tight_layout()
    fig.savefig(FIGURES / "summary_dice_and_auc.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["uq_examples", "comparison", "curves", "hotspot", "summary", "all"])
    parser.add_argument("--project", type=Path, default=ROOT.parents[1])
    args = parser.parse_args()
    project = args.project.resolve()
    commands = {"uq_examples": uq_examples, "comparison": comparison, "curves": curves, "hotspot": hotspot, "summary": summary}
    for name in ([args.command] if args.command != "all" else list(commands)):
        commands[name](project)


if __name__ == "__main__":
    main()
