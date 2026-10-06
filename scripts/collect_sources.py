"""Copy the metric files, figures, and training records the sections are built from into tables/ and figures/.

Run from the project that holds the results (the folder with draft/, models/, results/, datasets/):

    uv run --no-project --with pandas python scripts/collect_sources.py --project <project root>

Nothing is trained or re-run. The sections are then rebuilt from tables/ alone with scripts/build_sections.py.
"""
from __future__ import annotations

import argparse
import gzip
import json
import shutil
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from common import FIGURES, ROOT, TABLES, TARGETS, project_folder

METRIC_FILES = [
    "dice_by_model.csv", "filtering_effects.csv", "seg_published.csv", "stats_auroc_method_pairs.csv",
    "stats_auroc_model_pairs.csv", "stats_dice_model_pairs.csv", "stats_dice_model_pairs_published_run.csv",
    "stats_filtering_dice.csv", "stats_lesion_detection_model_pairs.csv", "uq_discrimination_by_config.csv",
    "uq_discrimination_by_model.csv",
]
NNUNET_RUNS = {
    "nnunet_single": ("Dataset261_BS80KLesionOnly", "nnUNetTrainerMultiTask_100epochs__nnUNetPlansA1Lesion2GB__2d"),
    "nnunetcbam_single": ("Dataset261_BS80KLesionOnly", "nnUNetTrainerMultiTask_100epochs__nnUNetPlansA1ControlledBatch4CBAMPostNorm__2d"),
    "nnunet_early": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTask_100epochs__nnUNetPlansA3ControlledBatch4__2d"),
    "nnunet_earlymid": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTask_100epochs__nnUNetPlansMultiTaskEarlyMid__2d"),
    "nnunet_mid": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTask_100epochs__nnUNetPlansMultiTaskMid__2d"),
    "nnunet_late": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTask_100epochs__nnUNetPlansMultiTask2GB__2d"),
    "nnunetcbam_multidecoder": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTaskDualDecoderCBAMWarmStart_100epochs__nnUNetPlansMultiTaskDualDecoderCBAMPostNorm__2d"),
    "nnunetcbam_earlymid": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTaskEarlyMidCBAMWarmStart_100epochs__nnUNetPlansMultiTaskEarlyMidCBAMPostNorm__2d"),
    "nnunetcbam_mid": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTaskMidCBAMWarmStart_100epochs__nnUNetPlansMultiTaskMidCBAMPostNorm__2d"),
    "nnunetcbam_multihead": ("Dataset260_BS80KLesionBoneMT", "nnUNetTrainerMultiTaskCBAMWarmStart_100epochs__nnUNetPlansMultiTaskCBAMPostNorm__2d"),
}
SEGFORMER_RUNS = {"segformer_single": "single_task", "segformer_early": "dual_decoder", "segformer_mid": "dual_fuse", "segformer_late": "dual_head"}
HOTSPOT_STEP_IMAGES = ["scan_box", "otsu", "closed_opened", "percentile", "final"]


