"""Image-level malignant detection AUC without any uncertainty method.

An image is positive when its ground truth has a malignant hotspot. The score is the number of predicted malignant pixels.
Predictions are those of the standard prediction pipeline on the 293 test cases (586 images).

    uv run --no-project --with pandas --with numpy --with pillow --with matplotlib --with tqdm python scripts/compute_image_auc.py --project <project folder>
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from common import MODEL_ORDER, ROOT, TABLES, read_table
from make_figures import prediction, truth_classes


def auc(positive: pd.Series, score: pd.Series) -> float:
    ranks = score.rank(method="average")
    n_pos, n_neg = int(positive.sum()), int((~positive).sum())
    return float((ranks[positive].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=ROOT.parents[1])
    project = parser.parse_args().project.resolve()
    split = read_table("split_assignment.csv")
    rows = []
    for case in tqdm(sorted(split[split.split == "test"].case), desc="images"):
        for view in ("anterior", "posterior"):
            row = {"case": case, "view": view, "positive": bool((truth_classes(project, case, view) == 2).any())}
            for model in MODEL_ORDER:
                row[model] = int(prediction(project, model, case, view)[1].sum())
            rows.append(row)
    scores = pd.DataFrame(rows)
    summary = pd.DataFrame([{"model": m, "positive_images": int(scores.positive.sum()), "negative_images": int((~scores.positive).sum()), "auc": auc(scores.positive, scores[m])} for m in MODEL_ORDER])
    summary.to_csv(TABLES / "image_level_auc.csv", index=False, encoding="utf-8")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
