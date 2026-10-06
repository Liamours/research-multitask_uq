"""Sections S1 to S4: results, paired tests, uncertainty methods, paired AUC tests."""
from __future__ import annotations

import pandas as pd

from common import (ALL_METHODS, BACKBONE, BONE_REGIONS, DICE_UQ_RUN, FISSION, METHOD_NAMES, MODEL_ORDER, MULTITASK, PAPER_METHODS,
                    PROPOSED, TARGETS, interval, label, md_table, num, pval, read_table, write_section)

DEFINITIONS = md_table(
    ["Term", "Meaning"],
    [
        ["Lesion-bearing Dice", "Mean Dice over the test images whose ground truth contains the class: 203 images for malignant, 473 for benign. The Dice of the paper."],
        ["Published-definition Dice", "Mean Dice over every image where Dice is defined. An image without the class in the ground truth but with a predicted region scores 0, so false predictions lower this value."],
        ["UQ run", "Predictions behind the uncertainty records: one full-image forward pass per view. Every table in these sections uses it unless a column says otherwise."],
        ["Standard-pipeline run", "Predictions of the standard nnU-Net prediction pipeline (`nnUNetv2_predict`, sliding window). For SegFormer it is the same run as the UQ run. Columns of the CSV files named `published_run` hold it."],
        ["Region", "An 8-connected component of the predicted class. A true region overlaps a ground-truth hotspot of its class, a false region overlaps none."],
        ["Matched hotspot", "A ground-truth hotspot matched one to one with a predicted region. Hotspot sensitivity is the share of ground-truth hotspots matched."],
        ["False positives per case", "Predicted regions not matched to a ground-truth hotspot, over both views, divided by the 293 test cases."],
    ],
    "ll",
)


def checkpoint_cell(model: str) -> str:
    return f"{label(model)} (`{model}`)"


def detection_counts() -> dict[tuple[str, str], tuple[int, int]]:
    pairs = read_table("stats_lesion_detection_model_pairs.csv")
    counts: dict[tuple[str, str], tuple[int, int]] = {}
    for row in pairs.itertuples():
        counts[(row.model_a, row.target)] = (int(row.detected_a), int(row.lesions))
        counts[(row.model_b, row.target)] = (int(row.detected_b), int(row.lesions))
    return counts


def section_1() -> None:
    dice = read_table("dice_by_model.csv").set_index(["model", "target"])
    seg = read_table("seg_published.csv").set_index("model")
    filtering = read_table("filtering_effects.csv")
    config = read_table("uq_discrimination_by_config.csv")
    detected = detection_counts()
    parts = ["# S1. Results of all fourteen checkpoints",
             "Every checkpoint was evaluated on the 293 test cases (586 images, anterior and posterior). The checkpoint names are listed in the README.",
             DEFINITIONS]
    for target in TARGETS:
        rows = []
        for model in MODEL_ORDER:
            row = dice.loc[(model, target)]
            rows.append([checkpoint_cell(model), num(row.uq_run_dice_lesion_bearing), num(row.published_run_dice_lesion_bearing),
                         num(row.uq_run_dice_published_definition), num(row.published_run_dice_published_definition)])
        parts += [f"## {target.capitalize()} Dice",
                  md_table(["Checkpoint", "Lesion-bearing, UQ run", "Lesion-bearing, standard-pipeline run", "Published definition, UQ run", "Published definition, standard-pipeline run"], rows),
                  "Source: `tables/dice_by_model.csv`. The number of images behind each cell is in the same file."]
    rows = []
    for model in MULTITASK:
        row = seg.loc[model]
        rows.append([label(model), num(row["bone.pixel_mean.dice"])] + [num(row[f"bone.by_label.label_{index}.dice"]) for index in range(1, 13)])
    parts += ["## Skeleton Dice",
              md_table(["Checkpoint", "Mean"] + BONE_REGIONS, rows),
              "Skeleton Dice of the standard-pipeline evaluation on the 293 test cases: the mean over the twelve regions and the Dice of each region. The single-task checkpoints have no skeleton output. Sternum has no ground-truth pixels in the posterior view of any test case. Source: `tables/seg_published.csv`."]
    for target in TARGETS:
        rows = []
        for model in MODEL_ORDER:
            row = filtering[(filtering.model == model) & (filtering.target == target) & (filtering.setting == "no_uq")].iloc[0]
            matched, total = detected[(model, target)]
            rows.append([checkpoint_cell(model), str(total), str(matched), num(row.lesion_sensitivity), str(int(row.false_regions)), num(row.region_precision), num(row.fp_per_case, 2)])
        parts += [f"## {target.capitalize()} hotspot detection before filtering",
                  md_table(["Checkpoint", "Hotspots", "Matched", "Hotspot sensitivity", "False regions", "Region precision", "False positives per case"], rows),
                  "UQ run, all predicted regions kept. Source: `tables/filtering_effects.csv` (setting `no_uq`) and `tables/stats_lesion_detection_model_pairs.csv`."]
    for target in TARGETS:
        subset = config[(config.target == target) & (config.method == "metaseg")]
        rows = []
        for model in MODEL_ORDER:
            cells, totals = [], [0, 0, 0]
            for view in ("anterior", "posterior"):
                row = subset[(subset.model == model) & (subset.view == view)].iloc[0]
                values = [int(row.regions), int(row.true_regions), int(row.false_regions)]
                totals = [a + b for a, b in zip(totals, values)]
                cells += [str(v) for v in values]
            rows.append([checkpoint_cell(model)] + cells + [str(v) for v in totals] + [num(totals[2] / 293, 2)])
        parts += [f"## {target.capitalize()} regions per view",
                  md_table(["Checkpoint", "Anterior regions", "true", "false", "Posterior regions", "true", "false", "Pooled regions", "true", "false", "False regions per case"], rows),
                  "UQ run, before filtering. False regions per case is the number of false regions over both views divided by 293. Source: `tables/uq_discrimination_by_config.csv`."]
    write_section("s01_results_all_checkpoints.md", parts)


