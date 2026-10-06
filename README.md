# Multi-Task Hotspot and Skeleton Segmentation on Whole-Body Bone Scintigraphy with Uncertainty Quantification

Supplementary material for the paper of the same title. The paper holds the method and results. This repository holds the figures and the code location.

## Code

The training and inference code is in two repositories.

| Repository | Content |
|---|---|
| [nnunetv2-multitask](https://github.com/Liamours/nnunetv2-multitask) | Fork of nnU-Net v2 for multi-task segmentation |
| [segformer-multitask](https://github.com/Liamours/segformer-multitask) | Multi-task SegFormer |

The `code/` folder here is reserved for the evaluation and uncertainty scripts.

## Figures

### Skeleton and hotspot mask generation

![Skeleton and hotspot mask generation](figures/skeleton_and_hotspot_mask_generation.png)

### Multi-task nnU-Net with CBAM and MetaSeg filtering

![Multi-task nnU-Net with CBAM and MetaSeg filtering](figures/multitask_nnunet_cbam_metaseg_pipeline.png)

### Test case with skeleton and hotspot masks

![Test case with skeleton and hotspot masks](figures/test_case_scan_skeleton_hotspot_masks.png)

### Decoder fission points

![Decoder fission points](figures/decoder_fission_points.png)

### Filtered predictions by uncertainty method

![Filtered predictions by uncertainty method](figures/filtered_predictions_by_uq_method.png)
