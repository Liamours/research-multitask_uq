# S1. Results of all fourteen checkpoints

Every checkpoint was evaluated on the 293 test cases (586 images, anterior and posterior). The checkpoint names are listed in the README.

| Term | Meaning |
|:---|:---|
| Lesion-bearing Dice | Mean Dice over the test images whose ground truth contains the class: 203 images for malignant, 473 for benign. The Dice of the paper. |
| Published-definition Dice | Mean Dice over every image where Dice is defined. An image without the class in the ground truth but with a predicted region scores 0, so false predictions lower this value. |
| UQ run | Predictions behind the uncertainty records: one full-image forward pass per view. Every table in these sections uses it unless a column says otherwise. |
| Standard-pipeline run | Predictions of the standard nnU-Net prediction pipeline (`nnUNetv2_predict`, sliding window). For SegFormer it is the same run as the UQ run. Columns of the CSV files named `published_run` hold it. |
| Region | An 8-connected component of the predicted class. A true region overlaps a ground-truth hotspot of its class, a false region overlaps none. |
| Matched hotspot | A ground-truth hotspot matched one to one with a predicted region. Hotspot sensitivity is the share of ground-truth hotspots matched. |
| False positives per case | Predicted regions not matched to a ground-truth hotspot, over both views, divided by the 293 test cases. |

## Malignant Dice

| Checkpoint | Lesion-bearing, UQ run | Lesion-bearing, standard-pipeline run | Published definition, UQ run | Published definition, standard-pipeline run |
|:---|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.4123 | 0.4082 | 0.2447 | 0.2771 |
| nnU-Net, Early (`nnunet_early`) | 0.4360 | 0.4387 | 0.2990 | 0.3092 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.4208 | 0.4163 | 0.3040 | 0.3029 |
| nnU-Net, Mid (`nnunet_mid`) | 0.4321 | 0.4304 | 0.2565 | 0.2765 |
| nnU-Net, Late (`nnunet_late`) | 0.4304 | 0.4360 | 0.3143 | 0.3184 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.4289 | 0.4231 | 0.2466 | 0.2762 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.4765 | 0.4600 | 0.3091 | 0.3061 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.4453 | 0.4349 | 0.2773 | 0.2904 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.4407 | 0.4255 | 0.2905 | 0.3063 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.4506 | 0.4388 | 0.3029 | 0.3061 |
| SegFormer, single-task (`segformer_single`) | 0.3705 | 0.3705 | 0.2926 | 0.2926 |
| SegFormer, Early (`segformer_early`) | 0.3825 | 0.3825 | 0.3156 | 0.3156 |
| SegFormer, Mid (`segformer_mid`) | 0.3973 | 0.3973 | 0.3175 | 0.3175 |
| SegFormer, Late (`segformer_late`) | 0.3857 | 0.3857 | 0.3249 | 0.3249 |

Source: `tables/dice_by_model.csv`. The number of images behind each cell is in the same file.

## Benign Dice

| Checkpoint | Lesion-bearing, UQ run | Lesion-bearing, standard-pipeline run | Published definition, UQ run | Published definition, standard-pipeline run |
|:---|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.5288 | 0.5324 | 0.4564 | 0.4698 |
| nnU-Net, Early (`nnunet_early`) | 0.5287 | 0.5384 | 0.4606 | 0.4743 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.5418 | 0.5532 | 0.4737 | 0.4864 |
| nnU-Net, Mid (`nnunet_mid`) | 0.5232 | 0.5314 | 0.4524 | 0.4612 |
| nnU-Net, Late (`nnunet_late`) | 0.5472 | 0.5546 | 0.4838 | 0.4903 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.5220 | 0.5303 | 0.4547 | 0.4697 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.5390 | 0.5426 | 0.4774 | 0.4788 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.5347 | 0.5422 | 0.4666 | 0.4776 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.5286 | 0.5364 | 0.4621 | 0.4725 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.5486 | 0.5539 | 0.4842 | 0.4888 |
| SegFormer, single-task (`segformer_single`) | 0.5319 | 0.5319 | 0.4756 | 0.4756 |
| SegFormer, Early (`segformer_early`) | 0.5498 | 0.5498 | 0.4870 | 0.4870 |
| SegFormer, Mid (`segformer_mid`) | 0.5451 | 0.5451 | 0.4856 | 0.4856 |
| SegFormer, Late (`segformer_late`) | 0.5473 | 0.5473 | 0.4847 | 0.4847 |