def pair_rows(frame: pd.DataFrame) -> list[list[str]]:
    rank = {name: index for index, name in enumerate(MODEL_ORDER)}
    frame = frame.assign(a=frame.model_a.map(rank), b=frame.model_b.map(rank)).sort_values(["a", "b"])
    return [[f"`{r.model_a}`", f"`{r.model_b}`", str(int(r.units)), num(r.mean_dice_a), num(r.mean_dice_b), num(r.mean_difference, 4, True),
             interval(r.ci_low, r.ci_high), f"{int(r.units_a_higher)} / {int(r.units_b_higher)}", pval(r.wilcoxon_p), pval(r.holm_p), pval(r.ttest_p), pval(r.ttest_holm_p)]
            for r in frame.itertuples()]


def significant(frame: pd.DataFrame, column: str) -> int:
    return int((frame[column] < 0.05).sum())


def section_2() -> None:
    uq_pairs = read_table("stats_dice_model_pairs.csv")
    std_pairs = read_table("stats_dice_model_pairs_published_run.csv")
    detection = read_table("stats_lesion_detection_model_pairs.csv")
    dice = read_table("dice_by_model.csv")
    parts = ["# S2. All paired tests",
             "Ninety-one pairs of the fourteen checkpoints, for the malignant and the benign class.",
             md_table(["Comparison", "Test", "Interval"], [
                 ["Dice of two checkpoints", "Wilcoxon signed-rank test on the per-image Dice differences of the images with the class in the ground truth, and a paired t-test. Holm correction over the 91 pairs", "Mean difference with a 95% percentile interval from 2000 bootstrap resamples of the 293 test cases, both views of a case kept together"],
                 ["Matched hotspots of two checkpoints", "Exact McNemar test on the hotspots matched by one checkpoint and not the other. Holm correction over the 91 pairs", "-"],
             ], "lll"),
             "Dice in the pair tables is the lesion-bearing Dice of the UQ run unless the heading says standard-pipeline run. " + DICE_UQ_RUN]
    for target in TARGETS:
        subset = uq_pairs[uq_pairs.target == target]
        parts += [f"## Dice pairs, {target}",
                  md_table(["Model A", "Model B", "Images", "Dice A", "Dice B", "Difference A minus B", "95% interval", "A higher / B higher", "Wilcoxon p", "Holm p", "t-test p", "t-test Holm p"], pair_rows(subset), "llrrrrrrrrrr"),
                  f"After Holm correction {significant(subset, 'holm_p')} of 91 pairs are significant under the Wilcoxon test and {significant(subset, 'ttest_holm_p')} under the t-test (p below 0.05)."]
    for target in TARGETS:
        subset = std_pairs[std_pairs.target == target]
        parts.append(f"Standard-pipeline run, {target}: {significant(subset, 'holm_p')} of 91 pairs are significant after Holm correction under the Wilcoxon test and {significant(subset, 'ttest_holm_p')} under the t-test. The full table is `tables/stats_dice_model_pairs_published_run.csv`.")
    for target in TARGETS:
        subset = detection[detection.target == target]
        rank = {name: index for index, name in enumerate(MODEL_ORDER)}
        subset = subset.assign(a=subset.model_a.map(rank), b=subset.model_b.map(rank)).sort_values(["a", "b"])
        rows = [[f"`{r.model_a}`", f"`{r.model_b}`", str(int(r.lesions)), str(int(r.detected_a)), str(int(r.detected_b)), str(int(r.only_a)), str(int(r.only_b)), pval(r.mcnemar_p), pval(r.holm_p)] for r in subset.itertuples()]
        parts += [f"## Matched hotspots, {target}",
                  md_table(["Model A", "Model B", "Hotspots", "Matched by A", "Matched by B", "Only A", "Only B", "McNemar p", "Holm p"], rows, "llrrrrrrr"),
                  f"{significant(subset, 'holm_p')} of 91 pairs are significant after Holm correction. The test treats the {int(subset.lesions.iloc[0])} hotspots as independent, although hotspots of one case are correlated. UQ run."]
    rows = []
    for model in MODEL_ORDER:
        entry = {target: dice[(dice.model == model) & (dice.target == target)].iloc[0] for target in TARGETS}
        rows.append([checkpoint_cell(model)] + [num(entry[t].uq_run_dice_lesion_bearing - entry[t].published_run_dice_lesion_bearing, 4, True) for t in TARGETS])
    parts += ["## Dice of the UQ run against the standard-pipeline run",
              md_table(["Checkpoint", "Malignant, UQ run minus standard-pipeline run", "Benign, UQ run minus standard-pipeline run"], rows),
              "Lesion-bearing Dice. The two runs are identical for the SegFormer checkpoints. For the nnU-Net-based checkpoints the standard pipeline crops each image, normalizes the crop, and slides a window, while the UQ run reads the full image in one pass. Source: `tables/dice_by_model.csv`."]
    write_section("s02_paired_tests.md", parts)


