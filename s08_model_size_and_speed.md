# S8. Model size and speed

Parameters, floating-point operations, and forward time of the fourteen checkpoints for one forward pass at the input of the UQ run: a two-channel image of the anterior and posterior view, 1024 x 256 pixels, for the nnU-Net-based checkpoints, and a 1024 x 512 image with the two views side by side and three channels for SegFormer.

| Checkpoint | Parameters (million) | GFLOPs | Median forward time (ms) | Input shape |
|:---|---:|---:|---:|:---|
| nnU-Net, single-task (`nnunet_single`) | 45.809 | 119.554 | 30.664 | 1x2x1024x256 |
| nnU-Net, Early (`nnunet_early`) | 72.777 | 201.998 | 54.421 | 1x2x1024x256 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 65.155 | 201.058 | 58.703 | 1x2x1024x256 |
| nnU-Net, Mid (`nnunet_mid`) | 45.834 | 135.560 | 49.868 | 1x2x1024x256 |
| nnU-Net, Late (`nnunet_late`) | 45.861 | 119.991 | 48.510 | 1x2x1024x256 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 46.061 | 119.692 | 58.147 | 1x2x1024x256 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 73.139 | 202.205 | 95.713 | 1x2x1024x256 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 65.484 | 201.265 | 94.354 | 1x2x1024x256 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 46.086 | 135.749 | 73.503 | 1x2x1024x256 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 46.114 | 120.129 | 60.970 | 1x2x1024x256 |
| SegFormer, single-task (`segformer_single`) | 24.723 | 115.822 | 87.860 | 1x3x1024x512 |
| SegFormer, Early (`segformer_early`) | 25.252 | 135.300 | 97.846 | 1x3x1024x512 |
| SegFormer, Mid (`segformer_mid`) | 24.989 | 133.219 | 92.754 | 1x3x1024x512 |
| SegFormer, Late (`segformer_late`) | 24.726 | 116.040 | 88.535 | 1x3x1024x512 |

FLOPs are counted with `torch.utils.flop_counter.FlopCounterMode`, which covers convolutions, matrix multiplications, and attention. Time is the median of 50 timed forward passes at batch size 1 after 10 warm-up passes, synchronized, with PyTorch 2.11.0 and CUDA 12.8 on an NVIDIA GeForce RTX 4050 Laptop GPU. The checkpoints were trained on another GPU, see S9. The SegFormer parameter counts agree with the trained checkpoints to within 0.001 million (`checkpoint_parameters_million` in `tables/model_size.csv`).

Source: `tables/model_size.csv`.
