# S4. Paired AUC tests for all fourteen checkpoints

Region AUC differences are tested with a paired bootstrap over the 293 test cases: the same resampled cases for every method and checkpoint, a 95% percentile interval of the difference, and p from the share of resamples with a difference on each side of zero. Region AUC is pooled over both views.

## MetaSeg against each other method

### Malignant

| Checkpoint | Method B | MetaSeg AUC | AUC of B | Difference | 95% interval | p |
|:---|:---|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | Predictive entropy | 0.7520 | 0.7079 | +0.0440 | [+0.0094, +0.0770] | 0.014 |
| nnU-Net, single-task (`nnunet_single`) | Local gradient UQ | 0.7520 | 0.7180 | +0.0340 | [+0.0079, +0.0622] | 0.010 |
| nnU-Net, single-task (`nnunet_single`) | Standardized max logit | 0.7520 | 0.7235 | +0.0284 | [-0.0063, +0.0646] | 0.105 |
| nnU-Net, single-task (`nnunet_single`) | Max-softmax | 0.7520 | 0.6984 | +0.0535 | [+0.0193, +0.0880] | 0.001 |
| nnU-Net, single-task (`nnunet_single`) | Mahalanobis distance | 0.7520 | 0.5470 | +0.2050 | [+0.1480, +0.2627] | <0.001 |
| nnU-Net, single-task (`nnunet_single`) | Inverse area (control) | 0.7520 | 0.7158 | +0.0362 | [+0.0090, +0.0607] | 0.004 |
| nnU-Net, Early (`nnunet_early`) | Predictive entropy | 0.7549 | 0.6747 | +0.0802 | [+0.0478, +0.1127] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | Local gradient UQ | 0.7549 | 0.7073 | +0.0476 | [+0.0187, +0.0788] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | Standardized max logit | 0.7549 | 0.7184 | +0.0366 | [-0.0029, +0.0767] | 0.076 |
| nnU-Net, Early (`nnunet_early`) | Max-softmax | 0.7549 | 0.6557 | +0.0993 | [+0.0657, +0.1325] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | Mahalanobis distance | 0.7549 | 0.6476 | +0.1073 | [+0.0615, +0.1546] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | Inverse area (control) | 0.7549 | 0.7585 | -0.0036 | [-0.0254, +0.0161] | 0.758 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Predictive entropy | 0.7260 | 0.6960 | +0.0301 | [+0.0013, +0.0590] | 0.044 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Local gradient UQ | 0.7260 | 0.6978 | +0.0282 | [-0.0020, +0.0580] | 0.062 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Standardized max logit | 0.7260 | 0.6783 | +0.0478 | [-0.0005, +0.0974] | 0.054 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Max-softmax | 0.7260 | 0.6869 | +0.0391 | [+0.0100, +0.0672] | 0.007 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Mahalanobis distance | 0.7260 | 0.5075 | +0.2186 | [+0.1493, +0.2909] | <0.001 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Inverse area (control) | 0.7260 | 0.7030 | +0.0231 | [-0.0086, +0.0539] | 0.141 |
| nnU-Net, Mid (`nnunet_mid`) | Predictive entropy | 0.7697 | 0.7327 | +0.0370 | [+0.0140, +0.0603] | 0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Local gradient UQ | 0.7697 | 0.7255 | +0.0442 | [+0.0223, +0.0669] | <0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Standardized max logit | 0.7697 | 0.7568 | +0.0130 | [-0.0123, +0.0370] | 0.321 |
| nnU-Net, Mid (`nnunet_mid`) | Max-softmax | 0.7697 | 0.7252 | +0.0445 | [+0.0189, +0.0695] | <0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Mahalanobis distance | 0.7697 | 0.4743 | +0.2955 | [+0.2155, +0.3707] | <0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Inverse area (control) | 0.7697 | 0.7518 | +0.0180 | [-0.0048, +0.0418] | 0.133 |
| nnU-Net, Late (`nnunet_late`) | Predictive entropy | 0.7731 | 0.7561 | +0.0170 | [-0.0194, +0.0610] | 0.367 |
| nnU-Net, Late (`nnunet_late`) | Local gradient UQ | 0.7731 | 0.7181 | +0.0550 | [+0.0125, +0.1012] | 0.012 |
| nnU-Net, Late (`nnunet_late`) | Standardized max logit | 0.7731 | 0.7940 | -0.0208 | [-0.0565, +0.0196] | 0.341 |
| nnU-Net, Late (`nnunet_late`) | Max-softmax | 0.7731 | 0.7397 | +0.0335 | [-0.0065, +0.0803] | 0.103 |
| nnU-Net, Late (`nnunet_late`) | Mahalanobis distance | 0.7731 | 0.6644 | +0.1087 | [+0.0397, +0.1736] | 0.002 |
| nnU-Net, Late (`nnunet_late`) | Inverse area (control) | 0.7731 | 0.7359 | +0.0372 | [+0.0072, +0.0675] | 0.011 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Predictive entropy | 0.7284 | 0.6849 | +0.0434 | [+0.0007, +0.0830] | 0.048 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Local gradient UQ | 0.7284 | 0.6988 | +0.0296 | [-0.0009, +0.0612] | 0.058 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Standardized max logit | 0.7284 | 0.7315 | -0.0032 | [-0.0386, +0.0302] | 0.878 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Max-softmax | 0.7284 | 0.6657 | +0.0626 | [+0.0186, +0.1030] | 0.004 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Mahalanobis distance | 0.7284 | 0.5442 | +0.1842 | [+0.1254, +0.2388] | <0.001 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Inverse area (control) | 0.7284 | 0.7026 | +0.0258 | [+0.0003, +0.0531] | 0.047 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Predictive entropy | 0.7455 | 0.6690 | +0.0766 | [+0.0157, +0.1391] | 0.019 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Local gradient UQ | 0.7455 | 0.6915 | +0.0541 | [+0.0175, +0.0931] | 0.004 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Standardized max logit | 0.7455 | 0.7147 | +0.0309 | [-0.0258, +0.0889] | 0.283 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Max-softmax | 0.7455 | 0.6529 | +0.0927 | [+0.0324, +0.1550] | 0.002 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Mahalanobis distance | 0.7455 | 0.5486 | +0.1969 | [+0.1431, +0.2488] | <0.001 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Inverse area (control) | 0.7455 | 0.7080 | +0.0375 | [+0.0146, +0.0602] | 0.003 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Predictive entropy | 0.7721 | 0.6979 | +0.0741 | [+0.0276, +0.1193] | 0.001 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Local gradient UQ | 0.7721 | 0.7253 | +0.0468 | [+0.0109, +0.0843] | 0.010 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Standardized max logit | 0.7721 | 0.7381 | +0.0340 | [-0.0033, +0.0684] | 0.071 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Max-softmax | 0.7721 | 0.6845 | +0.0875 | [+0.0385, +0.1352] | <0.001 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Mahalanobis distance | 0.7721 | 0.5291 | +0.2429 | [+0.1822, +0.3003] | <0.001 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Inverse area (control) | 0.7721 | 0.7169 | +0.0551 | [+0.0245, +0.0829] | <0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Predictive entropy | 0.7688 | 0.7268 | +0.0419 | [+0.0023, +0.0861] | 0.033 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Local gradient UQ | 0.7688 | 0.6999 | +0.0688 | [+0.0279, +0.1124] | <0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Standardized max logit | 0.7688 | 0.7959 | -0.0271 | [-0.0593, +0.0099] | 0.145 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Max-softmax | 0.7688 | 0.6999 | +0.0689 | [+0.0257, +0.1162] | <0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Mahalanobis distance | 0.7688 | 0.5609 | +0.2078 | [+0.1490, +0.2695] | <0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Inverse area (control) | 0.7688 | 0.7354 | +0.0333 | [+0.0085, +0.0576] | 0.009 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Predictive entropy | 0.7480 | 0.7065 | +0.0415 | [+0.0111, +0.0742] | 0.007 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Local gradient UQ | 0.7480 | 0.6770 | +0.0710 | [+0.0357, +0.1088] | <0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Standardized max logit | 0.7480 | 0.7728 | -0.0247 | [-0.0492, +0.0009] | 0.059 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Max-softmax | 0.7480 | 0.6788 | +0.0692 | [+0.0342, +0.1055] | <0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Mahalanobis distance | 0.7480 | 0.5718 | +0.1762 | [+0.1084, +0.2423] | <0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Inverse area (control) | 0.7480 | 0.7050 | +0.0430 | [+0.0115, +0.0760] | 0.008 |
| SegFormer, single-task (`segformer_single`) | Predictive entropy | 0.7891 | 0.7949 | -0.0058 | [-0.0224, +0.0139] | 0.552 |
| SegFormer, single-task (`segformer_single`) | Local gradient UQ | 0.7891 | 0.7733 | +0.0158 | [-0.0028, +0.0397] | 0.093 |
| SegFormer, single-task (`segformer_single`) | Standardized max logit | 0.7891 | 0.8022 | -0.0131 | [-0.0351, +0.0122] | 0.284 |
| SegFormer, single-task (`segformer_single`) | Max-softmax | 0.7891 | 0.7849 | +0.0041 | [-0.0162, +0.0284] | 0.683 |
| SegFormer, single-task (`segformer_single`) | Mahalanobis distance | 0.7891 | 0.4799 | +0.3091 | [+0.2303, +0.3797] | <0.001 |
| SegFormer, single-task (`segformer_single`) | Inverse area (control) | 0.7891 | 0.7160 | +0.0731 | [+0.0426, +0.1015] | <0.001 |
| SegFormer, Early (`segformer_early`) | Predictive entropy | 0.7968 | 0.7946 | +0.0022 | [-0.0174, +0.0201] | 0.774 |
| SegFormer, Early (`segformer_early`) | Local gradient UQ | 0.7968 | 0.7788 | +0.0180 | [-0.0052, +0.0381] | 0.115 |
| SegFormer, Early (`segformer_early`) | Standardized max logit | 0.7968 | 0.7961 | +0.0006 | [-0.0270, +0.0272] | 0.929 |
| SegFormer, Early (`segformer_early`) | Max-softmax | 0.7968 | 0.7802 | +0.0166 | [-0.0044, +0.0383] | 0.106 |
| SegFormer, Early (`segformer_early`) | Mahalanobis distance | 0.7968 | 0.4706 | +0.3262 | [+0.2372, +0.4034] | <0.001 |
| SegFormer, Early (`segformer_early`) | Inverse area (control) | 0.7968 | 0.7298 | +0.0669 | [+0.0242, +0.1072] | 0.001 |
| SegFormer, Mid (`segformer_mid`) | Predictive entropy | 0.7947 | 0.7943 | +0.0004 | [-0.0113, +0.0141] | 0.982 |
| SegFormer, Mid (`segformer_mid`) | Local gradient UQ | 0.7947 | 0.7791 | +0.0156 | [-0.0002, +0.0346] | 0.055 |
| SegFormer, Mid (`segformer_mid`) | Standardized max logit | 0.7947 | 0.7891 | +0.0056 | [-0.0189, +0.0292] | 0.658 |
| SegFormer, Mid (`segformer_mid`) | Max-softmax | 0.7947 | 0.7813 | +0.0134 | [-0.0000, +0.0281] | 0.051 |
| SegFormer, Mid (`segformer_mid`) | Mahalanobis distance | 0.7947 | 0.5055 | +0.2892 | [+0.2094, +0.3631] | <0.001 |
| SegFormer, Mid (`segformer_mid`) | Inverse area (control) | 0.7947 | 0.7348 | +0.0600 | [+0.0145, +0.1076] | 0.003 |
| SegFormer, Late (`segformer_late`) | Predictive entropy | 0.7712 | 0.7772 | -0.0060 | [-0.0194, +0.0082] | 0.360 |
| SegFormer, Late (`segformer_late`) | Local gradient UQ | 0.7712 | 0.7728 | -0.0017 | [-0.0174, +0.0121] | 0.801 |
| SegFormer, Late (`segformer_late`) | Standardized max logit | 0.7712 | 0.7677 | +0.0034 | [-0.0208, +0.0281] | 0.738 |
| SegFormer, Late (`segformer_late`) | Max-softmax | 0.7712 | 0.7716 | -0.0004 | [-0.0159, +0.0141] | 0.969 |
| SegFormer, Late (`segformer_late`) | Mahalanobis distance | 0.7712 | 0.4810 | +0.2901 | [+0.1869, +0.3767] | <0.001 |
| SegFormer, Late (`segformer_late`) | Inverse area (control) | 0.7712 | 0.7047 | +0.0665 | [+0.0198, +0.1168] | 0.006 |