def method_table(frame: pd.DataFrame, column: str, target: str, digits: int = 4) -> str:
    rows = []
    for model in MODEL_ORDER:
        cells = []
        for method in ALL_METHODS:
            value = frame[(frame.model == model) & (frame.target == target) & (frame.method == method)].iloc[0][column]
            cells.append(num(value, digits))
        rows.append([checkpoint_cell(model)] + cells)
    return md_table(["Checkpoint"] + [METHOD_NAMES[m] for m in ALL_METHODS], rows)


def section_3() -> None:
    by_model = read_table("uq_discrimination_by_model.csv")
    by_config = read_table("uq_discrimination_by_config.csv")
    filtering = read_table("filtering_effects.csv")
    parts = ["# S3. Uncertainty methods in full",
             "Seven region scores are computed for every predicted region of the checkpoints. A higher score means the region is more likely a false positive.",
             md_table(["Method", "Region score"], [
                 ["Max-softmax", "One minus the mean maximum softmax probability of the region"],
                 ["Predictive entropy", "Mean normalized Shannon entropy of the softmax output over the region"],
                 ["Local gradient UQ", "Norm of the gradient of the region's predicted probability with respect to decoder activations"],
                 ["MetaSeg", "Output of a meta-classifier on region features such as area, entropy, and logit spread"],
                 ["Standardized max logit", "Mean maximum logit of the region, standardized by its predicted class"],
                 ["Mahalanobis distance", "Distance of the mean decoder features of the region to the nearest class centroid"],
                 ["Inverse area", "One over the region area, a control without model confidence"],
             ], "ll"),
             "The paper reports the first four methods. Max-softmax, Mahalanobis distance, and inverse area appear only here. All values are computed on the test split from the UQ run. Region AUC is the probability that a false region scores higher than a true region."]
    for target in TARGETS:
        rows = []
        for model in MODEL_ORDER:
            cells = []
            for method in ALL_METHODS:
                r = by_model[(by_model.model == model) & (by_model.target == target) & (by_model.method == method)].iloc[0]
                cells.append(f"{r.pooled_auroc:.4f} [{r.pooled_ci_low:.4f}, {r.pooled_ci_high:.4f}]")
            rows.append([checkpoint_cell(model)] + cells)
        parts += [f"## Pooled region AUC with 95% interval, {target}",
                  md_table(["Checkpoint"] + [METHOD_NAMES[m] for m in ALL_METHODS], rows),
                  "Pooled over both views. The interval is the 95% bootstrap interval. Source: `tables/uq_discrimination_by_model.csv`."]
    for column, title, note in (("mean_auroc", "Mean region AUC over the two views", "Higher is better."),
                                ("mean_fpr_at_95_tpr", "Mean false-positive rate at 95% true-positive rate", "Share of false regions still kept when 95% of the true regions are kept. Lower is better."),
                                ("mean_ap_false_positive", "Mean average precision for false regions", "Average precision of ranking false regions above true regions. Higher is better.")):
        for target in TARGETS:
            parts += [f"## {title}, {target}", method_table(by_model, column, target), f"{note} Source: `tables/uq_discrimination_by_model.csv`."]
    for target in TARGETS:
        rows = []
        for model in MODEL_ORDER:
            for view in ("anterior", "posterior"):
                cells = []
                for method in ALL_METHODS:
                    r = by_config[(by_config.model == model) & (by_config.target == target) & (by_config.view == view) & (by_config.method == method)].iloc[0]
                    cells.append(num(r.auroc))
                rows.append([checkpoint_cell(model), view] + cells)
        parts += [f"## Region AUC per view, {target}", md_table(["Checkpoint", "View"] + [METHOD_NAMES[m] for m in ALL_METHODS], rows, "llrrrrrrr"),
                  "Source: `tables/uq_discrimination_by_config.csv`, which also holds the false-positive rate, average precision, and region counts per view."]
    parts.append("## Filtering at the threshold of the validation split")
    parts.append("A region is removed when its score is above the 95th percentile of the true-region scores of the validation split, fitted for each method, view, and class. Region sensitivity is the share of true regions kept. Region specificity is the share of false regions removed. FROC sensitivity is the hotspot sensitivity at 0.5 false positives per case when regions are removed in decreasing order of score, and the last column is the same with random order.")
    for target in TARGETS:
        subset = filtering[filtering.target == target]
        rows_sens, rows_spec, rows_froc = [], [], []
        for model in MODEL_ORDER:
            base = subset[(subset.model == model) & (subset.setting == "no_uq")].iloc[0].false_regions
            def pick(setting):
                return subset[(subset.model == model) & (subset.setting == setting)].iloc[0]
            rows_sens.append([checkpoint_cell(model)] + [num(pick(m).true_regions_kept) for m in ALL_METHODS])
            rows_spec.append([checkpoint_cell(model)] + [num(1 - pick(m).false_regions / base) for m in ALL_METHODS])
            rows_froc.append([checkpoint_cell(model)] + [num(pick(m)["sensitivity_at_fp_0.5"]) for m in ALL_METHODS] + [num(pick("random_removal")["sensitivity_at_fp_0.5"])])
        head = ["Checkpoint"] + [METHOD_NAMES[m] for m in ALL_METHODS]
        parts += [f"### Region sensitivity, {target}", md_table(head, rows_sens),
                  f"### Region specificity, {target}", md_table(head, rows_spec),
                  f"### FROC sensitivity at 0.5 false positives per case, {target}", md_table(head + ["Random removal"], rows_froc),
                  "Source: `tables/filtering_effects.csv`. Region specificity is one minus the false regions left after filtering over the false regions before."]
    write_section("s03_uncertainty_methods.md", parts)


