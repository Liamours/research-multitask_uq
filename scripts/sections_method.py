"""Sections S9 to S14: training, architectures, labels, data, prior studies, statements cut from the paper."""
from __future__ import annotations

import re
import statistics

import pandas as pd

from common import (BACKBONE, BONE_REGIONS, FISSION, METHOD_NAMES, MODEL_ORDER, PAPER_METHODS, PROPOSED, TARGETS, interval, label, md_table, num, pval,
                    read_table, write_section)


def checkpoint_cell(model: str) -> str:
    return f"{label(model)} (`{model}`)"


def run_date(log: str) -> str:
    year, month, day = re.search(r"training_log_(\d+)_(\d+)_(\d+)_", log).groups()
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def section_9() -> None:
    nn = read_table("training_nnunet.csv")
    sf = read_table("training_segformer.csv")
    versions = read_table("software_versions.csv")
    constants = ["batch_size", "patch_size", "stages", "features_per_stage", "epochs", "initial_lr", "weight_decay", "momentum", "foreground_oversampling", "gpu", "torch"]
    assert all(nn[c].nunique() == 1 for c in constants), "settings differ between nnU-Net checkpoints"
    first = nn.iloc[0]
    rows = [[f"`{r.checkpoint}`", label(r.checkpoint), f"`{r.trainer}`", f"`{r.plans}`", r.network_class, "yes" if r.cbam else "no", "single-task CBAM weights" if "WarmStart" in r.trainer else "random",
             "-" if r.loss_weights == "1.0" else r.loss_weights, run_date(r.training_log)] for r in nn.itertuples()]
    sf_rows = [[f"`{r.checkpoint}`", label(r.checkpoint), r.run, r.task_mode, r.pretrained, "-" if r.task_weights == "1.0/1.0" else r.task_weights, r.checkpoint_metric] for r in sf.itertuples()]
    sf0 = sf.iloc[0]
    parts = ["# S9. Training details",
             "One training run per configuration. The case split and the labels are described in S11 and S12.",
             "## Software and hardware", md_table(["Item", "Version", "Recorded in"], [[r.software, r.version, r.source] for r in versions.itertuples()], "lll"),
             "The nnU-Net run files do not record a training seed. The SegFormer runs use seed 42, the same seed as the case split. The GPU is not recorded in the SegFormer run files.",
             "## nnU-Net and nnU-Net with CBAM, settings shared by the ten checkpoints",
             md_table(["Setting", "Value"], [
                 ["Input", f"two channels, the anterior and the posterior view, patch size {first.patch_size} pixels"],
                 ["Batch size", str(first.batch_size)],
                 ["Network", f"{first.stages} stages, features per stage {first.features_per_stage}"],
                 ["Optimizer", f"SGD with Nesterov momentum {first.momentum}, weight decay {first.weight_decay}"],
                 ["Learning rate", f"{first.initial_lr}, polynomial decay"],
                 ["Epochs", str(first.epochs)],
                 ["Foreground oversampling", str(first.foreground_oversampling)],
                 ["Loss", "Dice and cross-entropy per task with deep supervision, tasks summed with the weights below"],
                 ["Fold", "0 (one run, the case split of S12)"],
             ], "ll"),
             "## nnU-Net and nnU-Net with CBAM, settings that differ",
             md_table(["Checkpoint", "Backbone and fission", "Trainer", "Plans", "Network class", "CBAM", "Initialization", "Task weights, hotspot / skeleton", "Training log date"], rows, "lllllllll"),
             "The single-task checkpoints are one-task instances of the same network class. Source: `tables/training_nnunet.csv`.",
             "## SegFormer", md_table(["Setting", "Value"], [
                 ["Backbone", f"{sf0.backbone}, initialized from `{sf0.pretrained}`, MLP decoder dimension {sf0.decoder_dim}"],
                 ["Input", f"{sf0.image_size} pixels, the two views side by side, batch size {sf0.batch_size}"],
                 ["Optimizer", f"{sf0.optimizer}, learning rate {sf0.lr_backbone} for the backbone and {sf0.lr_head} for the head, weight decay {sf0.weight_decay}"],
                 ["Schedule", f"{sf0.scheduler} decay with {sf0.warmup_iters} warm-up iterations"],
                 ["Loss", f"Dice and cross-entropy, weights {sf0.loss_dice_weight} and {sf0.loss_ce_weight}, tasks summed with the weights in the table below"],
                 ["Epochs", str(sf0.epochs)],
                 ["Precision", f"{sf0.amp} mixed precision"],
                 ["Seed", str(sf0.seed)],
             ], "ll"),
             md_table(["Checkpoint", "Backbone and fission", "Run folder", "Task mode", "Initialization", "Task weights, hotspot / skeleton", "Checkpoint metric"], sf_rows, "lllllll"),
             "Source: `tables/training_segformer.csv`.",
             "## Warm start of the multi-task CBAM checkpoints",
             "The four multi-task nnU-Net with CBAM checkpoints (Early, Early-Mid, Mid, and Late) are not trained from random weights. Each starts from the weights of the single-task nnU-Net with CBAM checkpoint. The shared encoder, the shared decoder stages, the decoder stages of the lesion task, and the lesion output head take the single-task values, and the decoder stages of the skeleton task and the skeleton output head keep their random initialization.",
             "The weights are matched by name and shape. For the Early fission checkpoint, the single-task decoder has the same shape as the lesion decoder of the two-decoder network, so the names differ only by the prefix `decoder.` against `decoders.lesion.`. The trainers check at run time that every key left out belongs to the skeleton branch and stop the run if any other key is missing or has another shape, so a partial transfer cannot pass unnoticed. The nnU-Net option `-pretrained_weights` is not used because it requires every key of the target network in the source checkpoint, which the skeleton branch cannot satisfy.",
             "The plain nnU-Net multi-task checkpoints and the single-task checkpoints are trained from random weights.",
             "## First training of the Early fission CBAM model",
             "The first multi-task CBAM run with the Early fission network, trained from random weights, collapsed. It predicted almost no malignant regions, and every number computed from its predictions was degenerate. That checkpoint is not the checkpoint of the paper.",
             "The cause was examined on the Late fission network with three instrumented 5-epoch runs. The collapse is a smooth and fast slide of the lesion output into predicting background everywhere, complete within about 140 training steps, inside the first epoch. The gradient of the lesion head does not vanish. It shrinks as the prediction saturates, the usual behavior of softmax gradients near an extreme. The pressure comes from the class imbalance between lesion and background pixels, so another random initialization is pushed in the same direction. The single-task CBAM network, trained with the same normalization fix on the same lesion data, left this state by about epoch 89 in two runs.",
             "An earlier retrain of the Early fission run, trained under another plan name, is reported in the notes of the code with an anterior malignant Dice rising from 0.2245 to 0.5990 and the predicted malignant regions from 0 to 355 against 353 in the ground truth. It is not the checkpoint of the paper either.",
             f"The checkpoint of the paper (`{PROPOSED}`) was trained with the warm start from the single-task CBAM weights, trainer `nnUNetTrainerMultiTaskDualDecoderCBAMWarmStart_100epochs`, on {run_date(nn[nn.checkpoint == PROPOSED].iloc[0].training_log)}. The Early-Mid, Mid, and Late multi-task CBAM checkpoints use the same fix.",
             "## Training curves", "### SegFormer", "![SegFormer validation Dice](figures/training_curves/segformer_validation_dice.png)",
             "Validation foreground mean Dice per epoch. For the multi-task checkpoints it is the Dice of the lesion task. Source: `tables/curve_segformer_*.csv`.",
             "### nnU-Net and nnU-Net with CBAM"]
    for r in nn.itertuples():
        parts += [f"#### {label(r.checkpoint)} (`{r.checkpoint}`)", f"![Training progress of {r.checkpoint}](figures/training_curves/{r.checkpoint}_progress.png)"]
    parts.append("The plots are written by nnU-Net during training: losses, the pseudo Dice on the validation cases, the epoch time, and the learning rate.")
    write_section("s09_training_details.md", parts)


