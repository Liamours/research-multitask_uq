# S2. All paired tests

Ninety-one pairs of the fourteen checkpoints, for the malignant and the benign class.

| Comparison | Test | Interval |
|:---|:---|:---|
| Dice of two checkpoints | Wilcoxon signed-rank test on the per-image Dice differences of the images with the class in the ground truth, and a paired t-test. Holm correction over the 91 pairs | Mean difference with a 95% percentile interval from 2000 bootstrap resamples of the 293 test cases, both views of a case kept together |
| Matched hotspots of two checkpoints | Exact McNemar test on the hotspots matched by one checkpoint and not the other. Holm correction over the 91 pairs | - |

Dice in the pair tables is the lesion-bearing Dice of the UQ run unless the heading says standard-pipeline run. Dice is the mean over the test images whose ground truth contains the class (203 malignant, 473 benign), computed on the predictions of the UQ run, one full-image forward pass per view.

## Dice pairs, malignant

| Model A | Model B | Images | Dice A | Dice B | Difference A minus B | 95% interval | A higher / B higher | Wilcoxon p | Holm p | t-test p | t-test Holm p |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nnunet_single` | `nnunet_early` | 203 | 0.4123 | 0.4360 | -0.0237 | [-0.0546, +0.0077] | 65 / 99 | 0.011 | 0.726 | 0.112 | 1.000 |
| `nnunet_single` | `nnunet_earlymid` | 203 | 0.4123 | 0.4208 | -0.0085 | [-0.0369, +0.0193] | 72 / 90 | 0.234 | 1.000 | 0.533 | 1.000 |
| `nnunet_single` | `nnunet_mid` | 203 | 0.4123 | 0.4321 | -0.0198 | [-0.0515, +0.0104] | 79 / 92 | 0.178 | 1.000 | 0.203 | 1.000 |
| `nnunet_single` | `nnunet_late` | 203 | 0.4123 | 0.4304 | -0.0181 | [-0.0507, +0.0147] | 62 / 103 | 0.042 | 1.000 | 0.243 | 1.000 |
| `nnunet_single` | `nnunetcbam_single` | 203 | 0.4123 | 0.4289 | -0.0165 | [-0.0443, +0.0135] | 71 / 96 | 0.163 | 1.000 | 0.285 | 1.000 |
| `nnunet_single` | `nnunetcbam_multidecoder` | 203 | 0.4123 | 0.4765 | -0.0642 | [-0.0943, -0.0332] | 61 / 113 | <0.001 | <0.001 | <0.001 | 0.004 |
| `nnunet_single` | `nnunetcbam_earlymid` | 203 | 0.4123 | 0.4453 | -0.0330 | [-0.0608, -0.0033] | 75 / 89 | 0.008 | 0.586 | 0.019 | 1.000 |
| `nnunet_single` | `nnunetcbam_mid` | 203 | 0.4123 | 0.4407 | -0.0284 | [-0.0605, +0.0047] | 64 / 99 | 0.003 | 0.239 | 0.071 | 1.000 |
| `nnunet_single` | `nnunetcbam_multihead` | 203 | 0.4123 | 0.4506 | -0.0382 | [-0.0691, -0.0051] | 64 / 102 | 0.003 | 0.197 | 0.019 | 1.000 |
| `nnunet_single` | `segformer_single` | 203 | 0.4123 | 0.3705 | +0.0418 | [+0.0021, +0.0855] | 81 / 82 | 0.212 | 1.000 | 0.035 | 1.000 |
| `nnunet_single` | `segformer_early` | 203 | 0.4123 | 0.3825 | +0.0298 | [-0.0103, +0.0698] | 81 / 83 | 0.338 | 1.000 | 0.133 | 1.000 |
| `nnunet_single` | `segformer_mid` | 203 | 0.4123 | 0.3973 | +0.0151 | [-0.0270, +0.0564] | 77 / 87 | 0.845 | 1.000 | 0.449 | 1.000 |
| `nnunet_single` | `segformer_late` | 203 | 0.4123 | 0.3857 | +0.0267 | [-0.0173, +0.0721] | 82 / 82 | 0.681 | 1.000 | 0.194 | 1.000 |
| `nnunet_early` | `nnunet_earlymid` | 203 | 0.4360 | 0.4208 | +0.0152 | [-0.0077, +0.0388] | 88 / 67 | 0.106 | 1.000 | 0.178 | 1.000 |
| `nnunet_early` | `nnunet_mid` | 203 | 0.4360 | 0.4321 | +0.0039 | [-0.0258, +0.0333] | 84 / 86 | 0.743 | 1.000 | 0.784 | 1.000 |
| `nnunet_early` | `nnunetcbam_multidecoder` | 203 | 0.4360 | 0.4765 | -0.0405 | [-0.0714, -0.0105] | 64 / 108 | <0.001 | 0.079 | 0.004 | 0.260 |
| `nnunet_early` | `nnunetcbam_earlymid` | 203 | 0.4360 | 0.4453 | -0.0093 | [-0.0347, +0.0158] | 74 / 87 | 0.468 | 1.000 | 0.431 | 1.000 |
| `nnunet_early` | `nnunetcbam_mid` | 203 | 0.4360 | 0.4407 | -0.0047 | [-0.0317, +0.0236] | 75 / 86 | 0.434 | 1.000 | 0.718 | 1.000 |
| `nnunet_early` | `segformer_early` | 203 | 0.4360 | 0.3825 | +0.0535 | [+0.0134, +0.0928] | 88 / 75 | 0.014 | 0.912 | 0.006 | 0.357 |
| `nnunet_early` | `segformer_mid` | 203 | 0.4360 | 0.3973 | +0.0387 | [+0.0009, +0.0766] | 88 / 77 | 0.067 | 1.000 | 0.039 | 1.000 |
| `nnunet_earlymid` | `nnunet_mid` | 203 | 0.4208 | 0.4321 | -0.0114 | [-0.0451, +0.0203] | 79 / 86 | 0.497 | 1.000 | 0.463 | 1.000 |
| `nnunet_earlymid` | `nnunetcbam_earlymid` | 203 | 0.4208 | 0.4453 | -0.0246 | [-0.0533, +0.0037] | 70 / 89 | 0.048 | 1.000 | 0.079 | 1.000 |
| `nnunet_earlymid` | `nnunetcbam_mid` | 203 | 0.4208 | 0.4407 | -0.0199 | [-0.0524, +0.0109] | 68 / 90 | 0.045 | 1.000 | 0.180 | 1.000 |
| `nnunet_earlymid` | `segformer_mid` | 203 | 0.4208 | 0.3973 | +0.0235 | [-0.0141, +0.0608] | 91 / 72 | 0.182 | 1.000 | 0.196 | 1.000 |
| `nnunet_mid` | `nnunetcbam_mid` | 203 | 0.4321 | 0.4407 | -0.0086 | [-0.0337, +0.0168] | 77 / 84 | 0.160 | 1.000 | 0.479 | 1.000 |
| `nnunet_mid` | `segformer_mid` | 203 | 0.4321 | 0.3973 | +0.0349 | [-0.0050, +0.0781] | 91 / 80 | 0.192 | 1.000 | 0.087 | 1.000 |
| `nnunet_late` | `nnunet_early` | 203 | 0.4304 | 0.4360 | -0.0056 | [-0.0319, +0.0198] | 83 / 81 | 0.937 | 1.000 | 0.647 | 1.000 |
| `nnunet_late` | `nnunet_earlymid` | 203 | 0.4304 | 0.4208 | +0.0096 | [-0.0164, +0.0364] | 91 / 65 | 0.101 | 1.000 | 0.462 | 1.000 |
| `nnunet_late` | `nnunet_mid` | 203 | 0.4304 | 0.4321 | -0.0017 | [-0.0271, +0.0230] | 84 / 79 | 0.703 | 1.000 | 0.888 | 1.000 |
| `nnunet_late` | `nnunetcbam_multidecoder` | 203 | 0.4304 | 0.4765 | -0.0461 | [-0.0738, -0.0206] | 66 / 98 | 0.004 | 0.319 | <0.001 | 0.047 |
| `nnunet_late` | `nnunetcbam_earlymid` | 203 | 0.4304 | 0.4453 | -0.0149 | [-0.0384, +0.0088] | 75 / 80 | 0.404 | 1.000 | 0.184 | 1.000 |
| `nnunet_late` | `nnunetcbam_mid` | 203 | 0.4304 | 0.4407 | -0.0103 | [-0.0359, +0.0152] | 79 / 79 | 0.690 | 1.000 | 0.401 | 1.000 |
| `nnunet_late` | `nnunetcbam_multihead` | 203 | 0.4304 | 0.4506 | -0.0202 | [-0.0438, +0.0021] | 71 / 84 | 0.124 | 1.000 | 0.076 | 1.000 |
| `nnunet_late` | `segformer_early` | 203 | 0.4304 | 0.3825 | +0.0479 | [+0.0117, +0.0842] | 88 / 71 | 0.023 | 1.000 | 0.011 | 0.664 |
| `nnunet_late` | `segformer_mid` | 203 | 0.4304 | 0.3973 | +0.0332 | [-0.0050, +0.0721] | 92 / 69 | 0.105 | 1.000 | 0.086 | 1.000 |
| `nnunet_late` | `segformer_late` | 203 | 0.4304 | 0.3857 | +0.0448 | [+0.0083, +0.0830] | 92 / 67 | 0.081 | 1.000 | 0.020 | 1.000 |
| `nnunetcbam_single` | `nnunet_early` | 203 | 0.4289 | 0.4360 | -0.0071 | [-0.0316, +0.0184] | 76 / 89 | 0.350 | 1.000 | 0.577 | 1.000 |
| `nnunetcbam_single` | `nnunet_earlymid` | 203 | 0.4289 | 0.4208 | +0.0081 | [-0.0196, +0.0352] | 86 / 78 | 0.613 | 1.000 | 0.555 | 1.000 |
| `nnunetcbam_single` | `nnunet_mid` | 203 | 0.4289 | 0.4321 | -0.0033 | [-0.0291, +0.0209] | 80 / 86 | 0.589 | 1.000 | 0.802 | 1.000 |
| `nnunetcbam_single` | `nnunet_late` | 203 | 0.4289 | 0.4304 | -0.0016 | [-0.0271, +0.0235] | 76 / 85 | 0.367 | 1.000 | 0.906 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_multidecoder` | 203 | 0.4289 | 0.4765 | -0.0477 | [-0.0751, -0.0234] | 62 / 106 | <0.001 | <0.001 | <0.001 | 0.011 |
| `nnunetcbam_single` | `nnunetcbam_earlymid` | 203 | 0.4289 | 0.4453 | -0.0165 | [-0.0360, +0.0034] | 64 / 94 | 0.025 | 1.000 | 0.110 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_mid` | 203 | 0.4289 | 0.4407 | -0.0119 | [-0.0338, +0.0121] | 62 / 96 | 0.034 | 1.000 | 0.306 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_multihead` | 203 | 0.4289 | 0.4506 | -0.0217 | [-0.0458, +0.0038] | 63 / 98 | 0.004 | 0.319 | 0.076 | 1.000 |
| `nnunetcbam_single` | `segformer_single` | 203 | 0.4289 | 0.3705 | +0.0584 | [+0.0221, +0.0965] | 85 / 78 | 0.034 | 1.000 | 0.002 | 0.111 |
| `nnunetcbam_single` | `segformer_early` | 203 | 0.4289 | 0.3825 | +0.0464 | [+0.0104, +0.0820] | 82 / 82 | 0.066 | 1.000 | 0.013 | 0.738 |
| `nnunetcbam_single` | `segformer_mid` | 203 | 0.4289 | 0.3973 | +0.0316 | [-0.0043, +0.0702] | 83 / 81 | 0.359 | 1.000 | 0.093 | 1.000 |
| `nnunetcbam_single` | `segformer_late` | 203 | 0.4289 | 0.3857 | +0.0432 | [+0.0070, +0.0812] | 83 / 81 | 0.192 | 1.000 | 0.024 | 1.000 |
| `nnunetcbam_multidecoder` | `nnunet_earlymid` | 203 | 0.4765 | 0.4208 | +0.0558 | [+0.0243, +0.0888] | 101 / 68 | <0.001 | 0.031 | <0.001 | 0.034 |
| `nnunetcbam_multidecoder` | `nnunet_mid` | 203 | 0.4765 | 0.4321 | +0.0444 | [+0.0166, +0.0718] | 107 / 62 | <0.001 | 0.033 | 0.002 | 0.127 |
| `nnunetcbam_multidecoder` | `nnunetcbam_earlymid` | 203 | 0.4765 | 0.4453 | +0.0312 | [+0.0119, +0.0535] | 92 / 69 | 0.007 | 0.521 | 0.003 | 0.203 |
| `nnunetcbam_multidecoder` | `nnunetcbam_mid` | 203 | 0.4765 | 0.4407 | +0.0358 | [+0.0138, +0.0616] | 90 / 75 | 0.033 | 1.000 | 0.002 | 0.128 |
| `nnunetcbam_multidecoder` | `segformer_early` | 203 | 0.4765 | 0.3825 | +0.0940 | [+0.0566, +0.1330] | 103 / 66 | <0.001 | 0.003 | <0.001 | <0.001 |
| `nnunetcbam_multidecoder` | `segformer_mid` | 203 | 0.4765 | 0.3973 | +0.0793 | [+0.0378, +0.1217] | 104 / 69 | <0.001 | 0.027 | <0.001 | 0.009 |
| `nnunetcbam_earlymid` | `nnunet_mid` | 203 | 0.4453 | 0.4321 | +0.0132 | [-0.0116, +0.0379] | 88 / 74 | 0.221 | 1.000 | 0.278 | 1.000 |
| `nnunetcbam_earlymid` | `nnunetcbam_mid` | 203 | 0.4453 | 0.4407 | +0.0046 | [-0.0112, +0.0222] | 78 / 75 | 0.975 | 1.000 | 0.595 | 1.000 |
| `nnunetcbam_earlymid` | `segformer_mid` | 203 | 0.4453 | 0.3973 | +0.0481 | [+0.0111, +0.0860] | 88 / 75 | 0.064 | 1.000 | 0.010 | 0.609 |
| `nnunetcbam_mid` | `segformer_mid` | 203 | 0.4407 | 0.3973 | +0.0435 | [+0.0063, +0.0817] | 91 / 72 | 0.070 | 1.000 | 0.021 | 1.000 |
| `nnunetcbam_multihead` | `nnunet_early` | 203 | 0.4506 | 0.4360 | +0.0146 | [-0.0126, +0.0419] | 86 / 77 | 0.185 | 1.000 | 0.264 | 1.000 |
| `nnunetcbam_multihead` | `nnunet_earlymid` | 203 | 0.4506 | 0.4208 | +0.0298 | [+0.0012, +0.0592] | 88 / 69 | 0.031 | 1.000 | 0.038 | 1.000 |
| `nnunetcbam_multihead` | `nnunet_mid` | 203 | 0.4506 | 0.4321 | +0.0184 | [-0.0080, +0.0459] | 95 / 71 | 0.053 | 1.000 | 0.174 | 1.000 |
| `nnunetcbam_multihead` | `nnunetcbam_multidecoder` | 203 | 0.4506 | 0.4765 | -0.0260 | [-0.0506, -0.0031] | 77 / 87 | 0.286 | 1.000 | 0.024 | 1.000 |
| `nnunetcbam_multihead` | `nnunetcbam_earlymid` | 203 | 0.4506 | 0.4453 | +0.0052 | [-0.0131, +0.0236] | 91 / 67 | 0.080 | 1.000 | 0.594 | 1.000 |
| `nnunetcbam_multihead` | `nnunetcbam_mid` | 203 | 0.4506 | 0.4407 | +0.0098 | [-0.0060, +0.0278] | 81 / 75 | 0.338 | 1.000 | 0.269 | 1.000 |
| `nnunetcbam_multihead` | `segformer_early` | 203 | 0.4506 | 0.3825 | +0.0681 | [+0.0330, +0.1028] | 89 / 72 | 0.001 | 0.113 | <0.001 | 0.024 |
| `nnunetcbam_multihead` | `segformer_mid` | 203 | 0.4506 | 0.3973 | +0.0533 | [+0.0167, +0.0911] | 90 / 73 | 0.012 | 0.802 | 0.005 | 0.327 |
| `nnunetcbam_multihead` | `segformer_late` | 203 | 0.4506 | 0.3857 | +0.0649 | [+0.0296, +0.1015] | 90 / 71 | 0.002 | 0.177 | <0.001 | 0.056 |
| `segformer_single` | `nnunet_early` | 203 | 0.3705 | 0.4360 | -0.0655 | [-0.1070, -0.0262] | 72 / 92 | 0.003 | 0.203 | <0.001 | 0.039 |
| `segformer_single` | `nnunet_earlymid` | 203 | 0.3705 | 0.4208 | -0.0503 | [-0.0866, -0.0151] | 77 / 81 | 0.045 | 1.000 | 0.004 | 0.266 |
| `segformer_single` | `nnunet_mid` | 203 | 0.3705 | 0.4321 | -0.0617 | [-0.1042, -0.0242] | 72 / 92 | 0.010 | 0.699 | <0.001 | 0.070 |
| `segformer_single` | `nnunet_late` | 203 | 0.3705 | 0.4304 | -0.0599 | [-0.0976, -0.0251] | 61 / 96 | 0.003 | 0.200 | <0.001 | 0.070 |
| `segformer_single` | `nnunetcbam_multidecoder` | 203 | 0.3705 | 0.4765 | -0.1061 | [-0.1483, -0.0662] | 63 / 106 | <0.001 | <0.001 | <0.001 | <0.001 |
| `segformer_single` | `nnunetcbam_earlymid` | 203 | 0.3705 | 0.4453 | -0.0749 | [-0.1129, -0.0385] | 68 / 92 | 0.001 | 0.113 | <0.001 | 0.006 |
| `segformer_single` | `nnunetcbam_mid` | 203 | 0.3705 | 0.4407 | -0.0702 | [-0.1097, -0.0333] | 70 / 87 | 0.003 | 0.203 | <0.001 | 0.014 |
| `segformer_single` | `nnunetcbam_multihead` | 203 | 0.3705 | 0.4506 | -0.0801 | [-0.1182, -0.0436] | 65 / 94 | <0.001 | 0.014 | <0.001 | 0.001 |
| `segformer_single` | `segformer_early` | 203 | 0.3705 | 0.3825 | -0.0120 | [-0.0364, +0.0100] | 71 / 76 | 0.747 | 1.000 | 0.304 | 1.000 |
| `segformer_single` | `segformer_mid` | 203 | 0.3705 | 0.3973 | -0.0268 | [-0.0519, -0.0008] | 67 / 84 | 0.038 | 1.000 | 0.038 | 1.000 |
| `segformer_single` | `segformer_late` | 203 | 0.3705 | 0.3857 | -0.0152 | [-0.0399, +0.0093] | 67 / 81 | 0.196 | 1.000 | 0.229 | 1.000 |
| `segformer_early` | `nnunet_earlymid` | 203 | 0.3825 | 0.4208 | -0.0383 | [-0.0766, +0.0004] | 74 / 86 | 0.122 | 1.000 | 0.041 | 1.000 |
| `segformer_early` | `nnunet_mid` | 203 | 0.3825 | 0.4321 | -0.0497 | [-0.0879, -0.0118] | 76 / 91 | 0.089 | 1.000 | 0.010 | 0.637 |
| `segformer_early` | `nnunetcbam_earlymid` | 203 | 0.3825 | 0.4453 | -0.0629 | [-0.0972, -0.0274] | 74 / 86 | 0.011 | 0.755 | <0.001 | 0.063 |
| `segformer_early` | `nnunetcbam_mid` | 203 | 0.3825 | 0.4407 | -0.0582 | [-0.0948, -0.0212] | 76 / 85 | 0.022 | 1.000 | 0.002 | 0.142 |
| `segformer_early` | `segformer_mid` | 203 | 0.3825 | 0.3973 | -0.0148 | [-0.0362, +0.0076] | 69 / 76 | 0.312 | 1.000 | 0.186 | 1.000 |
| `segformer_late` | `nnunet_early` | 203 | 0.3857 | 0.4360 | -0.0503 | [-0.0917, -0.0105] | 74 / 89 | 0.035 | 1.000 | 0.009 | 0.552 |
| `segformer_late` | `nnunet_earlymid` | 203 | 0.3857 | 0.4208 | -0.0351 | [-0.0713, +0.0008] | 77 / 84 | 0.165 | 1.000 | 0.061 | 1.000 |
| `segformer_late` | `nnunet_mid` | 203 | 0.3857 | 0.4321 | -0.0465 | [-0.0895, -0.0055] | 83 / 87 | 0.118 | 1.000 | 0.022 | 1.000 |
| `segformer_late` | `nnunetcbam_multidecoder` | 203 | 0.3857 | 0.4765 | -0.0909 | [-0.1328, -0.0491] | 70 / 103 | <0.001 | 0.018 | <0.001 | 0.001 |
| `segformer_late` | `nnunetcbam_earlymid` | 203 | 0.3857 | 0.4453 | -0.0597 | [-0.0967, -0.0228] | 71 / 90 | 0.014 | 0.912 | 0.002 | 0.120 |
| `segformer_late` | `nnunetcbam_mid` | 203 | 0.3857 | 0.4407 | -0.0551 | [-0.0934, -0.0173] | 72 / 90 | 0.024 | 1.000 | 0.004 | 0.272 |
| `segformer_late` | `segformer_early` | 203 | 0.3857 | 0.3825 | +0.0032 | [-0.0208, +0.0271] | 77 / 66 | 0.498 | 1.000 | 0.788 | 1.000 |
| `segformer_late` | `segformer_mid` | 203 | 0.3857 | 0.3973 | -0.0116 | [-0.0302, +0.0079] | 66 / 77 | 0.535 | 1.000 | 0.229 | 1.000 |