def copy(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_metric_files(project: Path) -> None:
    for name in tqdm(METRIC_FILES, desc="metric files"):
        copy(project_folder(project, "components") / "supplementary" / "metrics_all_models" / name, TABLES / name)
    copy(project_folder(project, "components") / "supplementary" / "froc_curves" / "froc_curves.csv", TABLES / "froc_curves.csv")
    copy(project_folder(project, "components") / "supplementary" / "model_size" / "model_size.csv", TABLES / "model_size.csv")
    copy(project_folder(project, "components") / "supplementary" / "data_description" / "split_counts.csv", TABLES / "split_counts.csv")
    copy(project_folder(project, "components") / "supplementary" / "data_description" / "split_assignment.csv", TABLES / "split_assignment.csv")
    copy(project_folder(project, "references") / "prior_studies.csv", TABLES / "prior_studies.csv")
    copy(project_folder(project, "components") / "tables/model_ranking.csv", TABLES / "model_ranking.csv")
    for target in TARGETS:
        copy(project_folder(project, "components") / "supplementary" / "froc_curves" / f"froc_{target}.png", FIGURES / "froc" / f"froc_{target}.png")


def uq_example_regions(project: Path) -> None:
    root = project_folder(project, "components") / "supplementary" / "uq_examples"
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    sets = manifest["sets"]["uq_agreement"]
    rows = []
    for group, cases in sets.items():
        for position, entry in enumerate(cases, start=1):
            folder = root / "uq_agreement" / f"{group}_{position}_{entry['case']}"
            data = json.loads((folder / "regions.json").read_text(encoding="utf-8"))
            for view, regions in data["views"].items():
                for region in regions:
                    row = {"set": group, "example": position, "case": entry["case"], "disagreement": entry["disagreement"], "view": view,
                           "region_id": region["region_id"], "area": region["area"], "true_positive": region["true_positive"]}
                    for method, score in region["scores"].items():
                        row[f"score_{method}"] = score
                        row[f"kept_{method}"] = region["kept"][method]
                    rows.append(row)
    pd.DataFrame(rows).to_csv(TABLES / "uq_examples_regions.csv", index=False, encoding="utf-8")


def label_and_hotspot_tables(project: Path) -> None:
    summary = json.loads((project_folder(project, "components") / "samples/hotspot_steps/summary.json").read_text(encoding="utf-8"))
    paths = pd.DataFrame(
        [{"path": path, "boxes": summary["stages"][path], "share": summary["share"][path], "median_box_area_pixels": summary["median_box_area"][path]}
         for path in summary["stages"]]
    )
    paths.to_csv(TABLES / "hotspot_mask_paths.csv", index=False, encoding="utf-8")
    inventory = json.loads((project / "results/lesion_thresholding_comparison/method_inventory.json").read_text(encoding="utf-8"))["rows"]
    keep = ["algorithm_method_name", "fallback_algorithm_method", "can_escape_bounding_box", "total_bounding_boxes_checked",
            "total_segment_per_bounding_box_mean", "total_segment_per_bounding_box_max", "square_score_mean"]
    pd.DataFrame(inventory)[keep].to_csv(TABLES / "hotspot_algorithms.csv", index=False, encoding="utf-8")
    examples = [{"path": name, **{k: v for k, v in example.items() if k != "matches_dataset_label"}} for name, example in summary["examples"].items()]
    for row in examples:
        row["box"] = "-".join(str(v) for v in row["box"])
    pd.DataFrame(examples).to_csv(TABLES / "hotspot_mask_examples.csv", index=False, encoding="utf-8")
    copy(project / "results/bone_region_samples_and_crosscheck/bone_region_bb_crosscheck/summary.csv", TABLES / "skeleton_box_crosscheck.csv")
    pseudo = project / "datasets/source/bs80k_bone_region_resolve/labels/dataset902-pseudo"
    plans = json.loads(gzip.open(pseudo / "plans.json.gz", "rt", encoding="utf-8").read())
    dataset = json.loads(gzip.open(pseudo / "dataset.json.gz", "rt", encoding="utf-8").read())
    config = plans["configurations"]["2d"]
    pd.DataFrame([{"setting": key, "value": value} for key, value in [
        ("configuration", "2d"), ("classes", len(dataset["labels"])), ("training_views", dataset["numTraining"]),
        ("patch_size", "x".join(str(v) for v in config["patch_size"])), ("batch_size", config["batch_size"]),
        ("normalization", "-".join(config["normalization_schemes"])), ("predicted_views", int(sources_total(project)))]]).to_csv(
        TABLES / "skeleton_pseudo_label_model.csv", index=False, encoding="utf-8")
    manifest = project / "datasets/source/bs80k_bone_region_resolve/labels/dataset902-merged/manifest.csv.gz"
    with gzip.open(manifest, "rt", encoding="utf-8") as handle:
        sources = pd.read_csv(handle)["source"].value_counts()
    pd.DataFrame({"source": sources.index, "views": sources.values}).to_csv(TABLES / "skeleton_label_sources_bs80k.csv", index=False, encoding="utf-8")
    for name in HOTSPOT_STEP_IMAGES:
        for path in ("otsu", "percentile"):
            copy(project_folder(project, "components") / "samples/hotspot_steps" / f"{path}_{name}.png", FIGURES / "hotspot_steps" / f"{path}_{name}.png")


def sources_total(project: Path) -> int:
    pool = project / "datasets/source/bs80k_bone_region_resolve/data/unlabeled_pool"
    return sum(1 for _ in pool.glob("*.png"))


def software_versions(project: Path) -> None:
    import re
    lock = (project / "repo/segformer_multitask/uv.lock").read_text(encoding="utf-8")
    pins = {name: re.search(rf'\[\[package\]\]\nname = "{name}"\nversion = "([^"]+)"', lock).group(1) for name in ("torch", "transformers")}
    nnunet = re.search(r'^version = "([^"]+)"', (project / "repo/nnunetv2_multitask/pyproject.toml").read_text(encoding="utf-8"), re.M).group(1)
    debug = json.loads(next((project / "models/nnunet").glob("*/*/fold_0/debug.json")).read_text(encoding="utf-8"))
    pd.DataFrame([
        {"software": "PyTorch", "version": debug["torch_version"], "source": "debug.json of the nnU-Net runs"},
        {"software": "PyTorch (SegFormer environment)", "version": pins["torch"], "source": "uv.lock of segformer_multitask"},
        {"software": "Transformers", "version": pins["transformers"], "source": "uv.lock of segformer_multitask"},
        {"software": "nnU-Net (multi-task fork)", "version": nnunet, "source": "pyproject.toml of nnunetv2_multitask"},
        {"software": "GPU of the nnU-Net runs", "version": debug["gpu_name"], "source": "debug.json of the nnU-Net runs"},
    ]).to_csv(TABLES / "software_versions.csv", index=False, encoding="utf-8")


def parse_optimizer(text: str, key: str) -> str:
    for line in text.splitlines():
        if line.strip().startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return "-"


def nnunet_training(project: Path) -> None:
    rows = []
    for checkpoint, (dataset, trainer) in tqdm(NNUNET_RUNS.items(), desc="nnU-Net runs"):
        folder = project / "models/nnunet" / dataset / trainer
        plans = json.loads((folder / "plans.json").read_text(encoding="utf-8"))
        config = plans["configurations"]["2d"]
        arch = config["architecture"]["arch_kwargs"]
        debug = json.loads((folder / "fold_0/debug.json").read_text(encoding="utf-8"))
        log = next((folder / "fold_0").glob("training_log_*.txt")).name
        cbam = arch.get("cbam", {})
        multitask = arch.get("multitask", {})
        rows.append({
            "checkpoint": checkpoint, "dataset": dataset, "trainer": trainer.split("__")[0], "plans": trainer.split("__")[1],
            "network_class": config["architecture"]["network_class_name"].split(".")[-1],
            "multitask_variant": multitask.get("variant", "-"),
            "cbam": bool(cbam.get("enabled", False)), "cbam_post_norm": cbam.get("post_norm", "-"),
            "batch_size": config["batch_size"], "patch_size": "x".join(str(v) for v in config["patch_size"]),
            "stages": arch["n_stages"], "features_per_stage": "-".join(str(v) for v in arch["features_per_stage"]),
            "epochs": debug["num_epochs"], "initial_lr": debug["initial_lr"], "weight_decay": debug["weight_decay"],
            "momentum": parse_optimizer(debug["optimizer"], "momentum"), "foreground_oversampling": debug["oversample_foreground_percent"],
            "loss_weights": "/".join(str(task["loss_weight"]) for task in multitask.get("tasks", [])) or "-",
            "gpu": debug["gpu_name"], "torch": debug["torch_version"], "cudnn": debug["cudnn_version"], "training_log": log,
        })
        copy(folder / "fold_0/progress.png", FIGURES / "training_curves" / f"{checkpoint}_progress.png")
    pd.DataFrame(rows).to_csv(TABLES / "training_nnunet.csv", index=False, encoding="utf-8")


def segformer_training(project: Path) -> None:
    rows = []
    for checkpoint, run in SEGFORMER_RUNS.items():
        config = json.loads((project / "models" / run / f"{run}_config.json").read_text(encoding="utf-8"))
        rows.append({
            "checkpoint": checkpoint, "run": run, "backbone": config["model"]["variant"], "task_mode": config["model"]["task_mode"],
            "pretrained": config["model"]["pretrained_hf_name"], "decoder_dim": config["model"]["decoder_dim"],
            "image_size": "x".join(str(v) for v in config["data"]["image_size"]), "batch_size": config["data"]["batch_size"],
            "optimizer": config["optimizer"]["name"], "lr_backbone": config["optimizer"]["learning_rate_backbone"],
            "lr_head": config["optimizer"]["learning_rate_head"], "weight_decay": config["optimizer"]["weight_decay"],
            "scheduler": config["scheduler"]["name"], "warmup_iters": config["scheduler"]["warmup_iters"],
            "loss": config["loss"]["name"], "loss_ce_weight": config["loss"]["ce_weight"], "loss_dice_weight": config["loss"]["dice_weight"], "task_weights": f"{config['loss'].get('task_a_weight', '-')}/{config['loss'].get('task_b_weight', '-')}",
            "epochs": config["run"]["epochs"], "seed": config["run"]["seed"], "amp": config["run"]["amp_dtype"] if config["run"]["amp"] else "off",
            "checkpoint_metric": config["logging"]["checkpoint_metric"],
        })
        log = project / "models" / run / f"{run}_metrics.jsonl"
        validation = [row for row in map(json.loads, log.read_text(encoding="utf-8").splitlines()) if row.get("split") == "val"]
        key = "task_a_foreground_mean_dice" if "task_a_foreground_mean_dice" in validation[0] else "foreground_mean_dice"
        pd.DataFrame({"epoch": [row["epoch"] for row in validation], "validation_foreground_mean_dice": [row[key] for row in validation],
                      "validation_loss": [row["loss"] for row in validation]}).to_csv(TABLES / f"curve_{checkpoint}.csv", index=False, encoding="utf-8")
    pd.DataFrame(rows).to_csv(TABLES / "training_segformer.csv", index=False, encoding="utf-8")


def architecture_figures(project: Path) -> None:
    for name in ("cbam_block_detail", "nnunet_plain_models", "nnunet_cbam_models", "segformer_models"):
        copy(project / "results/analyses/figures/manuscript" / f"{name}.png", FIGURES / "architecture" / f"{name}.png")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=ROOT.parents[1])
    project = parser.parse_args().project.resolve()
    TABLES.mkdir(exist_ok=True)
    copy_metric_files(project)
    uq_example_regions(project)
    label_and_hotspot_tables(project)
    nnunet_training(project)
    software_versions(project)
    segformer_training(project)
    architecture_figures(project)
    print("done")


if __name__ == "__main__":
    main()
