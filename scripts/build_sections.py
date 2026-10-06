"""Write the section files s01 to s14 and README.md from the CSV files in tables/ and the images in figures/.

    uv run --no-project --with pandas python scripts/build_sections.py

The tables and figures are produced by scripts/collect_sources.py and scripts/make_figures.py.
"""
from __future__ import annotations

from common import CHECKPOINTS, FISSION, MODEL_ORDER, PROPOSED, ROOT, md_table, num, read_table
from sections_examples import section_5, section_6, section_7, section_8
from sections_method import section_9, section_10, section_11, section_12, section_13, section_14
from sections_results import section_1, section_2, section_3, section_4

SECTIONS = [
    ("s01_results_all_checkpoints.md", "S1", "Results of all fourteen checkpoints: Dice under both definitions, skeleton Dice per region, hotspot detection, regions per view"),
    ("s02_paired_tests.md", "S2", "All paired tests: 91 Dice pairs, 91 McNemar pairs on matched hotspots, UQ run against standard pipeline"),
    ("s03_uncertainty_methods.md", "S3", "Seven uncertainty methods on every checkpoint, view, and class, benign results, Table IV for all checkpoints"),
    ("s04_paired_auc_tests.md", "S4", "Paired AUC tests of MetaSeg against the other methods and of the proposed checkpoint against every other checkpoint"),
    ("s05_uncertainty_examples.md", "S5", "Twelve uncertainty examples of the proposed checkpoint with region scores and decisions"),
    ("s06_froc_curves.md", "S6", "FROC curves of every checkpoint and method"),
    ("s07_comparison_examples.md", "S7", "Predictions of all fourteen checkpoints on the same test images"),
    ("s08_model_size_and_speed.md", "S8", "Parameters, FLOPs, and forward time"),
    ("s09_training_details.md", "S9", "Training settings, warm start, the collapsed first training, training curves"),
    ("s10_architecture_diagrams.md", "S10", "CBAM block and the nnU-Net and SegFormer networks"),
    ("s11_label_generation.md", "S11", "Hotspot mask algorithm, path shares, other algorithms, skeleton label sources, box cross-check"),
    ("s12_data_description.md", "S12", "Split rule and counts per split and view"),
    ("s13_prior_studies.md", "S13", "Table I extended with its evidence, and the five removed studies"),
    ("s14_statements_cut_from_paper.md", "S14", "Statements cut from the paper, restated with numbers from the metric files"),
]

TRAINERS = {
    "nnunet_single": "nnU-Net, one task, plain",
    "nnunetcbam_single": "nnU-Net, one task, CBAM",
}


