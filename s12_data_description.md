# S12. Data description

BS-80K has 3,247 patients with an anterior and a posterior whole-body scan. 2,925 cases are used, each with both views, stacked as a two-channel image of 1024 x 256 pixels.

## Split

The case identifiers are sorted and shuffled with NumPy `default_rng` and seed 42. The first 80% of the shuffled list is the training split, the next 10% the validation split, and the rest the test split, which gives 2,340, 292, and 293 cases. Both views of a case are in the same split. The assignment of every case is in `tables/split_assignment.csv`.

## Counts per split and view

| Split | View | Cases | Images | Boxes, benign | Boxes, malignant | Images with benign | Images with malignant | Regions, benign | Regions, malignant | Skeleton, manual | Skeleton, predicted |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| train | anterior | 2,340 | 2,340 | 7,146 | 2,540 | 2,105 | 852 | 7,134 | 2,532 | 1,387 | 953 |
| train | posterior | 2,340 | 2,340 | 3,326 | 2,742 | 1,720 | 752 | 3,323 | 2,720 | 1,351 | 989 |
| train | both | 2,340 | 4,680 | 10,472 | 5,282 | 3,825 | 1,604 | 10,457 | 5,252 | 2,738 | 1,942 |
| validation | anterior | 292 | 292 | 901 | 385 | 256 | 103 | 901 | 383 | 176 | 116 |
| validation | posterior | 292 | 292 | 379 | 470 | 203 | 95 | 379 | 466 | 155 | 137 |
| validation | both | 292 | 584 | 1,280 | 855 | 459 | 198 | 1,280 | 849 | 331 | 253 |
| test | anterior | 293 | 293 | 834 | 354 | 259 | 110 | 830 | 353 | 180 | 113 |
| test | posterior | 293 | 293 | 412 | 352 | 214 | 93 | 410 | 350 | 165 | 128 |
| test | both | 293 | 586 | 1,246 | 706 | 473 | 203 | 1,240 | 703 | 345 | 241 |

Boxes are the bounding boxes of BS-80K. Regions are the connected components of the hotspot masks made from the boxes. Skeleton columns count the views by the source of the skeleton mask. An image is one view of a case. Source: `tables/split_counts.csv`.

## Data record of the masks

The hotspot and skeleton masks are published as one data record of five files. The scans are not part of it.

| File | Content |
|:---|:---|
| `hotspot_masks.zip` | 5,462 masks, one for each view with hotspot boxes, pixel values 0 background, 1 benign, 2 malignant |
| `skeleton_masks.zip` | 6,494 masks, one for every view, pixel values 0 background and 1 to 12 for the twelve skeleton regions |
| `manifest.csv` | One row per mask: mask set, patient, study, view, path in the archive, source, split, SHA-256, size in bytes |
| `SHA256SUMS.txt` | SHA-256 of the two archives |
| `README.md` | Pixel values, method, and splits |

Inside the archives a mask is `<mask set>/<patient>/<study>/<view>.png`, 1024 x 256 pixels, 8 bit, aligned with the scan of the same patient, study, and view. The source of a skeleton mask is `manual` or `predicted`, and the split is `train`, `validation`, `test`, or `unused` for the 322 patients that are not among the 2,925 cases. The package is built by `scripts/package_zenodo_record.py`.