51 of 84 comparisons have p below 0.05 (no correction for multiple comparisons).

### Benign

| Checkpoint | Method B | MetaSeg AUC | AUC of B | Difference | 95% interval | p |
|:---|:---|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | Predictive entropy | 0.7936 | 0.7997 | -0.0061 | [-0.0156, +0.0032] | 0.184 |
| nnU-Net, single-task (`nnunet_single`) | Local gradient UQ | 0.7936 | 0.7764 | +0.0171 | [-0.0003, +0.0340] | 0.054 |
| nnU-Net, single-task (`nnunet_single`) | Standardized max logit | 0.7936 | 0.7708 | +0.0228 | [-0.0038, +0.0507] | 0.090 |
| nnU-Net, single-task (`nnunet_single`) | Max-softmax | 0.7936 | 0.7905 | +0.0030 | [-0.0085, +0.0149] | 0.615 |
| nnU-Net, single-task (`nnunet_single`) | Mahalanobis distance | 0.7936 | 0.5743 | +0.2192 | [+0.1743, +0.2634] | <0.001 |
| nnU-Net, single-task (`nnunet_single`) | Inverse area (control) | 0.7936 | 0.7335 | +0.0600 | [+0.0282, +0.0929] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | Predictive entropy | 0.7418 | 0.7477 | -0.0059 | [-0.0213, +0.0099] | 0.477 |
| nnU-Net, Early (`nnunet_early`) | Local gradient UQ | 0.7418 | 0.7211 | +0.0207 | [-0.0013, +0.0437] | 0.069 |
| nnU-Net, Early (`nnunet_early`) | Standardized max logit | 0.7418 | 0.7574 | -0.0155 | [-0.0408, +0.0101] | 0.238 |
| nnU-Net, Early (`nnunet_early`) | Max-softmax | 0.7418 | 0.7388 | +0.0031 | [-0.0126, +0.0185] | 0.693 |
| nnU-Net, Early (`nnunet_early`) | Mahalanobis distance | 0.7418 | 0.5657 | +0.1761 | [+0.1314, +0.2241] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | Inverse area (control) | 0.7418 | 0.6994 | +0.0424 | [+0.0080, +0.0781] | 0.014 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Predictive entropy | 0.7426 | 0.7448 | -0.0022 | [-0.0113, +0.0067] | 0.629 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Local gradient UQ | 0.7426 | 0.7136 | +0.0291 | [+0.0130, +0.0440] | <0.001 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Standardized max logit | 0.7426 | 0.7274 | +0.0152 | [-0.0125, +0.0432] | 0.288 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Max-softmax | 0.7426 | 0.7316 | +0.0111 | [+0.0019, +0.0205] | 0.023 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Mahalanobis distance | 0.7426 | 0.4406 | +0.3020 | [+0.2506, +0.3503] | <0.001 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | Inverse area (control) | 0.7426 | 0.7014 | +0.0412 | [+0.0148, +0.0671] | 0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Predictive entropy | 0.7943 | 0.7978 | -0.0035 | [-0.0147, +0.0085] | 0.535 |
| nnU-Net, Mid (`nnunet_mid`) | Local gradient UQ | 0.7943 | 0.7779 | +0.0163 | [-0.0015, +0.0364] | 0.075 |
| nnU-Net, Mid (`nnunet_mid`) | Standardized max logit | 0.7943 | 0.7624 | +0.0319 | [+0.0114, +0.0526] | <0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Max-softmax | 0.7943 | 0.7878 | +0.0065 | [-0.0061, +0.0199] | 0.317 |
| nnU-Net, Mid (`nnunet_mid`) | Mahalanobis distance | 0.7943 | 0.5358 | +0.2584 | [+0.2143, +0.3052] | <0.001 |
| nnU-Net, Mid (`nnunet_mid`) | Inverse area (control) | 0.7943 | 0.7487 | +0.0455 | [+0.0185, +0.0716] | <0.001 |
| nnU-Net, Late (`nnunet_late`) | Predictive entropy | 0.7565 | 0.7530 | +0.0035 | [-0.0074, +0.0148] | 0.553 |
| nnU-Net, Late (`nnunet_late`) | Local gradient UQ | 0.7565 | 0.7298 | +0.0267 | [+0.0121, +0.0411] | <0.001 |
| nnU-Net, Late (`nnunet_late`) | Standardized max logit | 0.7565 | 0.7603 | -0.0037 | [-0.0232, +0.0163] | 0.701 |
| nnU-Net, Late (`nnunet_late`) | Max-softmax | 0.7565 | 0.7433 | +0.0132 | [+0.0000, +0.0267] | 0.050 |
| nnU-Net, Late (`nnunet_late`) | Mahalanobis distance | 0.7565 | 0.5661 | +0.1905 | [+0.1564, +0.2241] | <0.001 |
| nnU-Net, Late (`nnunet_late`) | Inverse area (control) | 0.7565 | 0.7289 | +0.0276 | [+0.0078, +0.0461] | 0.001 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Predictive entropy | 0.7852 | 0.7803 | +0.0049 | [-0.0060, +0.0162] | 0.406 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Local gradient UQ | 0.7852 | 0.7617 | +0.0235 | [+0.0046, +0.0415] | 0.012 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Standardized max logit | 0.7852 | 0.8144 | -0.0292 | [-0.0491, -0.0092] | 0.006 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Max-softmax | 0.7852 | 0.7680 | +0.0172 | [+0.0048, +0.0302] | 0.006 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Mahalanobis distance | 0.7852 | 0.5594 | +0.2258 | [+0.1809, +0.2703] | <0.001 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | Inverse area (control) | 0.7852 | 0.7502 | +0.0350 | [+0.0077, +0.0631] | 0.015 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Predictive entropy | 0.7285 | 0.7258 | +0.0027 | [-0.0080, +0.0131] | 0.626 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Local gradient UQ | 0.7285 | 0.7118 | +0.0167 | [-0.0042, +0.0380] | 0.118 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Standardized max logit | 0.7285 | 0.7633 | -0.0349 | [-0.0583, -0.0131] | 0.005 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Max-softmax | 0.7285 | 0.7071 | +0.0214 | [+0.0058, +0.0371] | 0.006 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Mahalanobis distance | 0.7285 | 0.5348 | +0.1936 | [+0.1501, +0.2420] | <0.001 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | Inverse area (control) | 0.7285 | 0.7116 | +0.0169 | [-0.0213, +0.0542] | 0.362 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Predictive entropy | 0.7849 | 0.7795 | +0.0054 | [-0.0078, +0.0192] | 0.422 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Local gradient UQ | 0.7849 | 0.7667 | +0.0182 | [+0.0032, +0.0338] | 0.016 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Standardized max logit | 0.7849 | 0.7967 | -0.0118 | [-0.0316, +0.0069] | 0.217 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Max-softmax | 0.7849 | 0.7685 | +0.0164 | [+0.0011, +0.0336] | 0.036 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Mahalanobis distance | 0.7849 | 0.5679 | +0.2169 | [+0.1756, +0.2585] | <0.001 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | Inverse area (control) | 0.7849 | 0.7294 | +0.0555 | [+0.0248, +0.0853] | 0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Predictive entropy | 0.7985 | 0.7920 | +0.0066 | [-0.0071, +0.0205] | 0.369 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Local gradient UQ | 0.7985 | 0.7668 | +0.0318 | [+0.0102, +0.0528] | 0.003 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Standardized max logit | 0.7985 | 0.8098 | -0.0113 | [-0.0316, +0.0095] | 0.259 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Max-softmax | 0.7985 | 0.7782 | +0.0204 | [+0.0023, +0.0376] | 0.025 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Mahalanobis distance | 0.7985 | 0.5838 | +0.2147 | [+0.1744, +0.2523] | <0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | Inverse area (control) | 0.7985 | 0.7490 | +0.0495 | [+0.0205, +0.0781] | <0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Predictive entropy | 0.7608 | 0.7523 | +0.0085 | [-0.0042, +0.0208] | 0.200 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Local gradient UQ | 0.7608 | 0.7403 | +0.0205 | [+0.0061, +0.0341] | 0.006 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Standardized max logit | 0.7608 | 0.7627 | -0.0019 | [-0.0187, +0.0145] | 0.817 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Max-softmax | 0.7608 | 0.7386 | +0.0222 | [+0.0081, +0.0360] | 0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Mahalanobis distance | 0.7608 | 0.6060 | +0.1548 | [+0.1219, +0.1897] | <0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | Inverse area (control) | 0.7608 | 0.7394 | +0.0214 | [+0.0007, +0.0415] | 0.045 |
| SegFormer, single-task (`segformer_single`) | Predictive entropy | 0.7783 | 0.7724 | +0.0059 | [-0.0061, +0.0182] | 0.333 |
| SegFormer, single-task (`segformer_single`) | Local gradient UQ | 0.7783 | 0.7513 | +0.0270 | [+0.0133, +0.0417] | <0.001 |
| SegFormer, single-task (`segformer_single`) | Standardized max logit | 0.7783 | 0.7165 | +0.0618 | [+0.0319, +0.0902] | <0.001 |
| SegFormer, single-task (`segformer_single`) | Max-softmax | 0.7783 | 0.7674 | +0.0109 | [-0.0032, +0.0247] | 0.124 |
| SegFormer, single-task (`segformer_single`) | Mahalanobis distance | 0.7783 | 0.4785 | +0.2998 | [+0.2474, +0.3507] | <0.001 |
| SegFormer, single-task (`segformer_single`) | Inverse area (control) | 0.7783 | 0.7316 | +0.0467 | [+0.0239, +0.0698] | <0.001 |
| SegFormer, Early (`segformer_early`) | Predictive entropy | 0.7734 | 0.7712 | +0.0023 | [-0.0081, +0.0131] | 0.715 |
| SegFormer, Early (`segformer_early`) | Local gradient UQ | 0.7734 | 0.7545 | +0.0189 | [+0.0068, +0.0310] | 0.001 |
| SegFormer, Early (`segformer_early`) | Standardized max logit | 0.7734 | 0.7127 | +0.0607 | [+0.0320, +0.0905] | <0.001 |
| SegFormer, Early (`segformer_early`) | Max-softmax | 0.7734 | 0.7621 | +0.0113 | [-0.0004, +0.0237] | 0.056 |
| SegFormer, Early (`segformer_early`) | Mahalanobis distance | 0.7734 | 0.5133 | +0.2601 | [+0.2068, +0.3110] | <0.001 |
| SegFormer, Early (`segformer_early`) | Inverse area (control) | 0.7734 | 0.7328 | +0.0406 | [+0.0163, +0.0625] | <0.001 |
| SegFormer, Mid (`segformer_mid`) | Predictive entropy | 0.7708 | 0.7671 | +0.0037 | [-0.0076, +0.0144] | 0.518 |
| SegFormer, Mid (`segformer_mid`) | Local gradient UQ | 0.7708 | 0.7501 | +0.0206 | [+0.0086, +0.0324] | 0.002 |
| SegFormer, Mid (`segformer_mid`) | Standardized max logit | 0.7708 | 0.7190 | +0.0518 | [+0.0261, +0.0776] | <0.001 |
| SegFormer, Mid (`segformer_mid`) | Max-softmax | 0.7708 | 0.7620 | +0.0088 | [-0.0039, +0.0215] | 0.172 |
| SegFormer, Mid (`segformer_mid`) | Mahalanobis distance | 0.7708 | 0.5077 | +0.2631 | [+0.2098, +0.3132] | <0.001 |
| SegFormer, Mid (`segformer_mid`) | Inverse area (control) | 0.7708 | 0.7230 | +0.0478 | [+0.0230, +0.0714] | <0.001 |
| SegFormer, Late (`segformer_late`) | Predictive entropy | 0.7604 | 0.7594 | +0.0010 | [-0.0117, +0.0142] | 0.867 |
| SegFormer, Late (`segformer_late`) | Local gradient UQ | 0.7604 | 0.7423 | +0.0181 | [+0.0043, +0.0326] | 0.009 |
| SegFormer, Late (`segformer_late`) | Standardized max logit | 0.7604 | 0.7381 | +0.0223 | [-0.0027, +0.0490] | 0.082 |
| SegFormer, Late (`segformer_late`) | Max-softmax | 0.7604 | 0.7476 | +0.0128 | [-0.0002, +0.0269] | 0.053 |
| SegFormer, Late (`segformer_late`) | Mahalanobis distance | 0.7604 | 0.5348 | +0.2256 | [+0.1743, +0.2773] | <0.001 |
| SegFormer, Late (`segformer_late`) | Inverse area (control) | 0.7604 | 0.7237 | +0.0367 | [+0.0075, +0.0638] | 0.008 |