def section_4() -> None:
    methods = read_table("stats_auroc_method_pairs.csv")
    models = read_table("stats_auroc_model_pairs.csv")
    rank = {name: index for index, name in enumerate(MODEL_ORDER)}
    order = {m: i for i, m in enumerate(ALL_METHODS)}
    parts = ["# S4. Paired AUC tests for all fourteen checkpoints",
             "Region AUC differences are tested with a paired bootstrap over the 293 test cases: the same resampled cases for every method and checkpoint, a 95% percentile interval of the difference, and p from the share of resamples with a difference on each side of zero. Region AUC is pooled over both views.",
             "## MetaSeg against each other method"]
    for target in TARGETS:
        subset = methods[methods.target == target]
        subset = subset.assign(a=subset.model.map(rank), b=subset.method_b.map(order)).sort_values(["a", "b"])
        rows = [[checkpoint_cell(r.model), METHOD_NAMES[r.method_b], num(r.auroc_a), num(r.auroc_b), num(r.difference, 4, True), interval(r.ci_low, r.ci_high), pval(r.bootstrap_p)] for r in subset.itertuples()]
        parts += [f"### {target.capitalize()}", md_table(["Checkpoint", "Method B", "MetaSeg AUC", "AUC of B", "Difference", "95% interval", "p"], rows, "llrrrrr"),
                  f"{int((subset.bootstrap_p < 0.05).sum())} of {len(subset)} comparisons have p below 0.05 (no correction for multiple comparisons)."]
    parts.append(f"## {label(PROPOSED)} against every other checkpoint")
    for target in TARGETS:
        subset = models[models.target == target]
        subset = subset.assign(b=subset.model_b.map(rank)).sort_values("b")
        rows = [[checkpoint_cell(r.model_b), METHOD_NAMES.get(r.method, r.method), num(r.auroc_a), num(r.auroc_b), num(r.difference, 4, True), interval(r.ci_low, r.ci_high), pval(r.bootstrap_p)] for r in subset.itertuples()]
        parts += [f"### {target.capitalize()}", md_table(["Other checkpoint", "Method", "AUC of the proposed checkpoint", "AUC of the other", "Difference", "95% interval", "p"], rows, "llrrrrr"),
                  f"The smallest p is {pval(subset.bootstrap_p.min())}. No correction for multiple comparisons."]
    write_section("s04_paired_auc_tests.md", parts)
