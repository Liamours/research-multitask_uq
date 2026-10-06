"""Sections S5 to S8: uncertainty examples, FROC curves, comparison examples, model size."""
from __future__ import annotations

import pandas as pd

from common import (BACKBONE, FISSION, METHOD_NAMES, MODEL_ORDER, PAPER_METHODS, PROPOSED, TARGETS, label, md_table, num, read_table,
                    write_section)

REGION_METHODS = ["mean_normalized_entropy", "lguq", "metaseg", "standardized_max_logit"]


def checkpoint_cell(model: str) -> str:
    return f"{label(model)} (`{model}`)"


def ids(values) -> str:
    values = [f"`{v}`" for v in values]
    return ", ".join(values) if values else "none"


def section_5() -> None:
    regions = read_table("uq_examples_regions.csv")
    keys = ["set", "example", "case"]
    summary = []
    for (group, example, case), frame in regions.groupby(keys, sort=False):
        true, false = frame[frame.true_positive], frame[~frame.true_positive]
        differing = int((false[[f"kept_{m}" for m in REGION_METHODS]].nunique(axis=1) > 1).sum())
        row = {"group": group, "example": example, "case": case, "regions": len(frame), "true": len(true), "false": len(false), "differing": differing}
        for m in REGION_METHODS:
            row[f"false_removed_{m}"] = int((~false[f"kept_{m}"]).sum())
            row[f"true_removed_{m}"] = int((~true[f"kept_{m}"]).sum())
        summary.append(row)
    table = pd.DataFrame(summary)
    true_removed = table[[f"true_removed_{m}" for m in REGION_METHODS]].sum(axis=1) > 0
    none_removed = (table["false"] > 0) & (table[[f"false_removed_{m}" for m in REGION_METHODS]].sum(axis=1) == 0)
    rows = [[f"`{r.case}`", r.group, str(r.regions), str(r.true), str(r.false), str(r.differing)]
            + [f"{getattr(r, f'false_removed_{m}')} / {getattr(r, f'true_removed_{m}')}" for m in REGION_METHODS] for r in table.itertuples()]
    parts = ["# S5. More uncertainty examples",
             f"Twelve test cases of the proposed checkpoint (`{PROPOSED}`, {label(PROPOSED)}), predicted malignant regions, with the four uncertainty methods of the paper. Six cases are in the group `agree`, where the methods make the same decision on every false region, and six are in the group `disagree`, where they differ on at least one false region. The predictions are those of the UQ run. A region is removed when its score is above the threshold fitted on the validation split. Red is malignant.",
             "## Summary per case",
             md_table(["Case", "Group", "Regions", "True", "False", "False regions with differing decisions"] + [f"{METHOD_NAMES[m]}, false removed / true removed" for m in REGION_METHODS], rows, "llrrrrrrrr"),
             "## Categories",
             md_table(["Category", "Cases"], [
                 ["The four methods make the same decision on every false region", ids(table[table.differing == 0].case)],
                 ["The methods differ on at least one false region", ids(table[table.differing > 0].case)],
                 ["At least one method removes a true region", ids(table[true_removed].case)],
                 ["Every method keeps every false region", ids(table[none_removed].case)],
             ], "ll"),
             "A category with no case is stated as none. The last category means false regions exist in the case and no method removes any of them."]
    for r in table.itertuples():
        parts += [f"## {r.group.capitalize()} {r.example}, case `{r.case}`",
                  f"![{r.group} {r.example}, {r.case}](figures/uq_examples/{r.group}_{r.example}_{r.case}.png)",
                  f"{r.regions} regions, {r.true} true and {r.false} false."]
    rows = []
    for r in regions.itertuples():
        cells = []
        for m in REGION_METHODS:
            cells.append(f"{getattr(r, f'score_{m}'):.4f} {'keep' if getattr(r, f'kept_{m}') else 'remove'}")
        rows.append([f"`{r.case}`", r.view, str(r.region_id), str(r.area), "true" if r.true_positive else "false"] + cells)
    parts += ["## Region scores and decisions",
              md_table(["Case", "View", "Region", "Area in pixels", "Type"] + [METHOD_NAMES[m] for m in REGION_METHODS], rows, "llrrlrrrr"),
              "A higher score means the region is more likely a false positive. The scores of different methods are on different scales. Source: `tables/uq_examples_regions.csv`."]
    write_section("s05_uncertainty_examples.md", parts)