49 of 84 comparisons have p below 0.05 (no correction for multiple comparisons).

## nnU-Net + CBAM, Early against every other checkpoint

### Malignant

| Other checkpoint | Method | AUC of the proposed checkpoint | AUC of the other | Difference | 95% interval | p |
|:---|:---|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | MetaSeg | 0.7455 | 0.7520 | -0.0064 | [-0.0445, +0.0357] | 0.762 |
| nnU-Net, Early (`nnunet_early`) | MetaSeg | 0.7455 | 0.7549 | -0.0094 | [-0.0442, +0.0269] | 0.617 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | MetaSeg | 0.7455 | 0.7260 | +0.0195 | [-0.0267, +0.0651] | 0.401 |
| nnU-Net, Mid (`nnunet_mid`) | MetaSeg | 0.7455 | 0.7697 | -0.0242 | [-0.0638, +0.0114] | 0.208 |
| nnU-Net, Late (`nnunet_late`) | MetaSeg | 0.7455 | 0.7731 | -0.0276 | [-0.0672, +0.0112] | 0.161 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | MetaSeg | 0.7455 | 0.7284 | +0.0172 | [-0.0155, +0.0511] | 0.283 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | MetaSeg | 0.7455 | 0.7721 | -0.0265 | [-0.0622, +0.0098] | 0.146 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | MetaSeg | 0.7455 | 0.7688 | -0.0232 | [-0.0560, +0.0084] | 0.175 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | MetaSeg | 0.7455 | 0.7480 | -0.0025 | [-0.0418, +0.0368] | 0.930 |
| SegFormer, single-task (`segformer_single`) | MetaSeg | 0.7455 | 0.7891 | -0.0435 | [-0.0970, +0.0179] | 0.153 |
| SegFormer, Early (`segformer_early`) | MetaSeg | 0.7455 | 0.7968 | -0.0512 | [-0.1210, +0.0289] | 0.204 |
| SegFormer, Mid (`segformer_mid`) | MetaSeg | 0.7455 | 0.7947 | -0.0492 | [-0.1034, +0.0140] | 0.138 |
| SegFormer, Late (`segformer_late`) | MetaSeg | 0.7455 | 0.7712 | -0.0256 | [-0.0908, +0.0532] | 0.518 |