Source: `tables/dice_by_model.csv`. The number of images behind each cell is in the same file.

## Skeleton Dice

| Checkpoint | Mean | Skull | Cervical vertebrae | Thoracic vertebrae | Ribs | Sternum | Clavicle | Scapula | Humerus | Lumbar vertebrae | Sacrum | Pelvis | Femur |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, Early | 0.8819 | 0.9676 | 0.8762 | 0.8075 | 0.9305 | 0.8918 | 0.7231 | 0.8710 | 0.9047 | 0.8993 | 0.8735 | 0.9255 | 0.9174 |
| nnU-Net, Early-Mid | 0.8817 | 0.9677 | 0.8767 | 0.8083 | 0.9307 | 0.8922 | 0.7196 | 0.8717 | 0.9042 | 0.8994 | 0.8725 | 0.9251 | 0.9175 |
| nnU-Net, Mid | 0.8458 | 0.9593 | 0.8407 | 0.7708 | 0.9095 | 0.8743 | 0.6325 | 0.8188 | 0.8694 | 0.8803 | 0.8319 | 0.8843 | 0.8924 |
| nnU-Net, Late | 0.8506 | 0.9610 | 0.8408 | 0.7750 | 0.9136 | 0.8746 | 0.6407 | 0.8370 | 0.8845 | 0.8816 | 0.8299 | 0.8852 | 0.8949 |
| nnU-Net + CBAM, Early | 0.8810 | 0.9672 | 0.8759 | 0.8070 | 0.9297 | 0.8922 | 0.7209 | 0.8707 | 0.9014 | 0.8993 | 0.8729 | 0.9245 | 0.9162 |
| nnU-Net + CBAM, Early-Mid | 0.8805 | 0.9675 | 0.8763 | 0.8048 | 0.9297 | 0.8913 | 0.7160 | 0.8704 | 0.9023 | 0.8990 | 0.8721 | 0.9253 | 0.9171 |
| nnU-Net + CBAM, Mid | 0.8403 | 0.9601 | 0.8458 | 0.7716 | 0.9018 | 0.8734 | 0.6276 | 0.8154 | 0.8444 | 0.8744 | 0.8206 | 0.8798 | 0.8848 |
| nnU-Net + CBAM, Late | 0.8392 | 0.9585 | 0.8404 | 0.7721 | 0.9055 | 0.8711 | 0.6188 | 0.8137 | 0.8559 | 0.8745 | 0.8101 | 0.8768 | 0.8889 |
| SegFormer, Early | 0.8815 | 0.9680 | 0.8749 | 0.8003 | 0.9321 | 0.8885 | 0.7299 | 0.8741 | 0.9034 | 0.8979 | 0.8701 | 0.9261 | 0.9156 |
| SegFormer, Mid | 0.8810 | 0.9675 | 0.8715 | 0.8056 | 0.9302 | 0.8892 | 0.7282 | 0.8745 | 0.9027 | 0.8975 | 0.8691 | 0.9252 | 0.9146 |
| SegFormer, Late | 0.8740 | 0.9652 | 0.8641 | 0.7998 | 0.9264 | 0.8833 | 0.7127 | 0.8655 | 0.8947 | 0.8936 | 0.8634 | 0.9160 | 0.9083 |

Skeleton Dice of the standard-pipeline evaluation on the 293 test cases: the mean over the twelve regions and the Dice of each region. The single-task checkpoints have no skeleton output. Sternum has no ground-truth pixels in the posterior view of any test case. Source: `tables/seg_published.csv`.

## Malignant hotspot detection before filtering