After Holm correction 9 of 91 pairs are significant under the Wilcoxon test and 13 under the t-test (p below 0.05).

## Dice pairs, benign

| Model A | Model B | Images | Dice A | Dice B | Difference A minus B | 95% interval | A higher / B higher | Wilcoxon p | Holm p | t-test p | t-test Holm p |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `nnunet_single` | `nnunet_early` | 473 | 0.5288 | 0.5287 | +0.0000 | [-0.0088, +0.0089] | 217 / 215 | 0.545 | 1.000 | 0.991 | 1.000 |
| `nnunet_single` | `nnunet_earlymid` | 473 | 0.5288 | 0.5418 | -0.0131 | [-0.0250, -0.0022] | 220 / 218 | 0.545 | 1.000 | 0.020 | 1.000 |
| `nnunet_single` | `nnunet_mid` | 473 | 0.5288 | 0.5232 | +0.0056 | [-0.0026, +0.0132] | 234 / 190 | 0.005 | 0.268 | 0.178 | 1.000 |
| `nnunet_single` | `nnunet_late` | 473 | 0.5288 | 0.5472 | -0.0185 | [-0.0328, -0.0058] | 199 / 246 | 0.003 | 0.164 | 0.006 | 0.423 |
| `nnunet_single` | `nnunetcbam_single` | 473 | 0.5288 | 0.5220 | +0.0067 | [-0.0017, +0.0150] | 243 / 179 | 0.006 | 0.335 | 0.124 | 1.000 |
| `nnunet_single` | `nnunetcbam_multidecoder` | 473 | 0.5288 | 0.5390 | -0.0102 | [-0.0200, -0.0009] | 173 / 251 | <0.001 | 0.047 | 0.032 | 1.000 |
| `nnunet_single` | `nnunetcbam_earlymid` | 473 | 0.5288 | 0.5347 | -0.0059 | [-0.0157, +0.0036] | 201 / 223 | 0.153 | 1.000 | 0.229 | 1.000 |
| `nnunet_single` | `nnunetcbam_mid` | 473 | 0.5288 | 0.5286 | +0.0002 | [-0.0089, +0.0090] | 210 / 211 | 0.716 | 1.000 | 0.968 | 1.000 |
| `nnunet_single` | `nnunetcbam_multihead` | 473 | 0.5288 | 0.5486 | -0.0199 | [-0.0340, -0.0070] | 194 / 253 | 0.002 | 0.142 | 0.003 | 0.200 |
| `nnunet_single` | `segformer_single` | 473 | 0.5288 | 0.5319 | -0.0031 | [-0.0231, +0.0166] | 193 / 254 | 0.090 | 1.000 | 0.744 | 1.000 |
| `nnunet_single` | `segformer_early` | 473 | 0.5288 | 0.5498 | -0.0211 | [-0.0407, -0.0008] | 194 / 255 | 0.007 | 0.360 | 0.025 | 1.000 |
| `nnunet_single` | `segformer_mid` | 473 | 0.5288 | 0.5451 | -0.0163 | [-0.0361, +0.0039] | 199 / 256 | 0.024 | 1.000 | 0.091 | 1.000 |
| `nnunet_single` | `segformer_late` | 473 | 0.5288 | 0.5473 | -0.0185 | [-0.0371, +0.0015] | 193 / 261 | 0.002 | 0.138 | 0.044 | 1.000 |
| `nnunet_early` | `nnunet_earlymid` | 473 | 0.5287 | 0.5418 | -0.0131 | [-0.0226, -0.0035] | 222 / 219 | 0.294 | 1.000 | 0.007 | 0.474 |
| `nnunet_early` | `nnunet_mid` | 473 | 0.5287 | 0.5232 | +0.0055 | [-0.0019, +0.0129] | 246 / 182 | 0.003 | 0.177 | 0.139 | 1.000 |
| `nnunet_early` | `nnunetcbam_multidecoder` | 473 | 0.5287 | 0.5390 | -0.0103 | [-0.0172, -0.0031] | 169 / 257 | <0.001 | 0.001 | 0.003 | 0.196 |
| `nnunet_early` | `nnunetcbam_earlymid` | 473 | 0.5287 | 0.5347 | -0.0059 | [-0.0132, +0.0013] | 207 / 223 | 0.050 | 1.000 | 0.089 | 1.000 |
| `nnunet_early` | `nnunetcbam_mid` | 473 | 0.5287 | 0.5286 | +0.0001 | [-0.0075, +0.0076] | 193 / 237 | 0.174 | 1.000 | 0.971 | 1.000 |
| `nnunet_early` | `segformer_early` | 473 | 0.5287 | 0.5498 | -0.0211 | [-0.0391, -0.0015] | 189 / 261 | 0.002 | 0.125 | 0.018 | 1.000 |
| `nnunet_early` | `segformer_mid` | 473 | 0.5287 | 0.5451 | -0.0164 | [-0.0350, +0.0035] | 196 / 257 | 0.011 | 0.569 | 0.073 | 1.000 |
| `nnunet_earlymid` | `nnunet_mid` | 473 | 0.5418 | 0.5232 | +0.0186 | [+0.0094, +0.0286] | 256 / 185 | <0.001 | 0.013 | <0.001 | 0.015 |
| `nnunet_earlymid` | `nnunetcbam_earlymid` | 473 | 0.5418 | 0.5347 | +0.0072 | [-0.0034, +0.0178] | 198 / 241 | 0.274 | 1.000 | 0.188 | 1.000 |
| `nnunet_earlymid` | `nnunetcbam_mid` | 473 | 0.5418 | 0.5286 | +0.0132 | [+0.0026, +0.0246] | 218 / 217 | 0.612 | 1.000 | 0.018 | 1.000 |
| `nnunet_earlymid` | `segformer_mid` | 473 | 0.5418 | 0.5451 | -0.0033 | [-0.0213, +0.0159] | 206 / 251 | 0.084 | 1.000 | 0.716 | 1.000 |
| `nnunet_mid` | `nnunetcbam_mid` | 473 | 0.5232 | 0.5286 | -0.0054 | [-0.0129, +0.0026] | 181 / 243 | <0.001 | 0.044 | 0.176 | 1.000 |
| `nnunet_mid` | `segformer_mid` | 473 | 0.5232 | 0.5451 | -0.0219 | [-0.0412, -0.0013] | 188 / 266 | <0.001 | 0.068 | 0.022 | 1.000 |
| `nnunet_late` | `nnunet_early` | 473 | 0.5472 | 0.5287 | +0.0185 | [+0.0079, +0.0300] | 260 / 184 | <0.001 | 0.004 | <0.001 | 0.067 |
| `nnunet_late` | `nnunet_earlymid` | 473 | 0.5472 | 0.5418 | +0.0054 | [-0.0044, +0.0148] | 263 / 180 | <0.001 | 0.027 | 0.291 | 1.000 |
| `nnunet_late` | `nnunet_mid` | 473 | 0.5472 | 0.5232 | +0.0240 | [+0.0121, +0.0361] | 274 / 168 | <0.001 | <0.001 | <0.001 | 0.011 |
| `nnunet_late` | `nnunetcbam_multidecoder` | 473 | 0.5472 | 0.5390 | +0.0082 | [-0.0022, +0.0199] | 222 / 221 | 0.469 | 1.000 | 0.152 | 1.000 |
| `nnunet_late` | `nnunetcbam_earlymid` | 473 | 0.5472 | 0.5347 | +0.0126 | [+0.0017, +0.0244] | 230 / 210 | 0.039 | 1.000 | 0.029 | 1.000 |
| `nnunet_late` | `nnunetcbam_mid` | 473 | 0.5472 | 0.5286 | +0.0186 | [+0.0081, +0.0310] | 245 / 199 | 0.002 | 0.139 | 0.001 | 0.112 |
| `nnunet_late` | `nnunetcbam_multihead` | 473 | 0.5472 | 0.5486 | -0.0014 | [-0.0089, +0.0065] | 221 / 220 | 0.949 | 1.000 | 0.711 | 1.000 |
| `nnunet_late` | `segformer_early` | 473 | 0.5472 | 0.5498 | -0.0026 | [-0.0179, +0.0143] | 227 / 224 | 0.930 | 1.000 | 0.739 | 1.000 |
| `nnunet_late` | `segformer_mid` | 473 | 0.5472 | 0.5451 | +0.0021 | [-0.0138, +0.0198] | 222 / 232 | 0.971 | 1.000 | 0.800 | 1.000 |
| `nnunet_late` | `segformer_late` | 473 | 0.5472 | 0.5473 | -0.0000 | [-0.0155, +0.0155] | 226 / 225 | 0.748 | 1.000 | 0.995 | 1.000 |
| `nnunetcbam_single` | `nnunet_early` | 473 | 0.5220 | 0.5287 | -0.0067 | [-0.0154, +0.0017] | 188 / 241 | 0.021 | 1.000 | 0.116 | 1.000 |
| `nnunetcbam_single` | `nnunet_earlymid` | 473 | 0.5220 | 0.5418 | -0.0198 | [-0.0315, -0.0081] | 194 / 242 | 0.005 | 0.292 | <0.001 | 0.058 |
| `nnunetcbam_single` | `nnunet_mid` | 473 | 0.5220 | 0.5232 | -0.0012 | [-0.0094, +0.0067] | 221 / 205 | 0.440 | 1.000 | 0.778 | 1.000 |
| `nnunetcbam_single` | `nnunet_late` | 473 | 0.5220 | 0.5472 | -0.0252 | [-0.0381, -0.0128] | 170 / 275 | <0.001 | <0.001 | <0.001 | 0.011 |
| `nnunetcbam_single` | `nnunetcbam_multidecoder` | 473 | 0.5220 | 0.5390 | -0.0170 | [-0.0244, -0.0096] | 151 / 274 | <0.001 | <0.001 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunetcbam_earlymid` | 473 | 0.5220 | 0.5347 | -0.0126 | [-0.0195, -0.0056] | 170 / 249 | <0.001 | <0.001 | <0.001 | 0.041 |
| `nnunetcbam_single` | `nnunetcbam_mid` | 473 | 0.5220 | 0.5286 | -0.0065 | [-0.0139, +0.0009] | 180 / 241 | 0.003 | 0.164 | 0.072 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_multihead` | 473 | 0.5220 | 0.5486 | -0.0266 | [-0.0391, -0.0156] | 178 / 262 | <0.001 | <0.001 | <0.001 | <0.001 |
| `nnunetcbam_single` | `segformer_single` | 473 | 0.5220 | 0.5319 | -0.0098 | [-0.0299, +0.0100] | 187 / 257 | 0.005 | 0.288 | 0.303 | 1.000 |
| `nnunetcbam_single` | `segformer_early` | 473 | 0.5220 | 0.5498 | -0.0278 | [-0.0466, -0.0075] | 184 / 262 | <0.001 | 0.006 | 0.003 | 0.226 |
| `nnunetcbam_single` | `segformer_mid` | 473 | 0.5220 | 0.5451 | -0.0231 | [-0.0427, -0.0023] | 191 / 261 | 0.001 | 0.086 | 0.015 | 1.000 |
| `nnunetcbam_single` | `segformer_late` | 473 | 0.5220 | 0.5473 | -0.0252 | [-0.0439, -0.0059] | 184 / 267 | <0.001 | 0.002 | 0.005 | 0.360 |
| `nnunetcbam_multidecoder` | `nnunet_earlymid` | 473 | 0.5390 | 0.5418 | -0.0028 | [-0.0132, +0.0076] | 252 / 188 | 0.050 | 1.000 | 0.594 | 1.000 |
| `nnunetcbam_multidecoder` | `nnunet_mid` | 473 | 0.5390 | 0.5232 | +0.0158 | [+0.0078, +0.0234] | 270 / 152 | <0.001 | <0.001 | <0.001 | 0.006 |
| `nnunetcbam_multidecoder` | `nnunetcbam_earlymid` | 473 | 0.5390 | 0.5347 | +0.0043 | [-0.0001, +0.0088] | 230 / 191 | 0.008 | 0.400 | 0.057 | 1.000 |
| `nnunetcbam_multidecoder` | `nnunetcbam_mid` | 473 | 0.5390 | 0.5286 | +0.0104 | [+0.0047, +0.0160] | 253 / 165 | <0.001 | <0.001 | <0.001 | 0.035 |
| `nnunetcbam_multidecoder` | `segformer_early` | 473 | 0.5390 | 0.5498 | -0.0108 | [-0.0289, +0.0078] | 209 / 237 | 0.172 | 1.000 | 0.218 | 1.000 |
| `nnunetcbam_multidecoder` | `segformer_mid` | 473 | 0.5390 | 0.5451 | -0.0061 | [-0.0243, +0.0128] | 215 / 235 | 0.367 | 1.000 | 0.495 | 1.000 |
| `nnunetcbam_earlymid` | `nnunet_mid` | 473 | 0.5347 | 0.5232 | +0.0114 | [+0.0043, +0.0184] | 260 / 165 | <0.001 | <0.001 | 0.002 | 0.160 |
| `nnunetcbam_earlymid` | `nnunetcbam_mid` | 473 | 0.5347 | 0.5286 | +0.0061 | [+0.0000, +0.0119] | 231 / 189 | 0.052 | 1.000 | 0.036 | 1.000 |
| `nnunetcbam_earlymid` | `segformer_mid` | 473 | 0.5347 | 0.5451 | -0.0105 | [-0.0289, +0.0093] | 219 / 233 | 0.148 | 1.000 | 0.246 | 1.000 |
| `nnunetcbam_mid` | `segformer_mid` | 473 | 0.5286 | 0.5451 | -0.0165 | [-0.0364, +0.0039] | 201 / 250 | 0.026 | 1.000 | 0.080 | 1.000 |
| `nnunetcbam_multihead` | `nnunet_early` | 473 | 0.5486 | 0.5287 | +0.0199 | [+0.0093, +0.0313] | 261 / 184 | <0.001 | 0.010 | <0.001 | 0.056 |
| `nnunetcbam_multihead` | `nnunet_earlymid` | 473 | 0.5486 | 0.5418 | +0.0068 | [-0.0018, +0.0158] | 255 / 192 | <0.001 | 0.034 | 0.160 | 1.000 |
| `nnunetcbam_multihead` | `nnunet_mid` | 473 | 0.5486 | 0.5232 | +0.0254 | [+0.0144, +0.0377] | 279 / 167 | <0.001 | <0.001 | <0.001 | 0.004 |
| `nnunetcbam_multihead` | `nnunetcbam_multidecoder` | 473 | 0.5486 | 0.5390 | +0.0096 | [+0.0001, +0.0197] | 218 / 219 | 0.293 | 1.000 | 0.082 | 1.000 |
| `nnunetcbam_multihead` | `nnunetcbam_earlymid` | 473 | 0.5486 | 0.5347 | +0.0140 | [+0.0041, +0.0254] | 240 / 204 | 0.026 | 1.000 | 0.012 | 0.802 |
| `nnunetcbam_multihead` | `nnunetcbam_mid` | 473 | 0.5486 | 0.5286 | +0.0201 | [+0.0104, +0.0314] | 260 / 183 | <0.001 | 0.036 | <0.001 | 0.017 |
| `nnunetcbam_multihead` | `segformer_early` | 473 | 0.5486 | 0.5498 | -0.0012 | [-0.0166, +0.0156] | 219 / 231 | 0.753 | 1.000 | 0.879 | 1.000 |
| `nnunetcbam_multihead` | `segformer_mid` | 473 | 0.5486 | 0.5451 | +0.0035 | [-0.0128, +0.0209] | 220 / 235 | 0.773 | 1.000 | 0.663 | 1.000 |
| `nnunetcbam_multihead` | `segformer_late` | 473 | 0.5486 | 0.5473 | +0.0014 | [-0.0137, +0.0173] | 219 / 234 | 0.674 | 1.000 | 0.857 | 1.000 |
| `segformer_single` | `nnunet_early` | 473 | 0.5319 | 0.5287 | +0.0032 | [-0.0163, +0.0219] | 241 / 207 | 0.071 | 1.000 | 0.732 | 1.000 |
| `segformer_single` | `nnunet_earlymid` | 473 | 0.5319 | 0.5418 | -0.0100 | [-0.0294, +0.0082] | 234 / 216 | 0.478 | 1.000 | 0.286 | 1.000 |
| `segformer_single` | `nnunet_mid` | 473 | 0.5319 | 0.5232 | +0.0087 | [-0.0114, +0.0284] | 258 / 188 | 0.007 | 0.360 | 0.368 | 1.000 |
| `segformer_single` | `nnunet_late` | 473 | 0.5319 | 0.5472 | -0.0153 | [-0.0323, +0.0008] | 217 / 234 | 0.362 | 1.000 | 0.069 | 1.000 |
| `segformer_single` | `nnunetcbam_multidecoder` | 473 | 0.5319 | 0.5390 | -0.0071 | [-0.0259, +0.0113] | 233 / 209 | 0.699 | 1.000 | 0.429 | 1.000 |
| `segformer_single` | `nnunetcbam_earlymid` | 473 | 0.5319 | 0.5347 | -0.0028 | [-0.0217, +0.0159] | 231 / 213 | 0.357 | 1.000 | 0.762 | 1.000 |
| `segformer_single` | `nnunetcbam_mid` | 473 | 0.5319 | 0.5286 | +0.0033 | [-0.0162, +0.0230] | 253 / 192 | 0.082 | 1.000 | 0.725 | 1.000 |
| `segformer_single` | `nnunetcbam_multihead` | 473 | 0.5319 | 0.5486 | -0.0168 | [-0.0337, -0.0016] | 221 / 228 | 0.293 | 1.000 | 0.043 | 1.000 |
| `segformer_single` | `segformer_early` | 473 | 0.5319 | 0.5498 | -0.0180 | [-0.0296, -0.0057] | 217 / 214 | 0.077 | 1.000 | 0.002 | 0.144 |
| `segformer_single` | `segformer_mid` | 473 | 0.5319 | 0.5451 | -0.0132 | [-0.0259, -0.0006] | 214 / 225 | 0.196 | 1.000 | 0.030 | 1.000 |
| `segformer_single` | `segformer_late` | 473 | 0.5319 | 0.5473 | -0.0154 | [-0.0276, -0.0034] | 223 / 215 | 0.424 | 1.000 | 0.008 | 0.565 |
| `segformer_early` | `nnunet_earlymid` | 473 | 0.5498 | 0.5418 | +0.0080 | [-0.0108, +0.0257] | 248 / 205 | 0.034 | 1.000 | 0.362 | 1.000 |
| `segformer_early` | `nnunet_mid` | 473 | 0.5498 | 0.5232 | +0.0266 | [+0.0065, +0.0458] | 259 / 190 | <0.001 | 0.021 | 0.005 | 0.358 |
| `segformer_early` | `nnunetcbam_earlymid` | 473 | 0.5498 | 0.5347 | +0.0152 | [-0.0041, +0.0337] | 244 / 203 | 0.030 | 1.000 | 0.085 | 1.000 |
| `segformer_early` | `nnunetcbam_mid` | 473 | 0.5498 | 0.5286 | +0.0213 | [+0.0011, +0.0408] | 247 / 200 | 0.007 | 0.360 | 0.021 | 1.000 |
| `segformer_early` | `segformer_mid` | 473 | 0.5498 | 0.5451 | +0.0047 | [-0.0042, +0.0139] | 212 / 228 | 0.628 | 1.000 | 0.282 | 1.000 |
| `segformer_late` | `nnunet_early` | 473 | 0.5473 | 0.5287 | +0.0185 | [-0.0007, +0.0365] | 264 / 188 | <0.001 | 0.060 | 0.033 | 1.000 |
| `segformer_late` | `nnunet_earlymid` | 473 | 0.5473 | 0.5418 | +0.0054 | [-0.0129, +0.0230] | 257 / 200 | 0.017 | 0.824 | 0.533 | 1.000 |
| `segformer_late` | `nnunet_mid` | 473 | 0.5473 | 0.5232 | +0.0241 | [+0.0044, +0.0425] | 264 / 187 | <0.001 | 0.004 | 0.008 | 0.557 |
| `segformer_late` | `nnunetcbam_multidecoder` | 473 | 0.5473 | 0.5390 | +0.0083 | [-0.0099, +0.0258] | 236 / 214 | 0.103 | 1.000 | 0.327 | 1.000 |
| `segformer_late` | `nnunetcbam_earlymid` | 473 | 0.5473 | 0.5347 | +0.0126 | [-0.0061, +0.0303] | 242 / 209 | 0.025 | 1.000 | 0.140 | 1.000 |
| `segformer_late` | `nnunetcbam_mid` | 473 | 0.5473 | 0.5286 | +0.0187 | [-0.0010, +0.0375] | 258 / 191 | 0.002 | 0.145 | 0.036 | 1.000 |
| `segformer_late` | `segformer_early` | 473 | 0.5473 | 0.5498 | -0.0026 | [-0.0118, +0.0069] | 210 / 227 | 0.215 | 1.000 | 0.579 | 1.000 |
| `segformer_late` | `segformer_mid` | 473 | 0.5473 | 0.5451 | +0.0021 | [-0.0073, +0.0114] | 201 / 236 | 0.645 | 1.000 | 0.648 | 1.000 |