def section_6() -> None:
    froc = read_table("froc_curves.csv")
    parts = ["# S6. Full FROC curves",
             "Hotspot sensitivity against false positives per case for every checkpoint. Predicted regions are removed in decreasing order of their score, and the curve is traced over 15 levels from 0.1 to 2.0 false positives per case. The dashed line removes regions in random order. UQ run, test split.",
             "## Malignant hotspots", "![FROC curves, malignant](figures/froc/froc_malignant.png)",
             "## Benign hotspots", "![FROC curves, benign](figures/froc/froc_benign.png)"]
    order = REGION_METHODS + ["random_removal"]
    for target in TARGETS:
        for level in (0.3, 0.5, 1.0):
            rows = []
            for model in MODEL_ORDER:
                cells = []
                for setting in order:
                    value = froc[(froc.target == target) & (froc.model == model) & (froc.setting == setting) & ((froc.false_positives_per_case - level).abs() < 1e-9)].hotspot_sensitivity
                    cells.append(num(value.iloc[0]))
                rows.append([checkpoint_cell(model)] + cells)
            parts += [f"## Hotspot sensitivity at {level} false positives per case, {target}",
                      md_table(["Checkpoint"] + [METHOD_NAMES[m] for m in order], rows)]
    parts.append("The values at all 15 levels are in `tables/froc_curves.csv`.")
    write_section("s06_froc_curves.md", parts)


def section_7() -> None:
    selection = read_table("comparison_examples.csv")
    dice = read_table("malignant_dice_by_image.csv")
    descriptions = {
        "easy": "The two images with the highest mean Dice over the fourteen checkpoints.",
        "hard": "Among the images where at least one checkpoint reaches a Dice of 0.5, the two with the lowest mean Dice over the fourteen checkpoints.",
        "failure": "Among the images where all fourteen checkpoints have a Dice of 0, the two with the largest malignant hotspot area.",
        "missed": f"Among the images where the proposed checkpoint (`{PROPOSED}`) has a Dice of 0 and at least seven checkpoints reach a Dice of 0.3, the two where the most checkpoints do.",
    }
    parts = ["# S7. Comparison examples of all fourteen checkpoints",
             "Each figure shows one test image next to the predictions of the fourteen checkpoints, cropped around the ground-truth malignant hotspot. Green is benign and red is malignant. The title of each panel gives the checkpoint and the malignant Dice of that image.",
             "The masks come from the standard prediction pipeline for the nnU-Net-based checkpoints, not from the UQ run, so they differ slightly from the masks of Figure 5 and of the section on uncertainty examples. For the SegFormer checkpoints the two runs are identical. The malignant Dice of an image is computed on these masks, the mean over the 203 images with a malignant hotspot equals the standard-pipeline value of each checkpoint in `tables/dice_by_model.csv`.",
             f"Of the {len(dice)} test images with a malignant hotspot, {int((dice.iloc[:, 3:].max(axis=1) == 0).sum())} are missed by all fourteen checkpoints and {int((dice[PROPOSED] == 0).sum())} by the proposed checkpoint.",
             "## Selection rules", md_table(["Category", "Rule"], [[name.capitalize(), text] for name, text in descriptions.items()], "ll"),
             "Ties are broken by the case number. The malignant Dice of every checkpoint on every one of the images is in `tables/malignant_dice_by_image.csv`, and the selected images are in `tables/comparison_examples.csv`."]
    for category in descriptions:
        parts.append(f"## {category.capitalize()}")
        for r in selection[selection.category == category].itertuples():
            parts += [f"### Case `{r.case}`, {r.view} view",
                      f"![{category} {r.example}, {r.case} {r.view}](figures/comparison/{category}_{r.example}_{r.case}_{r.view}.png)",
                      f"Ground-truth malignant area {r.truth_pixels} pixels. Mean Dice over the checkpoints {r.mean_dice:.4f}, best {r.best_dice:.4f}, checkpoints with a Dice of at least 0.3: {int(r.checkpoints_found)}."]
    write_section("s07_comparison_examples.md", parts)


def section_8() -> None:
    size = read_table("model_size.csv").set_index("model")
    rows = []
    for model in MODEL_ORDER:
        r = size.loc[model]
        rows.append([checkpoint_cell(model), num(r.parameters_million, 3), num(r.gflops, 3), num(r.median_forward_ms, 3), r.input_shape])
    parts = ["# S8. Model size and speed",
             "Parameters, floating-point operations, and forward time of the fourteen checkpoints for one forward pass at the input of the UQ run: a two-channel image of the anterior and posterior view, 1024 x 256 pixels, for the nnU-Net-based checkpoints, and a 1024 x 512 image with the two views side by side and three channels for SegFormer.",
             md_table(["Checkpoint", "Parameters (million)", "GFLOPs", "Median forward time (ms)", "Input shape"], rows, "lrrrl"),
             "FLOPs are counted with `torch.utils.flop_counter.FlopCounterMode`, which covers convolutions, matrix multiplications, and attention. Time is the median of 50 timed forward passes at batch size 1 after 10 warm-up passes, synchronized, with PyTorch 2.11.0 and CUDA 12.8 on an NVIDIA GeForce RTX 4050 Laptop GPU. The checkpoints were trained on another GPU, see S9. The SegFormer parameter counts agree with the trained checkpoints to within 0.001 million (`checkpoint_parameters_million` in `tables/model_size.csv`).",
             "Source: `tables/model_size.csv`."]
    write_section("s08_model_size_and_speed.md", parts)