def section_10() -> None:
    parts = ["# S10. Architecture diagrams",
             "## CBAM block", "![CBAM block](figures/architecture/cbam_block_detail.png)",
             "The input feature map passes through channel attention, is multiplied by the channel attention weights, passes through spatial attention, and is multiplied by the spatial attention weights. The result is the refined feature map. The block is used after every encoder stage, every decoder stage, and the bottleneck of the nnU-Net with CBAM checkpoints, with a reduction of 16 and a spatial kernel of 7.",
             "## nnU-Net", "![nnU-Net](figures/architecture/nnunet_plain_models.png)",
             "(a) The single-task network with one decoder. (b) The multi-task network with a shared encoder and a shared decoder that splits into a lesion head and a skeleton head, Late fission. (c) The multi-task network with a shared encoder and one decoder for each task, Early fission. The Early-Mid and Mid networks are drawn in Figure 4 of the paper (`figures/decoder_fission_points.png`).",
             "## nnU-Net with CBAM", "![nnU-Net with CBAM](figures/architecture/nnunet_cbam_models.png)",
             "The same three networks with a CBAM block after every encoder and decoder stage.",
             "## SegFormer", "![SegFormer](figures/architecture/segformer_models.png)",
             "(a) The single-task network: a patch embedding, four transformer stages T1 to T4 as the encoder, and an MLP decoder that takes the outputs of the four stages. (b) The multi-task network with a shared MLP decoder and two output heads, Late fission. (c) The multi-task network with one MLP decoder for each task, Early fission. The Mid network, in which the two tasks share only the projection stage of the decoder, is not drawn."]
    write_section("s10_architecture_diagrams.md", parts)