| Checkpoint | Hotspots | Matched | Hotspot sensitivity | False regions | Region precision | False positives per case |
|:---|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 703 | 407 | 0.5789 | 505 | 0.4517 | 1.75 |
| nnU-Net, Early (`nnunet_early`) | 703 | 390 | 0.5548 | 274 | 0.5929 | 0.97 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 703 | 378 | 0.5377 | 204 | 0.6554 | 0.73 |
| nnU-Net, Mid (`nnunet_mid`) | 703 | 415 | 0.5903 | 423 | 0.5018 | 1.48 |
| nnU-Net, Late (`nnunet_late`) | 703 | 395 | 0.5619 | 203 | 0.6639 | 0.71 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 703 | 415 | 0.5903 | 471 | 0.4732 | 1.63 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 703 | 439 | 0.6245 | 367 | 0.5486 | 1.28 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 703 | 435 | 0.6188 | 396 | 0.5269 | 1.37 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 703 | 411 | 0.5846 | 338 | 0.5529 | 1.18 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 703 | 407 | 0.5789 | 270 | 0.6047 | 0.94 |
| SegFormer, single-task (`segformer_single`) | 703 | 448 | 0.6373 | 228 | 0.6667 | 0.81 |
| SegFormer, Early (`segformer_early`) | 703 | 438 | 0.6230 | 203 | 0.6853 | 0.71 |
| SegFormer, Mid (`segformer_mid`) | 703 | 485 | 0.6899 | 273 | 0.6413 | 0.94 |
| SegFormer, Late (`segformer_late`) | 703 | 445 | 0.6330 | 179 | 0.7168 | 0.64 |

UQ run, all predicted regions kept. Source: `tables/filtering_effects.csv` (setting `no_uq`) and `tables/stats_lesion_detection_model_pairs.csv`.

## Benign hotspot detection before filtering

| Checkpoint | Hotspots | Matched | Hotspot sensitivity | False regions | Region precision | False positives per case |
|:---|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 1240 | 622 | 0.5016 | 303 | 0.6752 | 1.06 |
| nnU-Net, Early (`nnunet_early`) | 1240 | 635 | 0.5121 | 286 | 0.6970 | 1.05 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 1240 | 762 | 0.6145 | 420 | 0.6515 | 1.51 |
| nnU-Net, Mid (`nnunet_mid`) | 1240 | 641 | 0.5169 | 380 | 0.6346 | 1.36 |
| nnU-Net, Late (`nnunet_late`) | 1240 | 763 | 0.6153 | 435 | 0.6434 | 1.56 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 1240 | 608 | 0.4903 | 319 | 0.6603 | 1.13 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 1240 | 639 | 0.5153 | 278 | 0.7030 | 1.01 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 1240 | 642 | 0.5177 | 302 | 0.6828 | 1.06 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 1240 | 637 | 0.5137 | 340 | 0.6573 | 1.21 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 1240 | 811 | 0.6540 | 518 | 0.6157 | 1.83 |
| SegFormer, single-task (`segformer_single`) | 1240 | 733 | 0.5911 | 400 | 0.6552 | 1.46 |
| SegFormer, Early (`segformer_early`) | 1240 | 774 | 0.6242 | 408 | 0.6606 | 1.46 |
| SegFormer, Mid (`segformer_mid`) | 1240 | 771 | 0.6218 | 425 | 0.6508 | 1.52 |
| SegFormer, Late (`segformer_late`) | 1240 | 761 | 0.6137 | 403 | 0.6596 | 1.44 |

UQ run, all predicted regions kept. Source: `tables/filtering_effects.csv` (setting `no_uq`) and `tables/stats_lesion_detection_model_pairs.csv`.

## Malignant regions per view

