# S13. Table I extended

Table I of the paper lists ten studies of bone scintigraphy segmentation. Each cell is taken from the abstract or the methods of the study. The Evidence column gives what the cell is based on. A dash means the abstract does not state it. The size is the number of patients or annotated images.

## The ten studies of Table I

| Group | Year | Model | Input | Data | Size | Training | Metric | Result | Evidence |
|:---|---:|:---|:---|:---|:---|:---|:---|:---|:---|
| Hotspots | 2020 | U-Net, Mask R-CNN | Thorax crop | Private | 76 patients | Single-task | IoU | 0.6103 | 112 samples (anterior and posterior) of whole-body bone SPECT images from 76 patients; IoU 0.6103 (abstract); data restricted by hospital ethics committee |
| Hotspots | 2023 | Double U-Net | Whole body | Private | 200 patients | Single-task | F1 | 0.6660 | 100 breast cancer and 100 prostate cancer patients, small internal dataset; F1-score 66.60% (abstract); Data Availability Statement: Not applicable |
| Hotspots | 2025 | Attention encoder-decoder | Patch | Private | 168 patients | Single-task | Dice | 0.6720 | 168 patients with bone metastases from lung cancer; 256x256 sub-images; DSC 0.6720 (abstract); anonymised data received from the hospital |
| Hotspots | 2025 | Conditional GAN | Thorax crop | Private | 171 patients | Single-task | Dice | 0.6671 | 286 SPECT images from 171 patients (118 training, 53 test); thoracic region cropped to 256x256; DSC 0.6671 (abstract); validation subset on request, whole dataset not yet public |
| Hotspots | 2026 | U-Net with Transformer | Patch | Private | 932 patients | Single-task | Dice | 0.8750 | 932 patients; 256x256 patches; Dice 0.8750 against U-Net, U-Net++, Attention U-Net, ResUNet++, MK-UNet; data not publicly available |
| Hotspots and skeleton | 2020 | Btrfly-Net | Whole body | Private | 246 patients | Separate | BSI correlation | 0.9337 | 246 cases of prostate cancer; cross-correlation between measured and true BSI 0.9337 (abstract); one network for skeleton and one for hotspots |
| Hotspots and skeleton | 2023 | U-Net | Patch | Private | 617 patients | Joint | Dice | Hotspot 0.7408, skeleton 0.8399 | 617 patients; 128x128 patches; mean Dice 74.08 lesion and 83.99 anterior skeleton; data cannot be shared publicly |
| Skeleton | 2023 | Mask R-CNN | Whole body | Private | 359 images | Single-task | F1 | Prostate 0.9000, breast 0.8800 | 196 prostate and 163 breast cancer WBBS images; F1 0.90 prostate and 0.88 breast; Data Availability Statement: Not applicable |
| Skeleton | 2026 | nnU-Net | Whole body | Public | 3,593 images | Single-task | Dice | Anterior 0.8168, posterior 0.8345 | 3,593 whole-body images from BS-80K; 5-fold macro-averaged Dice 0.8168 anterior and 0.8345 posterior (abstract) |
| Skeleton | 2026 | Btrfly-Net | Whole body | Public and private | 3,512 images | Single-task | Dice | Anterior 0.6140, posterior 0.7890 | 3,512 manually annotated images from BS-80K; Dice 0.614 anterior and 0.789 posterior (abstract); model trained on a private cohort |

Source: `tables/prior_studies.csv`.

## Five studies removed from Table I

Five studies from one research group were removed from Table I to save space. Metrics given as percentages in the abstracts are written as decimals.

| Group | Year | Model | Input | Data | Size | Training | Metric | Result | Evidence |
|:---|---:|:---|:---|:---|:---|:---|:---|:---|:---|
| Skeleton | 2022 | Btrfly-Net and U-Net, with cross-domain data and augmentation | - | - | - | Single-task | Dice | Btrfly-Net 0.8560, U-Net 0.7800 | Nugraha, Rachmawati, Sulistiyo, ICITEE 2022, 10.1109/ICITEE56407.2022.9954073. Abstract: whole-body bone scan segmentation, Dice 0.856 for Btrfly-Net and 0.780 for U-Net |
| Skeleton | 2023 | SegFormer | - | - | - | Single-task | mIoU | 0.7786 | Syam, Rachmawati, Sulistiyo, ICITACEE 2023, 10.1109/ICITACEE58587.2023.10277219. Abstract: bone scan images into 12 bone-region classes, highest mIoU 77.86% against FCN and DeepLabv3+ |
| Skeleton | 2023 | DANet | - | - | - | Single-task | mIoU | Anterior 0.7685, posterior 0.8099 | Sitaba, Rachmawati, Sulistiyo, ICITACEE 2023, 10.1109/ICITACEE58587.2023.10276939. Abstract: 12 bone-region classes, mIoU 76.85% anterior and 80.99% posterior |
| Hotspots | 2025 | U-Net++ | - | - | - | Single-task | F1 and IoU | F1 0.9900, IoU 0.3410 | Muhammad, Rachmawati, Yunanto, ICoICT 2025, 10.1109/ICoICT66265.2025.11192897. Abstract: hotspot segmentation on anterior and posterior views, F1 0.990 and IoU 0.341 in the 4-segment configuration |
| Skeleton | 2024 | Efficient-BtrflyNet | Whole body | - | 37 images | Single-task | Dice | - | Rachmawati, Sulistiyo, Nugraha, Int. J. Comput. Intell. Syst. 17, 2024, 10.1007/s44196-024-00453-4. Abstract: anterior and posterior views processed together, 37 bone scan images, Dice reported without a value in the abstract |