After Holm correction 22 of 91 pairs are significant under the Wilcoxon test and 10 under the t-test (p below 0.05).

Standard-pipeline run, malignant: 7 of 91 pairs are significant after Holm correction under the Wilcoxon test and 9 under the t-test. The full table is `tables/stats_dice_model_pairs_published_run.csv`.

Standard-pipeline run, benign: 13 of 91 pairs are significant after Holm correction under the Wilcoxon test and 8 under the t-test. The full table is `tables/stats_dice_model_pairs_published_run.csv`.

## Matched hotspots, malignant

| Model A | Model B | Hotspots | Matched by A | Matched by B | Only A | Only B | McNemar p | Holm p |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| `nnunet_single` | `nnunet_early` | 703 | 407 | 390 | 62 | 45 | 0.122 | 1.000 |
| `nnunet_single` | `nnunet_earlymid` | 703 | 407 | 378 | 71 | 42 | 0.008 | 0.383 |
| `nnunet_single` | `nnunet_mid` | 703 | 407 | 415 | 62 | 70 | 0.543 | 1.000 |
| `nnunet_single` | `nnunet_late` | 703 | 407 | 395 | 69 | 57 | 0.327 | 1.000 |
| `nnunet_single` | `nnunetcbam_single` | 703 | 407 | 415 | 53 | 61 | 0.512 | 1.000 |
| `nnunet_single` | `nnunetcbam_multidecoder` | 703 | 407 | 439 | 40 | 72 | 0.003 | 0.165 |
| `nnunet_single` | `nnunetcbam_earlymid` | 703 | 407 | 435 | 44 | 72 | 0.012 | 0.533 |
| `nnunet_single` | `nnunetcbam_mid` | 703 | 407 | 411 | 57 | 61 | 0.783 | 1.000 |
| `nnunet_single` | `nnunetcbam_multihead` | 703 | 407 | 407 | 67 | 67 | 1.000 | 1.000 |
| `nnunet_single` | `segformer_single` | 703 | 407 | 448 | 62 | 103 | 0.002 | 0.099 |
| `nnunet_single` | `segformer_early` | 703 | 407 | 438 | 67 | 98 | 0.019 | 0.789 |
| `nnunet_single` | `segformer_mid` | 703 | 407 | 485 | 48 | 126 | <0.001 | <0.001 |
| `nnunet_single` | `segformer_late` | 703 | 407 | 445 | 60 | 98 | 0.003 | 0.165 |
| `nnunet_early` | `nnunet_earlymid` | 703 | 390 | 378 | 42 | 30 | 0.195 | 1.000 |
| `nnunet_early` | `nnunet_mid` | 703 | 390 | 415 | 42 | 67 | 0.021 | 0.801 |
| `nnunet_early` | `nnunetcbam_multidecoder` | 703 | 390 | 439 | 26 | 75 | <0.001 | <0.001 |
| `nnunet_early` | `nnunetcbam_earlymid` | 703 | 390 | 435 | 29 | 74 | <0.001 | <0.001 |
| `nnunet_early` | `nnunetcbam_mid` | 703 | 390 | 411 | 38 | 59 | 0.042 | 1.000 |
| `nnunet_early` | `segformer_early` | 703 | 390 | 438 | 55 | 103 | <0.001 | 0.011 |
| `nnunet_early` | `segformer_mid` | 703 | 390 | 485 | 46 | 141 | <0.001 | <0.001 |
| `nnunet_earlymid` | `nnunet_mid` | 703 | 378 | 415 | 31 | 68 | <0.001 | 0.017 |
| `nnunet_earlymid` | `nnunetcbam_earlymid` | 703 | 378 | 435 | 22 | 79 | <0.001 | <0.001 |
| `nnunet_earlymid` | `nnunetcbam_mid` | 703 | 378 | 411 | 28 | 61 | <0.001 | 0.037 |
| `nnunet_earlymid` | `segformer_mid` | 703 | 378 | 485 | 45 | 152 | <0.001 | <0.001 |
| `nnunet_mid` | `nnunetcbam_mid` | 703 | 415 | 411 | 41 | 37 | 0.734 | 1.000 |
| `nnunet_mid` | `segformer_mid` | 703 | 415 | 485 | 64 | 134 | <0.001 | <0.001 |
| `nnunet_late` | `nnunet_early` | 703 | 395 | 390 | 48 | 43 | 0.675 | 1.000 |
| `nnunet_late` | `nnunet_earlymid` | 703 | 395 | 378 | 54 | 37 | 0.093 | 1.000 |
| `nnunet_late` | `nnunet_mid` | 703 | 395 | 415 | 29 | 49 | 0.031 | 1.000 |
| `nnunet_late` | `nnunetcbam_multidecoder` | 703 | 395 | 439 | 26 | 70 | <0.001 | <0.001 |
| `nnunet_late` | `nnunetcbam_earlymid` | 703 | 395 | 435 | 27 | 67 | <0.001 | 0.003 |
| `nnunet_late` | `nnunetcbam_mid` | 703 | 395 | 411 | 33 | 49 | 0.097 | 1.000 |
| `nnunet_late` | `nnunetcbam_multihead` | 703 | 395 | 407 | 35 | 47 | 0.224 | 1.000 |
| `nnunet_late` | `segformer_early` | 703 | 395 | 438 | 49 | 92 | <0.001 | 0.023 |
| `nnunet_late` | `segformer_mid` | 703 | 395 | 485 | 41 | 131 | <0.001 | <0.001 |
| `nnunet_late` | `segformer_late` | 703 | 395 | 445 | 42 | 92 | <0.001 | 0.001 |
| `nnunetcbam_single` | `nnunet_early` | 703 | 415 | 390 | 64 | 39 | 0.018 | 0.740 |
| `nnunetcbam_single` | `nnunet_earlymid` | 703 | 415 | 378 | 68 | 31 | <0.001 | 0.017 |
| `nnunetcbam_single` | `nnunet_mid` | 703 | 415 | 415 | 52 | 52 | 1.000 | 1.000 |
| `nnunetcbam_single` | `nnunet_late` | 703 | 415 | 395 | 67 | 47 | 0.075 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_multidecoder` | 703 | 415 | 439 | 26 | 50 | 0.008 | 0.379 |
| `nnunetcbam_single` | `nnunetcbam_earlymid` | 703 | 415 | 435 | 31 | 51 | 0.035 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_mid` | 703 | 415 | 411 | 41 | 37 | 0.734 | 1.000 |
| `nnunetcbam_single` | `nnunetcbam_multihead` | 703 | 415 | 407 | 48 | 40 | 0.456 | 1.000 |
| `nnunetcbam_single` | `segformer_single` | 703 | 415 | 448 | 63 | 96 | 0.011 | 0.503 |
| `nnunetcbam_single` | `segformer_early` | 703 | 415 | 438 | 70 | 93 | 0.085 | 1.000 |
| `nnunetcbam_single` | `segformer_mid` | 703 | 415 | 485 | 56 | 126 | <0.001 | <0.001 |
| `nnunetcbam_single` | `segformer_late` | 703 | 415 | 445 | 63 | 93 | 0.020 | 0.789 |
| `nnunetcbam_multidecoder` | `nnunet_earlymid` | 703 | 439 | 378 | 82 | 21 | <0.001 | <0.001 |
| `nnunetcbam_multidecoder` | `nnunet_mid` | 703 | 439 | 415 | 61 | 37 | 0.020 | 0.789 |
| `nnunetcbam_multidecoder` | `nnunetcbam_earlymid` | 703 | 439 | 435 | 36 | 32 | 0.716 | 1.000 |
| `nnunetcbam_multidecoder` | `nnunetcbam_mid` | 703 | 439 | 411 | 48 | 20 | <0.001 | 0.053 |
| `nnunetcbam_multidecoder` | `segformer_early` | 703 | 439 | 438 | 78 | 77 | 1.000 | 1.000 |
| `nnunetcbam_multidecoder` | `segformer_mid` | 703 | 439 | 485 | 62 | 108 | <0.001 | 0.032 |
| `nnunetcbam_earlymid` | `nnunet_mid` | 703 | 435 | 415 | 60 | 40 | 0.057 | 1.000 |
| `nnunetcbam_earlymid` | `nnunetcbam_mid` | 703 | 435 | 411 | 43 | 19 | 0.003 | 0.165 |
| `nnunetcbam_earlymid` | `segformer_mid` | 703 | 435 | 485 | 49 | 99 | <0.001 | 0.003 |
| `nnunetcbam_mid` | `segformer_mid` | 703 | 411 | 485 | 48 | 122 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunet_early` | 703 | 407 | 390 | 59 | 42 | 0.111 | 1.000 |
| `nnunetcbam_multihead` | `nnunet_earlymid` | 703 | 407 | 378 | 62 | 33 | 0.004 | 0.192 |
| `nnunetcbam_multihead` | `nnunet_mid` | 703 | 407 | 415 | 43 | 51 | 0.470 | 1.000 |
| `nnunetcbam_multihead` | `nnunetcbam_multidecoder` | 703 | 407 | 439 | 22 | 54 | <0.001 | 0.020 |
| `nnunetcbam_multihead` | `nnunetcbam_earlymid` | 703 | 407 | 435 | 22 | 50 | 0.001 | 0.074 |
| `nnunetcbam_multihead` | `nnunetcbam_mid` | 703 | 407 | 411 | 26 | 30 | 0.689 | 1.000 |
| `nnunetcbam_multihead` | `segformer_early` | 703 | 407 | 438 | 59 | 90 | 0.014 | 0.603 |
| `nnunetcbam_multihead` | `segformer_mid` | 703 | 407 | 485 | 45 | 123 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `segformer_late` | 703 | 407 | 445 | 53 | 91 | 0.002 | 0.107 |
| `segformer_single` | `nnunet_early` | 703 | 448 | 390 | 110 | 52 | <0.001 | <0.001 |
| `segformer_single` | `nnunet_earlymid` | 703 | 448 | 378 | 118 | 48 | <0.001 | <0.001 |
| `segformer_single` | `nnunet_mid` | 703 | 448 | 415 | 102 | 69 | 0.014 | 0.609 |
| `segformer_single` | `nnunet_late` | 703 | 448 | 395 | 99 | 46 | <0.001 | <0.001 |
| `segformer_single` | `nnunetcbam_multidecoder` | 703 | 448 | 439 | 78 | 69 | 0.510 | 1.000 |
| `segformer_single` | `nnunetcbam_earlymid` | 703 | 448 | 435 | 74 | 61 | 0.302 | 1.000 |
| `segformer_single` | `nnunetcbam_mid` | 703 | 448 | 411 | 92 | 55 | 0.003 | 0.154 |
| `segformer_single` | `nnunetcbam_multihead` | 703 | 448 | 407 | 93 | 52 | <0.001 | 0.049 |
| `segformer_single` | `segformer_early` | 703 | 448 | 438 | 43 | 33 | 0.302 | 1.000 |
| `segformer_single` | `segformer_mid` | 703 | 448 | 485 | 23 | 60 | <0.001 | 0.004 |
| `segformer_single` | `segformer_late` | 703 | 448 | 445 | 38 | 35 | 0.815 | 1.000 |
| `segformer_early` | `nnunet_earlymid` | 703 | 438 | 378 | 113 | 53 | <0.001 | <0.001 |
| `segformer_early` | `nnunet_mid` | 703 | 438 | 415 | 99 | 76 | 0.096 | 1.000 |
| `segformer_early` | `nnunetcbam_earlymid` | 703 | 438 | 435 | 66 | 63 | 0.860 | 1.000 |
| `segformer_early` | `nnunetcbam_mid` | 703 | 438 | 411 | 87 | 60 | 0.032 | 1.000 |
| `segformer_early` | `segformer_mid` | 703 | 438 | 485 | 12 | 59 | <0.001 | <0.001 |
| `segformer_late` | `nnunet_early` | 703 | 445 | 390 | 104 | 49 | <0.001 | <0.001 |
| `segformer_late` | `nnunet_earlymid` | 703 | 445 | 378 | 114 | 47 | <0.001 | <0.001 |
| `segformer_late` | `nnunet_mid` | 703 | 445 | 415 | 99 | 69 | 0.025 | 0.924 |
| `segformer_late` | `nnunetcbam_multidecoder` | 703 | 445 | 439 | 76 | 70 | 0.679 | 1.000 |
| `segformer_late` | `nnunetcbam_earlymid` | 703 | 445 | 435 | 73 | 63 | 0.440 | 1.000 |
| `segformer_late` | `nnunetcbam_mid` | 703 | 445 | 411 | 84 | 50 | 0.004 | 0.205 |
| `segformer_late` | `segformer_early` | 703 | 445 | 438 | 35 | 28 | 0.450 | 1.000 |
| `segformer_late` | `segformer_mid` | 703 | 445 | 485 | 14 | 54 | <0.001 | <0.001 |

33 of 91 pairs are significant after Holm correction. The test treats the 703 hotspots as independent, although hotspots of one case are correlated. UQ run.

## Matched hotspots, benign

| Model A | Model B | Hotspots | Matched by A | Matched by B | Only A | Only B | McNemar p | Holm p |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| `nnunet_single` | `nnunet_early` | 1240 | 622 | 635 | 21 | 34 | 0.105 | 1.000 |
| `nnunet_single` | `nnunet_earlymid` | 1240 | 622 | 762 | 13 | 153 | <0.001 | <0.001 |
| `nnunet_single` | `nnunet_mid` | 1240 | 622 | 641 | 15 | 34 | 0.009 | 0.254 |
| `nnunet_single` | `nnunet_late` | 1240 | 622 | 763 | 25 | 166 | <0.001 | <0.001 |
| `nnunet_single` | `nnunetcbam_single` | 1240 | 622 | 608 | 33 | 19 | 0.070 | 1.000 |
| `nnunet_single` | `nnunetcbam_multidecoder` | 1240 | 622 | 639 | 15 | 32 | 0.019 | 0.484 |
| `nnunet_single` | `nnunetcbam_earlymid` | 1240 | 622 | 642 | 11 | 31 | 0.003 | 0.090 |
| `nnunet_single` | `nnunetcbam_mid` | 1240 | 622 | 637 | 14 | 29 | 0.032 | 0.757 |
| `nnunet_single` | `nnunetcbam_multihead` | 1240 | 622 | 811 | 16 | 205 | <0.001 | <0.001 |
| `nnunet_single` | `segformer_single` | 1240 | 622 | 733 | 56 | 167 | <0.001 | <0.001 |
| `nnunet_single` | `segformer_early` | 1240 | 622 | 774 | 45 | 197 | <0.001 | <0.001 |
| `nnunet_single` | `segformer_mid` | 1240 | 622 | 771 | 47 | 196 | <0.001 | <0.001 |
| `nnunet_single` | `segformer_late` | 1240 | 622 | 761 | 49 | 188 | <0.001 | <0.001 |
| `nnunet_early` | `nnunet_earlymid` | 1240 | 635 | 762 | 12 | 139 | <0.001 | <0.001 |
| `nnunet_early` | `nnunet_mid` | 1240 | 635 | 641 | 23 | 29 | 0.488 | 1.000 |
| `nnunet_early` | `nnunetcbam_multidecoder` | 1240 | 635 | 639 | 18 | 22 | 0.636 | 1.000 |
| `nnunet_early` | `nnunetcbam_earlymid` | 1240 | 635 | 642 | 20 | 27 | 0.382 | 1.000 |
| `nnunet_early` | `nnunetcbam_mid` | 1240 | 635 | 637 | 22 | 24 | 0.883 | 1.000 |
| `nnunet_early` | `segformer_early` | 1240 | 635 | 774 | 36 | 175 | <0.001 | <0.001 |
| `nnunet_early` | `segformer_mid` | 1240 | 635 | 771 | 39 | 175 | <0.001 | <0.001 |
| `nnunet_earlymid` | `nnunet_mid` | 1240 | 762 | 641 | 144 | 23 | <0.001 | <0.001 |
| `nnunet_earlymid` | `nnunetcbam_earlymid` | 1240 | 762 | 642 | 140 | 20 | <0.001 | <0.001 |
| `nnunet_earlymid` | `nnunetcbam_mid` | 1240 | 762 | 637 | 147 | 22 | <0.001 | <0.001 |
| `nnunet_earlymid` | `segformer_mid` | 1240 | 762 | 771 | 89 | 98 | 0.559 | 1.000 |
| `nnunet_mid` | `nnunetcbam_mid` | 1240 | 641 | 637 | 23 | 19 | 0.644 | 1.000 |
| `nnunet_mid` | `segformer_mid` | 1240 | 641 | 771 | 50 | 180 | <0.001 | <0.001 |
| `nnunet_late` | `nnunet_early` | 1240 | 763 | 635 | 147 | 19 | <0.001 | <0.001 |
| `nnunet_late` | `nnunet_earlymid` | 1240 | 763 | 762 | 53 | 52 | 1.000 | 1.000 |
| `nnunet_late` | `nnunet_mid` | 1240 | 763 | 641 | 144 | 22 | <0.001 | <0.001 |
| `nnunet_late` | `nnunetcbam_multidecoder` | 1240 | 763 | 639 | 146 | 22 | <0.001 | <0.001 |
| `nnunet_late` | `nnunetcbam_earlymid` | 1240 | 763 | 642 | 144 | 23 | <0.001 | <0.001 |
| `nnunet_late` | `nnunetcbam_mid` | 1240 | 763 | 637 | 149 | 23 | <0.001 | <0.001 |
| `nnunet_late` | `nnunetcbam_multihead` | 1240 | 763 | 811 | 21 | 69 | <0.001 | <0.001 |
| `nnunet_late` | `segformer_early` | 1240 | 763 | 774 | 73 | 84 | 0.425 | 1.000 |
| `nnunet_late` | `segformer_mid` | 1240 | 763 | 771 | 76 | 84 | 0.580 | 1.000 |
| `nnunet_late` | `segformer_late` | 1240 | 763 | 761 | 71 | 69 | 0.933 | 1.000 |
| `nnunetcbam_single` | `nnunet_early` | 1240 | 608 | 635 | 18 | 45 | <0.001 | 0.029 |
| `nnunetcbam_single` | `nnunet_earlymid` | 1240 | 608 | 762 | 16 | 170 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunet_mid` | 1240 | 608 | 641 | 14 | 47 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunet_late` | 1240 | 608 | 763 | 20 | 175 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunetcbam_multidecoder` | 1240 | 608 | 639 | 9 | 40 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunetcbam_earlymid` | 1240 | 608 | 642 | 7 | 41 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunetcbam_mid` | 1240 | 608 | 637 | 9 | 38 | <0.001 | <0.001 |
| `nnunetcbam_single` | `nnunetcbam_multihead` | 1240 | 608 | 811 | 8 | 211 | <0.001 | <0.001 |
| `nnunetcbam_single` | `segformer_single` | 1240 | 608 | 733 | 52 | 177 | <0.001 | <0.001 |
| `nnunetcbam_single` | `segformer_early` | 1240 | 608 | 774 | 38 | 204 | <0.001 | <0.001 |
| `nnunetcbam_single` | `segformer_mid` | 1240 | 608 | 771 | 42 | 205 | <0.001 | <0.001 |
| `nnunetcbam_single` | `segformer_late` | 1240 | 608 | 761 | 39 | 192 | <0.001 | <0.001 |
| `nnunetcbam_multidecoder` | `nnunet_earlymid` | 1240 | 639 | 762 | 17 | 140 | <0.001 | <0.001 |
| `nnunetcbam_multidecoder` | `nnunet_mid` | 1240 | 639 | 641 | 18 | 20 | 0.871 | 1.000 |
| `nnunetcbam_multidecoder` | `nnunetcbam_earlymid` | 1240 | 639 | 642 | 10 | 13 | 0.678 | 1.000 |
| `nnunetcbam_multidecoder` | `nnunetcbam_mid` | 1240 | 639 | 637 | 12 | 10 | 0.832 | 1.000 |
| `nnunetcbam_multidecoder` | `segformer_early` | 1240 | 639 | 774 | 42 | 177 | <0.001 | <0.001 |
| `nnunetcbam_multidecoder` | `segformer_mid` | 1240 | 639 | 771 | 46 | 178 | <0.001 | <0.001 |
| `nnunetcbam_earlymid` | `nnunet_mid` | 1240 | 642 | 641 | 18 | 17 | 1.000 | 1.000 |
| `nnunetcbam_earlymid` | `nnunetcbam_mid` | 1240 | 642 | 637 | 16 | 11 | 0.442 | 1.000 |
| `nnunetcbam_earlymid` | `segformer_mid` | 1240 | 642 | 771 | 50 | 179 | <0.001 | <0.001 |
| `nnunetcbam_mid` | `segformer_mid` | 1240 | 637 | 771 | 43 | 177 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunet_early` | 1240 | 811 | 635 | 191 | 15 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunet_earlymid` | 1240 | 811 | 762 | 82 | 33 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunet_mid` | 1240 | 811 | 641 | 188 | 18 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunetcbam_multidecoder` | 1240 | 811 | 639 | 186 | 14 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunetcbam_earlymid` | 1240 | 811 | 642 | 180 | 11 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `nnunetcbam_mid` | 1240 | 811 | 637 | 187 | 13 | <0.001 | <0.001 |
| `nnunetcbam_multihead` | `segformer_early` | 1240 | 811 | 774 | 99 | 62 | 0.004 | 0.128 |
| `nnunetcbam_multihead` | `segformer_mid` | 1240 | 811 | 771 | 107 | 67 | 0.003 | 0.090 |
| `nnunetcbam_multihead` | `segformer_late` | 1240 | 811 | 761 | 100 | 50 | <0.001 | 0.002 |
| `segformer_single` | `nnunet_early` | 1240 | 733 | 635 | 154 | 56 | <0.001 | <0.001 |
| `segformer_single` | `nnunet_earlymid` | 1240 | 733 | 762 | 78 | 107 | 0.039 | 0.903 |
| `segformer_single` | `nnunet_mid` | 1240 | 733 | 641 | 155 | 63 | <0.001 | <0.001 |
| `segformer_single` | `nnunet_late` | 1240 | 733 | 763 | 65 | 95 | 0.022 | 0.539 |
| `segformer_single` | `nnunetcbam_multidecoder` | 1240 | 733 | 639 | 154 | 60 | <0.001 | <0.001 |
| `segformer_single` | `nnunetcbam_earlymid` | 1240 | 733 | 642 | 154 | 63 | <0.001 | <0.001 |
| `segformer_single` | `nnunetcbam_mid` | 1240 | 733 | 637 | 154 | 58 | <0.001 | <0.001 |
| `segformer_single` | `nnunetcbam_multihead` | 1240 | 733 | 811 | 50 | 128 | <0.001 | <0.001 |
| `segformer_single` | `segformer_early` | 1240 | 733 | 774 | 28 | 69 | <0.001 | 0.001 |
| `segformer_single` | `segformer_mid` | 1240 | 733 | 771 | 41 | 79 | <0.001 | 0.022 |
| `segformer_single` | `segformer_late` | 1240 | 733 | 761 | 38 | 66 | 0.008 | 0.218 |
| `segformer_early` | `nnunet_earlymid` | 1240 | 774 | 762 | 97 | 85 | 0.415 | 1.000 |
| `segformer_early` | `nnunet_mid` | 1240 | 774 | 641 | 181 | 48 | <0.001 | <0.001 |
| `segformer_early` | `nnunetcbam_earlymid` | 1240 | 774 | 642 | 179 | 47 | <0.001 | <0.001 |
| `segformer_early` | `nnunetcbam_mid` | 1240 | 774 | 637 | 178 | 41 | <0.001 | <0.001 |
| `segformer_early` | `segformer_mid` | 1240 | 774 | 771 | 36 | 33 | 0.810 | 1.000 |
| `segformer_late` | `nnunet_early` | 1240 | 761 | 635 | 166 | 40 | <0.001 | <0.001 |
| `segformer_late` | `nnunet_earlymid` | 1240 | 761 | 762 | 87 | 88 | 1.000 | 1.000 |
| `segformer_late` | `nnunet_mid` | 1240 | 761 | 641 | 172 | 52 | <0.001 | <0.001 |
| `segformer_late` | `nnunetcbam_multidecoder` | 1240 | 761 | 639 | 169 | 47 | <0.001 | <0.001 |
| `segformer_late` | `nnunetcbam_earlymid` | 1240 | 761 | 642 | 168 | 49 | <0.001 | <0.001 |
| `segformer_late` | `nnunetcbam_mid` | 1240 | 761 | 637 | 168 | 44 | <0.001 | <0.001 |
| `segformer_late` | `segformer_early` | 1240 | 761 | 774 | 33 | 46 | 0.177 | 1.000 |
| `segformer_late` | `segformer_mid` | 1240 | 761 | 771 | 40 | 50 | 0.343 | 1.000 |

60 of 91 pairs are significant after Holm correction. The test treats the 1240 hotspots as independent, although hotspots of one case are correlated. UQ run.

## Dice of the UQ run against the standard-pipeline run

| Checkpoint | Malignant, UQ run minus standard-pipeline run | Benign, UQ run minus standard-pipeline run |
|:---|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | +0.0041 | -0.0036 |
| nnU-Net, Early (`nnunet_early`) | -0.0027 | -0.0097 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | +0.0044 | -0.0114 |
| nnU-Net, Mid (`nnunet_mid`) | +0.0017 | -0.0082 |
| nnU-Net, Late (`nnunet_late`) | -0.0056 | -0.0074 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | +0.0058 | -0.0083 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | +0.0166 | -0.0036 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | +0.0104 | -0.0076 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | +0.0152 | -0.0079 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | +0.0118 | -0.0052 |
| SegFormer, single-task (`segformer_single`) | +0.0000 | +0.0000 |
| SegFormer, Early (`segformer_early`) | +0.0000 | +0.0000 |
| SegFormer, Mid (`segformer_mid`) | +0.0000 | -0.0000 |
| SegFormer, Late (`segformer_late`) | +0.0000 | +0.0000 |

Lesion-bearing Dice. The two runs are identical for the SegFormer checkpoints. For the nnU-Net-based checkpoints the standard pipeline crops each image, normalizes the crop, and slides a window, while the UQ run reads the full image in one pass. Source: `tables/dice_by_model.csv`.