def section_11() -> None:
    paths = read_table("hotspot_mask_paths.csv").set_index("path")
    examples = read_table("hotspot_mask_examples.csv").set_index("path")
    algorithms = read_table("hotspot_algorithms.csv")
    pseudo = read_table("skeleton_pseudo_label_model.csv").set_index("setting").value
    sources = read_table("skeleton_label_sources_bs80k.csv").set_index("source").views
    counts = read_table("split_counts.csv")
    both = counts[counts.view == "both"]
    manual, auto = int(both.skeleton_manual.sum()), int(both.skeleton_pseudo.sum())
    crosscheck = read_table("skeleton_box_crosscheck.csv")
    percentile, otsu = paths.loc["smooth_percentile_fallback"], paths.loc["otsu_morph_k7"]
    total_boxes = int(paths.boxes.sum())
    algo_names = {"otsu_morphology-guarded_smooth": "Otsu with morphology and guarded smooth fallback (used)", "random_walker_seeded": "Random walker with seeds", "grabcut_seeded_context": "GrabCut with seeds and context", "full_bbox": "Full box"}
    rows = []
    for r in algorithms.itertuples():
        rows.append([algo_names.get(r.algorithm_method_name, r.algorithm_method_name), "yes" if r.can_escape_bounding_box else "no", f"{int(r.total_bounding_boxes_checked):,}",
                     num(r.total_segment_per_bounding_box_mean, 4), str(int(r.total_segment_per_bounding_box_max))])
    rows.append([algo_names["full_bbox"], "no", "-", "-", "-"])
    cross_rows = [[r.region, str(int(r.n)), num(r.mean_iou), num(r.median_iou), num(r.mean_containment_in_template), num(r.mean_containment_in_segmentation), "yes" if r.full_containment_expected else "no"] for r in crosscheck.itertuples()]
    parts = ["# S11. Label generation in detail",
             "## Hotspot masks",
             "BS-80K provides one bounding box for each hotspot, marked normal or abnormal. The two classes are the benign class (normal) and the malignant class (abnormal). Inside each box the mask is made in the six steps below, with the settings of the table.",
             "1. Crop the box from the scan.",
             "2. Threshold the box with Otsu's method.",
             "3. Close the mask with an elliptical kernel, then open it.",
             "4. Check the mask. It fails the check when it is empty, covers more than 85% of the box, or when more than 65% of the pixels on the border of the box are in the mask.",
             "5. For a mask that fails, replace it with the percentile mask: smooth the box with a Gaussian filter, keep the pixels at or above the 75th percentile, keep the largest connected region, fill its holes, and close it with a 3 x 3 kernel.",
             "6. If the mask is still empty, draw an ellipse at the brightest pixel of the box.",
             md_table(["Setting", "Value"], [["Kernel", "elliptical, 7 x 7 pixels"], ["Closing", "2 iterations"], ["Opening", "1 iteration"], ["Maximum coverage of the box", "0.85"],
                                             ["Maximum border contact", "0.65"], ["Percentile of the smoothed box", "75"], ["Gaussian smoothing sigma", "1.5 pixels"]], "ll"),
             "## Share of boxes on each path",
             md_table(["Path", "Boxes", "Share of the boxes", "Median box area in pixels"], [
                 ["Otsu path, mask passes the check (steps 1 to 4)", f"{int(otsu.boxes):,}", f"{otsu.share * 100:.1f}%", f"{otsu.median_box_area_pixels:.0f}"],
                 ["Percentile path, mask replaced (step 5)", f"{int(percentile.boxes):,}", f"{percentile.share * 100:.1f}%", f"{percentile.median_box_area_pixels:.0f}"],
             ], "lrrr"),
             f"All {total_boxes:,} boxes end on one of the two paths, so step 6 is not reached. The Otsu path covers the larger boxes. Source: `tables/hotspot_mask_paths.csv`.",
             "## Example of each path", "![Steps of the hotspot mask algorithm](figures/hotspot_steps/hotspot_mask_steps.png)",
             f"Otsu path: case `{examples.loc['otsu'].case}`, {examples.loc['otsu'].view} view. Percentile path: case `{examples.loc['percentile'].case}`, {examples.loc['percentile'].view} view. Each column is the image after the step named above it. The Otsu path does not use the percentile step. Source: `tables/hotspot_mask_examples.csv`.",
             "## The other algorithms tried",
             md_table(["Algorithm", "Can leave the box", "Boxes checked", "Segments per box, mean", "Segments per box, maximum"], rows, "lrrrr"),
             f"Each algorithm turns a bounding box into a mask. GrabCut is the only one that can place pixels outside the box, and in some boxes it returns up to three segments. The full box uses the whole box as the mask. Source: `tables/hotspot_algorithms.csv`.",
             "## Skeleton labels",
             f"The skeleton mask has twelve regions and background: {', '.join(r.lower() for r in BONE_REGIONS)}. Part of the views were annotated manually. For the other views the mask is the prediction of an nnU-Net trained on the manual masks.",
             md_table(["Set", "Manual", "Predicted", "Manual share"], [
                 ["All of BS-80K, views", f"{int(sources['manual']):,}", f"{int(sources['pseudo']):,}", f"{sources['manual'] / (sources['manual'] + sources['pseudo']) * 100:.1f}%"],
                 ["The 2,925 cases used, views", f"{manual:,}", f"{auto:,}", f"{manual / (manual + auto) * 100:.1f}%"],
             ], "lrrr"),
             "The counts of the cases used are the sum over the three splits in `tables/split_counts.csv`, the counts of BS-80K are from the label list of the merged skeleton masks (`tables/skeleton_label_sources_bs80k.csv`).",
             md_table(["Setting of the predicting nnU-Net", "Value"], [
                 ["Configuration", pseudo["configuration"]], ["Classes", f"{pseudo['classes']} (background and twelve regions)"], ["Views used for training", f"{int(pseudo['training_views']):,}"],
                 ["Patch size", pseudo["patch_size"]], ["Batch size", pseudo["batch_size"]], ["Normalization", pseudo["normalization"]], ["Views predicted", f"{int(pseudo['predicted_views']):,}"],
             ], "ll"),
             "The settings are read from the plans saved with the predictions. Source: `tables/skeleton_pseudo_label_model.csv`.",
             "## Cross-check of the skeleton masks against the bone boxes",
             "The bone-region boxes of BS-80K (template-matched crops) are compared with boxes built from the skeleton masks: for each crop region the boxes of the bone regions inside it are united, and the agreement is scored with the intersection over union and two directional containment ratios. Regions marked no for full containment are crops that frame only part of the bone, such as the elbow and knee crops for the humerus and femur masks.",
             md_table(["Crop region", "Views", "Mean IoU", "Median IoU", "Mean containment in template", "Mean containment in segmentation", "Full containment expected"], cross_rows, "lrrrrrl"),
             "Source: `tables/skeleton_box_crosscheck.csv`."]
    write_section("s11_label_generation.md", parts)