def readme() -> None:
    rows = []
    for name, backbone, fission in CHECKPOINTS:
        task = "single-task" if fission == "single-task" else "multi-task"
        rows.append([f"`{name}`" + ("*" if name == PROPOSED else ""), backbone, task, "-" if fission == "single-task" else fission])
    dice = read_table("dice_by_model.csv")
    seg = read_table("seg_published.csv").set_index("model")
    config = read_table("uq_discrimination_by_config.csv")
    auc = config[config.method == "metaseg"].groupby("model").auroc.mean()
    own = config[config.method == "mean_normalized_entropy"].groupby("model").auroc.mean()
    def dice_of(model, target):
        return dice[(dice.model == model) & (dice.target == target)].iloc[0].uq_run_dice_lesion_bearing
    metrics = [[f"`{m}`" + ("*" if m == PROPOSED else ""), num(dice_of(m, "malignant")), num(dice_of(m, "benign")),
                "-" if FISSION[m] == "single-task" else num(seg.loc[m]["bone.pixel_mean.dice"]), num(own[m]), num(auc[m])] for m in MODEL_ORDER]
    parts = [
        "# Multi-Task Hotspot and Skeleton Segmentation on Whole-Body Bone Scintigraphy with Uncertainty Quantification",
        "Supplementary material for the paper of the same title. It holds what the paper cannot state: the results of all fourteen checkpoints, the statistical tests, the uncertainty methods in full, more examples, the training and label details, and the data description.",
        "## Sections",
        md_table(["File", "Section", "Content"], [[f"[{file}]({file})", code, text] for file, code, text in SECTIONS], "lll"),
        "## Rules",
        md_table(["Topic", "Rule"], [
            ["Numbers", "Every number comes from a CSV file in `tables/`. The Markdown sections are written from those files by `scripts/build_sections.py`."],
            ["Dice", "The Dice of the paper is the mean over the test images whose ground truth contains the class (203 malignant, 473 benign), computed on the predictions of the UQ run, one full-image forward pass per view. Each table states the definition it uses. S1 explains the second definition and the standard-pipeline run."],
            ["Checkpoint names", "The names in the table below are used in every table and in the CSV files. For nnU-Net and nnU-Net with CBAM, `multihead` is Late fission and `multidecoder` is Early fission. The SegFormer run folders `dual_decoder`, `dual_fuse`, and `dual_head` are Early, Mid, and Late fission."],
            ["Methods", "Predictive entropy, local gradient UQ, MetaSeg, and standardized max logit are the methods of the paper. Max-softmax, Mahalanobis distance, and inverse area (a control) appear only in S3 and S4."],
            ["Colors", "Benign hotspots are green (30, 160, 60) and malignant hotspots are red (215, 25, 25) in the images."],
            ["Scope", "Nothing is trained or re-run to write these sections. External classification and saliency analyses are not part of them."],
        ], "ll"),
        "## Checkpoints",
        md_table(["Checkpoint", "Backbone", "Training", "Fission point"], rows, "llll"),
        "\\* The proposed method: nnU-Net with CBAM at Early fission, with MetaSeg filtering.",
        "## Metrics",
        md_table(["Checkpoint", "Malignant Dice", "Benign Dice", "Skeleton Dice", "Region AUC, predictive entropy", "Region AUC, MetaSeg"], metrics),
        "Dice is the mean over the test images whose ground truth contains the class (203 malignant, 473 benign), on the UQ run. Skeleton Dice is the mean over the twelve regions on the standard-pipeline run. Region AUC separates true from false predicted regions, as the mean over the two views and the two classes. Predictive entropy is computed from the softmax output of the model itself, MetaSeg is a trained meta-classifier on region features. \\* The proposed method. All other metrics are in the sections above.",
        "![Malignant Dice and MetaSeg region AUC of the fourteen checkpoints](figures/summary_dice_and_auc.png)",
        "## Code",
        "The training and inference code is in two repositories.",
        md_table(["Repository", "Content"], [
            ["[nnunetv2-multitask](https://github.com/Liamours/nnunetv2-multitask)", "Fork of nnU-Net v2 for multi-task segmentation"],
            ["[segformer-multitask](https://github.com/Liamours/segformer-multitask)", "Multi-task SegFormer"],
        ], "ll"),
        "The `code/` folder here is reserved for the evaluation and uncertainty scripts.",
        "## Figures of the paper",
        "![Skeleton and hotspot mask generation](figures/skeleton_and_hotspot_mask_generation.png)",
        "![Multi-task nnU-Net with CBAM and MetaSeg filtering](figures/multitask_nnunet_cbam_metaseg_pipeline.png)",
        "![Test case with skeleton and hotspot masks](figures/test_case_scan_skeleton_hotspot_masks.png)",
        "![Decoder fission points](figures/decoder_fission_points.png)",
        "![Filtered predictions by uncertainty method](figures/filtered_predictions_by_uq_method.png)",
        "## Regenerate",
        "The sections are rebuilt from `tables/` and `figures/` alone. The two collection steps read the saved results of the project and need the project folder.",
        md_table(["Output", "Command"], [
            ["Section files and this README", "`uv run --no-project --with pandas python scripts/build_sections.py`"],
            ["`tables/` and the copied figures", "`uv run --no-project --with pandas --with tqdm python scripts/collect_sources.py --project <project folder>`"],
            ["Figures of S5, S7, S9, S11", "`uv run --no-project --with pandas --with numpy --with pillow --with matplotlib --with tqdm python scripts/make_figures.py all --project <project folder>`"],
        ], "ll"),
        "The metric files in `tables/` were computed from the saved test predictions and uncertainty records by the scripts of the project. The FROC plots of S6, the training progress plots of S9, and the diagrams of S10 are copied from the project, not redrawn here.",
    ]
    (ROOT / "README.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    for build in (section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8, section_9, section_10, section_11, section_12, section_13, section_14, readme):
        build()
        print(build.__name__)


if __name__ == "__main__":
    main()