The smallest p is 0.138. No correction for multiple comparisons.

### Benign

| Other checkpoint | Method | AUC of the proposed checkpoint | AUC of the other | Difference | 95% interval | p |
|:---|:---|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | MetaSeg | 0.7285 | 0.7936 | -0.0651 | [-0.1059, -0.0266] | <0.001 |
| nnU-Net, Early (`nnunet_early`) | MetaSeg | 0.7285 | 0.7418 | -0.0134 | [-0.0578, +0.0300] | 0.546 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | MetaSeg | 0.7285 | 0.7426 | -0.0141 | [-0.0549, +0.0254] | 0.508 |
| nnU-Net, Mid (`nnunet_mid`) | MetaSeg | 0.7285 | 0.7943 | -0.0658 | [-0.1040, -0.0265] | <0.001 |
| nnU-Net, Late (`nnunet_late`) | MetaSeg | 0.7285 | 0.7565 | -0.0281 | [-0.0704, +0.0107] | 0.182 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | MetaSeg | 0.7285 | 0.7852 | -0.0567 | [-0.0956, -0.0192] | 0.003 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | MetaSeg | 0.7285 | 0.7849 | -0.0564 | [-0.0917, -0.0234] | <0.001 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | MetaSeg | 0.7285 | 0.7985 | -0.0701 | [-0.1055, -0.0366] | <0.001 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | MetaSeg | 0.7285 | 0.7608 | -0.0323 | [-0.0722, +0.0084] | 0.127 |
| SegFormer, single-task (`segformer_single`) | MetaSeg | 0.7285 | 0.7783 | -0.0498 | [-0.0911, -0.0055] | 0.032 |
| SegFormer, Early (`segformer_early`) | MetaSeg | 0.7285 | 0.7734 | -0.0449 | [-0.0862, -0.0007] | 0.044 |
| SegFormer, Mid (`segformer_mid`) | MetaSeg | 0.7285 | 0.7708 | -0.0423 | [-0.0841, +0.0002] | 0.052 |
| SegFormer, Late (`segformer_late`) | MetaSeg | 0.7285 | 0.7604 | -0.0319 | [-0.0711, +0.0098] | 0.129 |

The smallest p is <0.001. No correction for multiple comparisons.