def section_12() -> None:
    counts = read_table("split_counts.csv")
    order = {"train": 0, "validation": 1, "test": 2}
    view_order = {"anterior": 0, "posterior": 1, "both": 2}
    counts = counts.assign(a=counts.split.map(order), b=counts.view.map(view_order)).sort_values(["a", "b"])
    rows = [[r.split, r.view, f"{r.cases:,}", f"{r.images:,}", f"{r.boxes_benign:,}", f"{r.boxes_malignant:,}", f"{r.images_with_benign:,}", f"{r.images_with_malignant:,}",
             f"{r.regions_benign:,}", f"{r.regions_malignant:,}", f"{r.skeleton_manual:,}", f"{r.skeleton_pseudo:,}"] for r in counts.itertuples()]
    total_cases = int(counts[counts.view == "both"].cases.sum())
    parts = ["# S12. Data description",
             f"BS-80K has 3,247 patients with an anterior and a posterior whole-body scan. {total_cases:,} cases are used, each with both views, stacked as a two-channel image of 1024 x 256 pixels.",
             "## Split",
             "The case identifiers are sorted and shuffled with NumPy `default_rng` and seed 42. The first 80% of the shuffled list is the training split, the next 10% the validation split, and the rest the test split, which gives 2,340, 292, and 293 cases. Both views of a case are in the same split. The assignment of every case is in `tables/split_assignment.csv`.",
             "## Counts per split and view",
             md_table(["Split", "View", "Cases", "Images", "Boxes, benign", "Boxes, malignant", "Images with benign", "Images with malignant", "Regions, benign", "Regions, malignant", "Skeleton, manual", "Skeleton, predicted"], rows),
             "Boxes are the bounding boxes of BS-80K. Regions are the connected components of the hotspot masks made from the boxes. Skeleton columns count the views by the source of the skeleton mask. An image is one view of a case. Source: `tables/split_counts.csv`.",
             "## Data record of the masks",
             "The hotspot and skeleton masks are published as one data record of five files. The scans are not part of it.",
             md_table(["File", "Content"], [
                 ["`hotspot_masks.zip`", "5,462 masks, one for each view with hotspot boxes, pixel values 0 background, 1 benign, 2 malignant"],
                 ["`skeleton_masks.zip`", "6,494 masks, one for every view, pixel values 0 background and 1 to 12 for the twelve skeleton regions"],
                 ["`manifest.csv`", "One row per mask: mask set, patient, study, view, path in the archive, source, split, SHA-256, size in bytes"],
                 ["`SHA256SUMS.txt`", "SHA-256 of the two archives"],
                 ["`README.md`", "Pixel values, method, and splits"],
             ], "ll"),
             "Inside the archives a mask is `<mask set>/<patient>/<study>/<view>.png`, 1024 x 256 pixels, 8 bit, aligned with the scan of the same patient, study, and view. The source of a skeleton mask is `manual` or `predicted`, and the split is `train`, `validation`, `test`, or `unused` for the 322 patients that are not among the 2,925 cases. The package is built by `scripts/package_zenodo_record.py`."]
    write_section("s12_data_description.md", parts)