| Checkpoint | Anterior regions | true | false | Posterior regions | true | false | Pooled regions | true | false | False regions per case |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 396 | 178 | 218 | 525 | 238 | 287 | 921 | 416 | 505 | 1.72 |
| nnU-Net, Early (`nnunet_early`) | 335 | 186 | 149 | 338 | 213 | 125 | 673 | 399 | 274 | 0.94 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 299 | 186 | 113 | 293 | 202 | 91 | 592 | 388 | 204 | 0.70 |
| nnU-Net, Mid (`nnunet_mid`) | 455 | 206 | 249 | 394 | 220 | 174 | 849 | 426 | 423 | 1.44 |
| nnU-Net, Late (`nnunet_late`) | 315 | 197 | 118 | 289 | 204 | 85 | 604 | 401 | 203 | 0.69 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 459 | 206 | 253 | 435 | 217 | 218 | 894 | 423 | 471 | 1.61 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 430 | 215 | 215 | 383 | 231 | 152 | 813 | 446 | 367 | 1.25 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 429 | 219 | 210 | 408 | 222 | 186 | 837 | 441 | 396 | 1.35 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 383 | 205 | 178 | 373 | 213 | 160 | 756 | 418 | 338 | 1.15 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 371 | 214 | 157 | 312 | 199 | 113 | 683 | 413 | 270 | 0.92 |
| SegFormer, single-task (`segformer_single`) | 344 | 219 | 125 | 340 | 237 | 103 | 684 | 456 | 228 | 0.78 |
| SegFormer, Early (`segformer_early`) | 321 | 221 | 100 | 324 | 221 | 103 | 645 | 442 | 203 | 0.69 |
| SegFormer, Mid (`segformer_mid`) | 372 | 237 | 135 | 389 | 251 | 138 | 761 | 488 | 273 | 0.93 |
| SegFormer, Late (`segformer_late`) | 314 | 223 | 91 | 318 | 230 | 88 | 632 | 453 | 179 | 0.61 |

UQ run, before filtering. False regions per case is the number of false regions over both views divided by 293. Source: `tables/uq_discrimination_by_config.csv`.

## Benign regions per view

| Checkpoint | Anterior regions | true | false | Posterior regions | true | false | Pooled regions | true | false | False regions per case |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 498 | 351 | 147 | 435 | 279 | 156 | 933 | 630 | 303 | 1.03 |
| nnU-Net, Early (`nnunet_early`) | 539 | 375 | 164 | 405 | 283 | 122 | 944 | 658 | 286 | 0.98 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 789 | 492 | 297 | 416 | 293 | 123 | 1205 | 785 | 420 | 1.43 |
| nnU-Net, Mid (`nnunet_mid`) | 572 | 366 | 206 | 468 | 294 | 174 | 1040 | 660 | 380 | 1.30 |
| nnU-Net, Late (`nnunet_late`) | 812 | 499 | 313 | 408 | 286 | 122 | 1220 | 785 | 435 | 1.48 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 521 | 354 | 167 | 418 | 266 | 152 | 939 | 620 | 319 | 1.09 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 529 | 364 | 165 | 407 | 294 | 113 | 936 | 658 | 278 | 0.95 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 522 | 363 | 159 | 430 | 287 | 143 | 952 | 650 | 302 | 1.03 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 550 | 365 | 185 | 442 | 287 | 155 | 992 | 652 | 340 | 1.16 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 951 | 540 | 411 | 397 | 290 | 107 | 1348 | 830 | 518 | 1.77 |
| SegFormer, single-task (`segformer_single`) | 764 | 474 | 290 | 396 | 286 | 110 | 1160 | 760 | 400 | 1.37 |
| SegFormer, Early (`segformer_early`) | 798 | 502 | 296 | 404 | 292 | 112 | 1202 | 794 | 408 | 1.39 |
| SegFormer, Mid (`segformer_mid`) | 794 | 490 | 304 | 423 | 302 | 121 | 1217 | 792 | 425 | 1.45 |
| SegFormer, Late (`segformer_late`) | 770 | 487 | 283 | 414 | 294 | 120 | 1184 | 781 | 403 | 1.38 |

UQ run, before filtering. False regions per case is the number of false regions over both views divided by 293. Source: `tables/uq_discrimination_by_config.csv`.