def section_13() -> None:
    prior = read_table("prior_studies.csv")
    rows = [[r.group, str(r.year), r.model, r.input, r.data, r.size, r.training, r.metric, str(r.result), r.evidence] for r in prior.sort_values(["group", "year"]).itertuples()]
    removed = [
        ["Skeleton", "2022", "Btrfly-Net and U-Net, with cross-domain data and augmentation", "-", "-", "-", "Single-task", "Dice", "Btrfly-Net 0.8560, U-Net 0.7800", "Nugraha, Rachmawati, Sulistiyo, ICITEE 2022, 10.1109/ICITEE56407.2022.9954073. Abstract: whole-body bone scan segmentation, Dice 0.856 for Btrfly-Net and 0.780 for U-Net"],
        ["Skeleton", "2023", "SegFormer", "-", "-", "-", "Single-task", "mIoU", "0.7786", "Syam, Rachmawati, Sulistiyo, ICITACEE 2023, 10.1109/ICITACEE58587.2023.10277219. Abstract: bone scan images into 12 bone-region classes, highest mIoU 77.86% against FCN and DeepLabv3+"],
        ["Skeleton", "2023", "DANet", "-", "-", "-", "Single-task", "mIoU", "Anterior 0.7685, posterior 0.8099", "Sitaba, Rachmawati, Sulistiyo, ICITACEE 2023, 10.1109/ICITACEE58587.2023.10276939. Abstract: 12 bone-region classes, mIoU 76.85% anterior and 80.99% posterior"],
        ["Hotspots", "2025", "U-Net++", "-", "-", "-", "Single-task", "F1 and IoU", "F1 0.9900, IoU 0.3410", "Muhammad, Rachmawati, Yunanto, ICoICT 2025, 10.1109/ICoICT66265.2025.11192897. Abstract: hotspot segmentation on anterior and posterior views, F1 0.990 and IoU 0.341 in the 4-segment configuration"],
        ["Skeleton", "2024", "Efficient-BtrflyNet", "Whole body", "-", "37 images", "Single-task", "Dice", "-", "Rachmawati, Sulistiyo, Nugraha, Int. J. Comput. Intell. Syst. 17, 2024, 10.1007/s44196-024-00453-4. Abstract: anterior and posterior views processed together, 37 bone scan images, Dice reported without a value in the abstract"],
    ]
    head = ["Group", "Year", "Model", "Input", "Data", "Size", "Training", "Metric", "Result", "Evidence"]
    parts = ["# S13. Table I extended",
             "Table I of the paper lists ten studies of bone scintigraphy segmentation. Each cell is taken from the abstract or the methods of the study. The Evidence column gives what the cell is based on. A dash means the abstract does not state it. The size is the number of patients or annotated images.",
             "## The ten studies of Table I", md_table(head, rows, "lrllllllll"),
             "Source: `tables/prior_studies.csv`.",
             "## Five studies removed from Table I",
             "Five studies from one research group were removed from Table I to save space. Metrics given as percentages in the abstracts are written as decimals.",
             md_table(head, removed, "lrllllllll")]
    write_section("s13_prior_studies.md", parts)


def froc_value(frame: pd.DataFrame, model: str, setting: str, level: float = 0.5) -> float:
    column = f"sensitivity_at_fp_{level}"
    return float(frame[(frame.model == model) & (frame.setting == setting)].iloc[0][column])


def section_14() -> None:
    f = read_table("filtering_effects.csv")
    m = f[f.target == "malignant"]
    base = m[m.setting == "no_uq"].set_index("model")
    discr = read_table("uq_discrimination_by_config.csv")
    det = read_table("stats_lesion_detection_model_pairs.csv")
    dice_pairs = read_table("stats_dice_model_pairs.csv")
    auc_models = read_table("stats_auroc_model_pairs.csv")
    cbam = [name for name in MODEL_ORDER if name.startswith("nnunetcbam")]
    multi_per_model = discr.groupby(["model", "method"]).auroc.mean().unstack()
    multitask = [name for name in MODEL_ORDER if FISSION[name] != "single-task"]

    def removed(model: str, setting: str) -> float:
        return 1 - float(m[(m.model == model) & (m.setting == setting)].iloc[0].false_regions) / float(base.loc[model].false_regions)

    def kept(model: str, setting: str) -> float:
        return float(m[(m.model == model) & (m.setting == setting)].iloc[0].true_regions_kept)

    def dice_change(model: str, setting: str) -> float:
        return float(m[(m.model == model) & (m.setting == setting)].iloc[0].dice_lesion_bearing - base.loc[model].dice_lesion_bearing)

    all_removed = [removed(model, s) for model in MODEL_ORDER for s in PAPER_METHODS]
    all_kept = [kept(model, s) for model in MODEL_ORDER for s in PAPER_METHODS]
    all_change = [dice_change(model, s) for model in MODEL_ORDER for s in PAPER_METHODS]
    cbam_removed = [removed(model, s) for model in cbam for s in PAPER_METHODS]
    cbam_kept = [kept(model, s) for model in cbam for s in PAPER_METHODS]
    cbam_froc = [froc_value(m, model, s) for model in cbam for s in PAPER_METHODS]
    cbam_random = [froc_value(m, model, "random_removal") for model in cbam]
    best = max(((froc_value(m, model, s), model, s) for model in MODEL_ORDER for s in PAPER_METHODS))
    metaseg_mean = {model: multi_per_model.loc[model, "metaseg"] for model in MODEL_ORDER}
    method_means = {s: statistics.mean(multi_per_model.loc[model, s] for model in multitask) for s in PAPER_METHODS}
    single_vs_multi = []
    for backbone in ("nnunet", "nnunetcbam", "segformer"):
        single = f"{backbone}_single"
        for model in MODEL_ORDER:
            if model.startswith(backbone + "_") and model != single:
                row = det[(det.target == "malignant") & (((det.model_a == single) & (det.model_b == model)) | ((det.model_a == model) & (det.model_b == single)))].iloc[0]
                a = row.detected_a if row.model_a == single else row.detected_b
                b = row.detected_b if row.model_a == single else row.detected_a
                single_vs_multi.append((model, int(a), int(b), float(row.holm_p)))
    sig_detect = [f"{label(model)} ({a} to {b}, Holm p {pval(p)})" for model, a, b, p in single_vs_multi if p < 0.05]
    fp_lines = []
    for backbone in ("nnunet", "nnunetcbam", "segformer"):
        multi = [name for name in multitask if name.startswith(backbone + "_")]
        fp_lines.append(f"{BACKBONE[f'{backbone}_single']}: single-task {base.loc[f'{backbone}_single'].fp_per_case:.2f}, multi-task {min(base.loc[x].fp_per_case for x in multi):.2f} to {max(base.loc[x].fp_per_case for x in multi):.2f}")
    more = [fission for fission in ("Early", "Early-Mid", "Mid", "Late") if base.loc[next(n for n in cbam if FISSION[n] == fission)].fp_per_case > base.loc[next(n for n in MODEL_ORDER if n.startswith("nnunet_") and FISSION[n] == fission)].fp_per_case]
    mal_pairs = dice_pairs[dice_pairs.target == "malignant"]
    t_flag, w_flag = mal_pairs[mal_pairs.ttest_holm_p < 0.05], mal_pairs[mal_pairs.holm_p < 0.05]
    both_flag = t_flag.merge(w_flag, on=["model_a", "model_b"])
    proposed_m = m[(m.model == PROPOSED)]
    pre, post = proposed_m[proposed_m.setting == "no_uq"].iloc[0], proposed_m[proposed_m.setting == "metaseg"].iloc[0]
    mal_model_pairs = auc_models[auc_models.target == "malignant"]
    rows = [
        ["Region AUC of MetaSeg across the fourteen checkpoints, and the mean over the eleven multi-task checkpoints for each of the four methods", f"MetaSeg {min(metaseg_mean.values()):.4f} to {max(metaseg_mean.values()):.4f}. Mean over the eleven multi-task checkpoints: " + ", ".join(f"{METHOD_NAMES[s]} {v:.4f}" for s, v in sorted(method_means.items(), key=lambda kv: -kv[1])) + ". Region AUC is the mean over the two views and the two classes.", "`uq_discrimination_by_config.csv`"],
        ["The four methods on the five nnU-Net with CBAM checkpoints, malignant", f"Keep {min(cbam_kept) * 100:.0f} to {max(cbam_kept) * 100:.0f}% of the true regions and remove {min(cbam_removed) * 100:.0f} to {max(cbam_removed) * 100:.0f}% of the false regions. FROC sensitivity at 0.5 false positives per case {min(cbam_froc):.3f} to {max(cbam_froc):.3f}, against {min(cbam_random):.3f} to {max(cbam_random):.3f} for random removal.", "`filtering_effects.csv`"],
        ["The four methods on all fourteen checkpoints, malignant", f"Remove {min(all_removed) * 100:.0f} to {max(all_removed) * 100:.0f}% of the false regions (median {statistics.median(all_removed) * 100:.0f}%), keep {min(all_kept) * 100:.0f} to {max(all_kept) * 100:.0f}% of the true regions (median {statistics.median(all_kept) * 100:.0f}%), and change the lesion-bearing malignant Dice by {min(all_change):+.4f} to {max(all_change):+.4f} (median {statistics.median(all_change):+.4f}).", "`filtering_effects.csv`"],
        ["Highest FROC value of all checkpoints and the four methods", f"{best[0]:.3f}, {label(best[1])} (`{best[1]}`) with {METHOD_NAMES[best[2]].lower()}, at 0.5 false positives per case, malignant.", "`filtering_effects.csv`"],
        ["Effect of the skeleton task on the matched malignant hotspots", ("Significant after Holm correction only for " + "; ".join(sig_detect) if sig_detect else "No single-task against multi-task pair is significant after Holm correction") + ". Pairs of the single-task checkpoint against each multi-task checkpoint of the same backbone.", "`stats_lesion_detection_model_pairs.csv`"],
        [f"Proposed method (`{PROPOSED}`) with MetaSeg, malignant", f"Region precision {pre.region_precision:.3f} to {post.region_precision:.3f}. Removes {int(pre.false_regions - post.false_regions)} of {int(pre.false_regions)} false regions. Hotspot sensitivity at 1.0 false positives per case {froc_value(m, PROPOSED, 'metaseg', 1.0):.3f}, against {froc_value(m, PROPOSED, 'random_removal', 1.0):.3f} for random removal. The smallest p of its MetaSeg region AUC against any other checkpoint is {pval(mal_model_pairs.bootstrap_p.min())}.", "`filtering_effects.csv`, `stats_auroc_model_pairs.csv`"],
        ["False positives per case before and after adding the skeleton task, malignant", "; ".join(fp_lines) + f". The nnU-Net with CBAM checkpoint has more false positives per case than the nnU-Net checkpoint at {len(more)} of the 4 multi-task fission points" + (": " + ", ".join(more) if more else "") + ".", "`filtering_effects.csv`"],
        ["Dice pairs flagged by the t-test", f"After Holm correction the t-test flags {len(t_flag)} of 91 malignant Dice pairs and the Wilcoxon test {len(w_flag)}. {len(both_flag)} pairs are flagged by both, and {len(t_flag) - len(both_flag)} only by the t-test.", "`stats_dice_model_pairs.csv`"],
        [f"True regions kept at Early fission with CBAM (`{PROPOSED}`), malignant", ", ".join(f"{METHOD_NAMES[s]} {kept(PROPOSED, s):.3f}" for s in PAPER_METHODS) + ".", "`filtering_effects.csv`"],
        ["Limitations of the 9-page draft", "Dice on the images with a hotspot does not penalize false predictions on images without one, and the CBAM weights of the multi-task checkpoints come from the single-task checkpoints.", "S1 and S9"],
    ]
    parts = ["# S14. Statements cut from the paper",
             "Statements of the first, longer draft that did not fit the six pages, restated with the numbers computed from the metric files of this repository. All values use the UQ run, the test split, and the lesion-bearing Dice unless the row says otherwise.",
             md_table(["Statement", "Restated", "Source"], rows, "lll")]
    write_section("s14_statements_cut_from_paper.md", parts)
