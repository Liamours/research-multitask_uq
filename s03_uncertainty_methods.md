# S3. Uncertainty methods in full

Seven region scores are computed for every predicted region of the checkpoints. A higher score means the region is more likely a false positive.

| Method | Region score |
|:---|:---|
| Max-softmax | One minus the mean maximum softmax probability of the region |
| Predictive entropy | Mean normalized Shannon entropy of the softmax output over the region |
| Local gradient UQ | Norm of the gradient of the region's predicted probability with respect to decoder activations |
| MetaSeg | Output of a meta-classifier on region features such as area, entropy, and logit spread |
| Standardized max logit | Mean maximum logit of the region, standardized by its predicted class |
| Mahalanobis distance | Distance of the mean decoder features of the region to the nearest class centroid |
| Inverse area | One over the region area, a control without model confidence |

The paper reports the first four methods. Max-softmax, Mahalanobis distance, and inverse area appear only here. All values are computed on the test split from the UQ run. Region AUC is the probability that a false region scores higher than a true region.

## Pooled region AUC with 95% interval, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.7079 [0.6642, 0.7502] | 0.7180 [0.6783, 0.7593] | 0.7520 [0.7104, 0.7918] | 0.7235 [0.6746, 0.7654] | 0.6984 [0.6574, 0.7406] | 0.5470 [0.5039, 0.5895] | 0.7158 [0.6685, 0.7642] |
| nnU-Net, Early (`nnunet_early`) | 0.6747 [0.6293, 0.7207] | 0.7073 [0.6621, 0.7523] | 0.7549 [0.7044, 0.8016] | 0.7184 [0.6700, 0.7685] | 0.6557 [0.6108, 0.7028] | 0.6476 [0.6001, 0.6951] | 0.7585 [0.7088, 0.8061] |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.6960 [0.6486, 0.7480] | 0.6978 [0.6476, 0.7517] | 0.7260 [0.6737, 0.7803] | 0.6783 [0.6235, 0.7369] | 0.6869 [0.6399, 0.7388] | 0.5075 [0.4522, 0.5598] | 0.7030 [0.6429, 0.7663] |
| nnU-Net, Mid (`nnunet_mid`) | 0.7327 [0.6860, 0.7807] | 0.7255 [0.6762, 0.7760] | 0.7697 [0.7209, 0.8175] | 0.7568 [0.7088, 0.8070] | 0.7252 [0.6794, 0.7730] | 0.4743 [0.4245, 0.5267] | 0.7518 [0.7005, 0.8059] |
| nnU-Net, Late (`nnunet_late`) | 0.7561 [0.7094, 0.8002] | 0.7181 [0.6706, 0.7657] | 0.7731 [0.7150, 0.8337] | 0.7940 [0.7493, 0.8349] | 0.7397 [0.6926, 0.7816] | 0.6644 [0.6155, 0.7117] | 0.7359 [0.6755, 0.7981] |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.6849 [0.6481, 0.7204] | 0.6988 [0.6526, 0.7436] | 0.7284 [0.6824, 0.7731] | 0.7315 [0.6918, 0.7703] | 0.6657 [0.6291, 0.7005] | 0.5442 [0.4963, 0.5893] | 0.7026 [0.6551, 0.7533] |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.6690 [0.6240, 0.7105] | 0.6915 [0.6411, 0.7423] | 0.7455 [0.6940, 0.7976] | 0.7147 [0.6671, 0.7568] | 0.6529 [0.6087, 0.6954] | 0.5486 [0.4993, 0.6035] | 0.7080 [0.6574, 0.7591] |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.6979 [0.6565, 0.7412] | 0.7253 [0.6856, 0.7625] | 0.7721 [0.7278, 0.8145] | 0.7381 [0.6959, 0.7812] | 0.6845 [0.6435, 0.7274] | 0.5291 [0.4780, 0.5837] | 0.7169 [0.6669, 0.7651] |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.7268 [0.6930, 0.7612] | 0.6999 [0.6638, 0.7370] | 0.7688 [0.7280, 0.8113] | 0.7959 [0.7601, 0.8313] | 0.6999 [0.6641, 0.7362] | 0.5609 [0.5160, 0.6111] | 0.7354 [0.6944, 0.7809] |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.7065 [0.6616, 0.7512] | 0.6770 [0.6274, 0.7255] | 0.7480 [0.7033, 0.7904] | 0.7728 [0.7297, 0.8149] | 0.6788 [0.6331, 0.7252] | 0.5718 [0.5159, 0.6282] | 0.7050 [0.6580, 0.7512] |
| SegFormer, single-task (`segformer_single`) | 0.7949 [0.7406, 0.8397] | 0.7733 [0.7171, 0.8159] | 0.7891 [0.7367, 0.8313] | 0.8022 [0.7427, 0.8494] | 0.7849 [0.7283, 0.8297] | 0.4799 [0.4309, 0.5384] | 0.7160 [0.6596, 0.7640] |
| SegFormer, Early (`segformer_early`) | 0.7946 [0.7356, 0.8430] | 0.7788 [0.7204, 0.8297] | 0.7968 [0.7326, 0.8487] | 0.7961 [0.7331, 0.8493] | 0.7802 [0.7224, 0.8296] | 0.4706 [0.4223, 0.5205] | 0.7298 [0.6543, 0.8055] |
| SegFormer, Mid (`segformer_mid`) | 0.7943 [0.7368, 0.8387] | 0.7791 [0.7228, 0.8230] | 0.7947 [0.7400, 0.8369] | 0.7891 [0.7337, 0.8340] | 0.7813 [0.7253, 0.8260] | 0.5055 [0.4524, 0.5560] | 0.7348 [0.6664, 0.7895] |
| SegFormer, Late (`segformer_late`) | 0.7772 [0.7060, 0.8308] | 0.7728 [0.7026, 0.8254] | 0.7712 [0.6990, 0.8244] | 0.7677 [0.6941, 0.8222] | 0.7716 [0.7027, 0.8235] | 0.4810 [0.4192, 0.5479] | 0.7047 [0.6162, 0.7780] |

Pooled over both views. The interval is the 95% bootstrap interval. Source: `tables/uq_discrimination_by_model.csv`.

## Pooled region AUC with 95% interval, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.7997 [0.7691, 0.8311] | 0.7764 [0.7447, 0.8102] | 0.7936 [0.7629, 0.8246] | 0.7708 [0.7340, 0.8046] | 0.7905 [0.7584, 0.8230] | 0.5743 [0.5343, 0.6162] | 0.7335 [0.6964, 0.7718] |
| nnU-Net, Early (`nnunet_early`) | 0.7477 [0.7092, 0.7848] | 0.7211 [0.6799, 0.7585] | 0.7418 [0.7032, 0.7793] | 0.7574 [0.7212, 0.7925] | 0.7388 [0.6986, 0.7771] | 0.5657 [0.5180, 0.6109] | 0.6994 [0.6561, 0.7432] |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.7448 [0.7148, 0.7737] | 0.7136 [0.6824, 0.7434] | 0.7426 [0.7116, 0.7724] | 0.7274 [0.6931, 0.7624] | 0.7316 [0.7005, 0.7607] | 0.4406 [0.4000, 0.4825] | 0.7014 [0.6677, 0.7353] |
| nnU-Net, Mid (`nnunet_mid`) | 0.7978 [0.7666, 0.8299] | 0.7779 [0.7459, 0.8109] | 0.7943 [0.7637, 0.8251] | 0.7624 [0.7282, 0.7936] | 0.7878 [0.7557, 0.8193] | 0.5358 [0.4940, 0.5803] | 0.7487 [0.7129, 0.7839] |
| nnU-Net, Late (`nnunet_late`) | 0.7530 [0.7242, 0.7829] | 0.7298 [0.6990, 0.7605] | 0.7565 [0.7268, 0.7880] | 0.7603 [0.7329, 0.7887] | 0.7433 [0.7138, 0.7733] | 0.5661 [0.5295, 0.6020] | 0.7289 [0.6968, 0.7619] |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.7803 [0.7451, 0.8169] | 0.7617 [0.7279, 0.7967] | 0.7852 [0.7510, 0.8220] | 0.8144 [0.7814, 0.8511] | 0.7680 [0.7318, 0.8065] | 0.5594 [0.5146, 0.6055] | 0.7502 [0.7117, 0.7886] |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.7258 [0.6859, 0.7650] | 0.7118 [0.6728, 0.7514] | 0.7285 [0.6892, 0.7670] | 0.7633 [0.7290, 0.8005] | 0.7071 [0.6663, 0.7485] | 0.5348 [0.4890, 0.5832] | 0.7116 [0.6695, 0.7518] |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.7795 [0.7446, 0.8145] | 0.7667 [0.7325, 0.8021] | 0.7849 [0.7510, 0.8195] | 0.7967 [0.7631, 0.8317] | 0.7685 [0.7314, 0.8048] | 0.5679 [0.5240, 0.6130] | 0.7294 [0.6913, 0.7680] |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.7920 [0.7628, 0.8238] | 0.7668 [0.7373, 0.7971] | 0.7985 [0.7696, 0.8300] | 0.8098 [0.7778, 0.8448] | 0.7782 [0.7482, 0.8107] | 0.5838 [0.5435, 0.6255] | 0.7490 [0.7133, 0.7851] |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.7523 [0.7239, 0.7810] | 0.7403 [0.7113, 0.7695] | 0.7608 [0.7316, 0.7902] | 0.7627 [0.7345, 0.7905] | 0.7386 [0.7099, 0.7675] | 0.6060 [0.5705, 0.6411] | 0.7394 [0.7109, 0.7689] |
| SegFormer, single-task (`segformer_single`) | 0.7724 [0.7426, 0.8005] | 0.7513 [0.7199, 0.7816] | 0.7783 [0.7478, 0.8057] | 0.7165 [0.6833, 0.7500] | 0.7674 [0.7356, 0.7972] | 0.4785 [0.4382, 0.5181] | 0.7316 [0.7017, 0.7626] |
| SegFormer, Early (`segformer_early`) | 0.7712 [0.7419, 0.8014] | 0.7545 [0.7238, 0.7855] | 0.7734 [0.7427, 0.8034] | 0.7127 [0.6786, 0.7447] | 0.7621 [0.7323, 0.7933] | 0.5133 [0.4752, 0.5518] | 0.7328 [0.7027, 0.7634] |
| SegFormer, Mid (`segformer_mid`) | 0.7671 [0.7378, 0.7976] | 0.7501 [0.7193, 0.7812] | 0.7708 [0.7420, 0.8001] | 0.7190 [0.6861, 0.7515] | 0.7620 [0.7329, 0.7923] | 0.5077 [0.4684, 0.5489] | 0.7230 [0.6901, 0.7555] |
| SegFormer, Late (`segformer_late`) | 0.7594 [0.7304, 0.7908] | 0.7423 [0.7123, 0.7761] | 0.7604 [0.7298, 0.7926] | 0.7381 [0.7065, 0.7692] | 0.7476 [0.7187, 0.7788] | 0.5348 [0.4946, 0.5748] | 0.7237 [0.6917, 0.7563] |

Pooled over both views. The interval is the 95% bootstrap interval. Source: `tables/uq_discrimination_by_model.csv`.

## Mean region AUC over the two views, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.7067 | 0.7145 | 0.7540 | 0.7246 | 0.6967 | 0.5449 | 0.7159 |
| nnU-Net, Early (`nnunet_early`) | 0.6684 | 0.7041 | 0.7550 | 0.7182 | 0.6474 | 0.6345 | 0.7563 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.6927 | 0.6962 | 0.7236 | 0.6788 | 0.6823 | 0.4878 | 0.7010 |
| nnU-Net, Mid (`nnunet_mid`) | 0.7294 | 0.7199 | 0.7662 | 0.7540 | 0.7221 | 0.4782 | 0.7458 |
| nnU-Net, Late (`nnunet_late`) | 0.7617 | 0.7226 | 0.7730 | 0.8017 | 0.7446 | 0.6633 | 0.7338 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.6923 | 0.7042 | 0.7360 | 0.7324 | 0.6731 | 0.5434 | 0.7041 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.6766 | 0.6955 | 0.7458 | 0.7126 | 0.6611 | 0.5334 | 0.7042 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.7019 | 0.7289 | 0.7771 | 0.7367 | 0.6882 | 0.5239 | 0.7170 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.7269 | 0.7037 | 0.7711 | 0.7971 | 0.7003 | 0.5606 | 0.7358 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.7082 | 0.6817 | 0.7519 | 0.7760 | 0.6809 | 0.5727 | 0.7077 |
| SegFormer, single-task (`segformer_single`) | 0.7935 | 0.7717 | 0.7899 | 0.8021 | 0.7826 | 0.4797 | 0.7160 |
| SegFormer, Early (`segformer_early`) | 0.7938 | 0.7775 | 0.7963 | 0.7957 | 0.7791 | 0.4709 | 0.7293 |
| SegFormer, Mid (`segformer_mid`) | 0.7940 | 0.7794 | 0.7943 | 0.7906 | 0.7810 | 0.5077 | 0.7354 |
| SegFormer, Late (`segformer_late`) | 0.7774 | 0.7723 | 0.7675 | 0.7684 | 0.7726 | 0.4819 | 0.7047 |

Higher is better. Source: `tables/uq_discrimination_by_model.csv`.

## Mean region AUC over the two views, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.7996 | 0.7746 | 0.7943 | 0.7710 | 0.7894 | 0.5734 | 0.7298 |
| nnU-Net, Early (`nnunet_early`) | 0.7513 | 0.7263 | 0.7458 | 0.7582 | 0.7420 | 0.5645 | 0.6998 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.7438 | 0.7126 | 0.7422 | 0.7385 | 0.7299 | 0.4651 | 0.6965 |
| nnU-Net, Mid (`nnunet_mid`) | 0.7986 | 0.7816 | 0.7974 | 0.7605 | 0.7886 | 0.5380 | 0.7480 |
| nnU-Net, Late (`nnunet_late`) | 0.7634 | 0.7422 | 0.7627 | 0.7706 | 0.7537 | 0.5586 | 0.7251 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.7870 | 0.7681 | 0.7838 | 0.8139 | 0.7720 | 0.5548 | 0.7493 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.7199 | 0.7113 | 0.7230 | 0.7546 | 0.7018 | 0.5342 | 0.7073 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.7815 | 0.7712 | 0.7858 | 0.7971 | 0.7698 | 0.5669 | 0.7286 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.7917 | 0.7710 | 0.7982 | 0.8099 | 0.7782 | 0.5839 | 0.7485 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.7466 | 0.7380 | 0.7423 | 0.7654 | 0.7323 | 0.5755 | 0.7208 |
| SegFormer, single-task (`segformer_single`) | 0.7783 | 0.7580 | 0.7783 | 0.7225 | 0.7729 | 0.4957 | 0.7252 |
| SegFormer, Early (`segformer_early`) | 0.7774 | 0.7600 | 0.7784 | 0.7231 | 0.7691 | 0.5328 | 0.7303 |
| SegFormer, Mid (`segformer_mid`) | 0.7727 | 0.7558 | 0.7762 | 0.7302 | 0.7666 | 0.5319 | 0.7201 |
| SegFormer, Late (`segformer_late`) | 0.7679 | 0.7485 | 0.7675 | 0.7538 | 0.7550 | 0.5429 | 0.7241 |

Higher is better. Source: `tables/uq_discrimination_by_model.csv`.

## Mean false-positive rate at 95% true-positive rate, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.8195 | 0.7944 | 0.8176 | 0.8455 | 0.8253 | 0.9105 | 0.8459 |
| nnU-Net, Early (`nnunet_early`) | 0.8214 | 0.8260 | 0.7986 | 0.8187 | 0.8422 | 0.8864 | 0.7958 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.8523 | 0.8698 | 0.8358 | 0.8479 | 0.8677 | 0.9527 | 0.8421 |
| nnU-Net, Mid (`nnunet_mid`) | 0.8186 | 0.8547 | 0.8176 | 0.8240 | 0.8194 | 0.9520 | 0.8252 |
| nnU-Net, Late (`nnunet_late`) | 0.7435 | 0.7757 | 0.7503 | 0.7213 | 0.7258 | 0.9099 | 0.7352 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.7939 | 0.7909 | 0.7604 | 0.7739 | 0.7996 | 0.8709 | 0.7948 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.8003 | 0.8040 | 0.7430 | 0.7716 | 0.8053 | 0.9099 | 0.8158 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.8223 | 0.8142 | 0.7150 | 0.8229 | 0.8247 | 0.9153 | 0.8401 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.7614 | 0.7536 | 0.8058 | 0.7339 | 0.7692 | 0.9285 | 0.8389 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.8078 | 0.8110 | 0.7039 | 0.7995 | 0.8022 | 0.9328 | 0.7988 |
| SegFormer, single-task (`segformer_single`) | 0.8261 | 0.7963 | 0.7784 | 0.7401 | 0.8089 | 0.9606 | 0.8166 |
| SegFormer, Early (`segformer_early`) | 0.7633 | 0.7392 | 0.7783 | 0.8223 | 0.7781 | 0.9804 | 0.8031 |
| SegFormer, Mid (`segformer_mid`) | 0.7802 | 0.6955 | 0.8029 | 0.8382 | 0.7512 | 0.9594 | 0.7727 |
| SegFormer, Late (`segformer_late`) | 0.8492 | 0.8038 | 0.8276 | 0.9220 | 0.8657 | 0.9890 | 0.8501 |

Share of false regions still kept when 95% of the true regions are kept. Lower is better. Source: `tables/uq_discrimination_by_model.csv`.

## Mean false-positive rate at 95% true-positive rate, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.7091 | 0.6965 | 0.7167 | 0.7673 | 0.7033 | 0.9141 | 0.7145 |
| nnU-Net, Early (`nnunet_early`) | 0.8029 | 0.8080 | 0.7701 | 0.8029 | 0.7916 | 0.8633 | 0.8080 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.8299 | 0.8704 | 0.8627 | 0.8578 | 0.8258 | 0.9240 | 0.8622 |
| nnU-Net, Mid (`nnunet_mid`) | 0.6782 | 0.7083 | 0.6742 | 0.7644 | 0.7052 | 0.9044 | 0.7535 |
| nnU-Net, Late (`nnunet_late`) | 0.8001 | 0.8273 | 0.8068 | 0.7979 | 0.8008 | 0.9177 | 0.8161 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.6993 | 0.6660 | 0.7178 | 0.7046 | 0.7059 | 0.8591 | 0.6999 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.8022 | 0.7649 | 0.8553 | 0.8096 | 0.7947 | 0.8719 | 0.7919 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.6854 | 0.7368 | 0.7305 | 0.6494 | 0.7095 | 0.8679 | 0.7413 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.6550 | 0.6603 | 0.6405 | 0.6356 | 0.6501 | 0.8625 | 0.7121 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.8141 | 0.8133 | 0.8079 | 0.8246 | 0.8035 | 0.9060 | 0.8218 |
| SegFormer, single-task (`segformer_single`) | 0.7357 | 0.8168 | 0.7274 | 0.8425 | 0.7409 | 0.9270 | 0.7906 |
| SegFormer, Early (`segformer_early`) | 0.7753 | 0.8096 | 0.7893 | 0.8209 | 0.8033 | 0.9076 | 0.8168 |
| SegFormer, Mid (`segformer_mid`) | 0.7616 | 0.8161 | 0.7550 | 0.8160 | 0.7715 | 0.8993 | 0.8161 |
| SegFormer, Late (`segformer_late`) | 0.7874 | 0.8628 | 0.7806 | 0.7769 | 0.8052 | 0.9190 | 0.8171 |

Share of false regions still kept when 95% of the true regions are kept. Lower is better. Source: `tables/uq_discrimination_by_model.csv`.

## Mean average precision for false regions, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.7228 | 0.7450 | 0.7608 | 0.7242 | 0.7225 | 0.6060 | 0.7439 |
| nnU-Net, Early (`nnunet_early`) | 0.5881 | 0.6172 | 0.6565 | 0.6121 | 0.5756 | 0.5277 | 0.6498 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.5322 | 0.5179 | 0.5456 | 0.5092 | 0.5238 | 0.3442 | 0.5271 |
| nnU-Net, Mid (`nnunet_mid`) | 0.7062 | 0.6962 | 0.7321 | 0.7218 | 0.7010 | 0.4951 | 0.7067 |
| nnU-Net, Late (`nnunet_late`) | 0.6166 | 0.5740 | 0.6266 | 0.6682 | 0.5999 | 0.4771 | 0.5858 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.7143 | 0.7188 | 0.7361 | 0.7382 | 0.6995 | 0.5962 | 0.7144 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.6258 | 0.6489 | 0.6894 | 0.6499 | 0.6206 | 0.5125 | 0.6418 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.6652 | 0.6986 | 0.7520 | 0.6783 | 0.6554 | 0.5243 | 0.6835 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.6835 | 0.6759 | 0.7081 | 0.7376 | 0.6662 | 0.5125 | 0.6794 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.6213 | 0.5842 | 0.6545 | 0.6730 | 0.5932 | 0.4507 | 0.6059 |
| SegFormer, single-task (`segformer_single`) | 0.6150 | 0.6047 | 0.6276 | 0.6231 | 0.6035 | 0.3182 | 0.5663 |
| SegFormer, Early (`segformer_early`) | 0.6155 | 0.5888 | 0.6174 | 0.5843 | 0.6050 | 0.2951 | 0.5885 |
| SegFormer, Mid (`segformer_mid`) | 0.6369 | 0.6571 | 0.6340 | 0.5997 | 0.6393 | 0.3593 | 0.6191 |
| SegFormer, Late (`segformer_late`) | 0.5072 | 0.5233 | 0.5089 | 0.4746 | 0.5227 | 0.2646 | 0.4831 |

Average precision of ranking false regions above true regions. Higher is better. Source: `tables/uq_discrimination_by_model.csv`.

## Mean average precision for false regions, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.6652 | 0.6333 | 0.6524 | 0.6079 | 0.6547 | 0.3923 | 0.6000 |
| nnU-Net, Early (`nnunet_early`) | 0.5473 | 0.5380 | 0.5448 | 0.5200 | 0.5542 | 0.3849 | 0.5006 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.5518 | 0.5231 | 0.5443 | 0.5377 | 0.5488 | 0.3499 | 0.5195 |
| nnU-Net, Mid (`nnunet_mid`) | 0.6836 | 0.6680 | 0.6765 | 0.6221 | 0.6790 | 0.4123 | 0.6385 |
| nnU-Net, Late (`nnunet_late`) | 0.5789 | 0.5624 | 0.5706 | 0.5782 | 0.5783 | 0.4144 | 0.5569 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.6626 | 0.6523 | 0.6426 | 0.6836 | 0.6565 | 0.4381 | 0.6315 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.5143 | 0.5134 | 0.4964 | 0.5553 | 0.5046 | 0.3732 | 0.5051 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.6342 | 0.6298 | 0.6172 | 0.6562 | 0.6192 | 0.4386 | 0.5933 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.6600 | 0.6499 | 0.6561 | 0.6830 | 0.6510 | 0.4462 | 0.6181 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.5830 | 0.5683 | 0.5699 | 0.5905 | 0.5771 | 0.4300 | 0.5684 |
| SegFormer, single-task (`segformer_single`) | 0.6346 | 0.5737 | 0.6266 | 0.5499 | 0.6255 | 0.3456 | 0.5654 |
| SegFormer, Early (`segformer_early`) | 0.6024 | 0.5716 | 0.6053 | 0.5377 | 0.5905 | 0.3743 | 0.5564 |
| SegFormer, Mid (`segformer_mid`) | 0.6023 | 0.5700 | 0.6101 | 0.5383 | 0.6017 | 0.3969 | 0.5665 |
| SegFormer, Late (`segformer_late`) | 0.5829 | 0.5345 | 0.5876 | 0.5805 | 0.5693 | 0.3829 | 0.5541 |

Average precision of ranking false regions above true regions. Higher is better. Source: `tables/uq_discrimination_by_model.csv`.

## Region AUC per view, malignant

| Checkpoint | View | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | anterior | 0.6911 | 0.6917 | 0.7333 | 0.7274 | 0.6789 | 0.5294 | 0.7056 |
| nnU-Net, single-task (`nnunet_single`) | posterior | 0.7223 | 0.7373 | 0.7746 | 0.7219 | 0.7145 | 0.5604 | 0.7262 |
| nnU-Net, Early (`nnunet_early`) | anterior | 0.6976 | 0.7196 | 0.7398 | 0.7326 | 0.6812 | 0.6460 | 0.7543 |
| nnU-Net, Early (`nnunet_early`) | posterior | 0.6392 | 0.6887 | 0.7703 | 0.7037 | 0.6136 | 0.6230 | 0.7583 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | anterior | 0.6811 | 0.6837 | 0.6792 | 0.6749 | 0.6671 | 0.4660 | 0.7088 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | posterior | 0.7044 | 0.7087 | 0.7679 | 0.6827 | 0.6974 | 0.5095 | 0.6932 |
| nnU-Net, Mid (`nnunet_mid`) | anterior | 0.7266 | 0.7337 | 0.7566 | 0.7567 | 0.7217 | 0.4040 | 0.7604 |
| nnU-Net, Mid (`nnunet_mid`) | posterior | 0.7321 | 0.7062 | 0.7758 | 0.7514 | 0.7224 | 0.5524 | 0.7312 |
| nnU-Net, Late (`nnunet_late`) | anterior | 0.7167 | 0.6856 | 0.7486 | 0.7734 | 0.6967 | 0.6583 | 0.7265 |
| nnU-Net, Late (`nnunet_late`) | posterior | 0.8067 | 0.7596 | 0.7973 | 0.8300 | 0.7926 | 0.6682 | 0.7411 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | anterior | 0.6956 | 0.7087 | 0.7279 | 0.7657 | 0.6675 | 0.5397 | 0.7165 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | posterior | 0.6891 | 0.6997 | 0.7442 | 0.6991 | 0.6787 | 0.5471 | 0.6916 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | anterior | 0.6832 | 0.7110 | 0.7469 | 0.7312 | 0.6643 | 0.5493 | 0.7524 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | posterior | 0.6699 | 0.6800 | 0.7448 | 0.6941 | 0.6578 | 0.5174 | 0.6561 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | anterior | 0.7156 | 0.7331 | 0.7572 | 0.7638 | 0.6960 | 0.5127 | 0.7203 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | posterior | 0.6882 | 0.7248 | 0.7971 | 0.7097 | 0.6804 | 0.5352 | 0.7136 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | anterior | 0.7152 | 0.6993 | 0.7527 | 0.7878 | 0.6922 | 0.5008 | 0.7267 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | posterior | 0.7386 | 0.7081 | 0.7896 | 0.8064 | 0.7085 | 0.6205 | 0.7450 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | anterior | 0.7104 | 0.6869 | 0.7296 | 0.7790 | 0.6832 | 0.5858 | 0.7060 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | posterior | 0.7059 | 0.6765 | 0.7742 | 0.7729 | 0.6786 | 0.5596 | 0.7095 |
| SegFormer, single-task (`segformer_single`) | anterior | 0.7805 | 0.7714 | 0.7606 | 0.7902 | 0.7742 | 0.4458 | 0.7150 |
| SegFormer, single-task (`segformer_single`) | posterior | 0.8065 | 0.7719 | 0.8192 | 0.8140 | 0.7910 | 0.5136 | 0.7170 |
| SegFormer, Early (`segformer_early`) | anterior | 0.7737 | 0.7564 | 0.7651 | 0.7827 | 0.7549 | 0.4083 | 0.6984 |
| SegFormer, Early (`segformer_early`) | posterior | 0.8139 | 0.7986 | 0.8276 | 0.8087 | 0.8033 | 0.5335 | 0.7602 |
| SegFormer, Mid (`segformer_mid`) | anterior | 0.8045 | 0.7929 | 0.7887 | 0.8050 | 0.7918 | 0.4687 | 0.7340 |
| SegFormer, Mid (`segformer_mid`) | posterior | 0.7836 | 0.7659 | 0.8000 | 0.7761 | 0.7703 | 0.5467 | 0.7369 |
| SegFormer, Late (`segformer_late`) | anterior | 0.7498 | 0.7443 | 0.7250 | 0.7394 | 0.7464 | 0.4598 | 0.6661 |
| SegFormer, Late (`segformer_late`) | posterior | 0.8049 | 0.8003 | 0.8101 | 0.7973 | 0.7988 | 0.5040 | 0.7432 |

Source: `tables/uq_discrimination_by_config.csv`, which also holds the false-positive rate, average precision, and region counts per view.

## Region AUC per view, benign

| Checkpoint | View | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | anterior | 0.8007 | 0.7654 | 0.7864 | 0.7767 | 0.7799 | 0.6014 | 0.7363 |
| nnU-Net, single-task (`nnunet_single`) | posterior | 0.7985 | 0.7837 | 0.8022 | 0.7652 | 0.7989 | 0.5455 | 0.7233 |
| nnU-Net, Early (`nnunet_early`) | anterior | 0.7398 | 0.7062 | 0.7246 | 0.7574 | 0.7283 | 0.5767 | 0.6976 |
| nnU-Net, Early (`nnunet_early`) | posterior | 0.7628 | 0.7463 | 0.7670 | 0.7590 | 0.7557 | 0.5523 | 0.7021 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | anterior | 0.7378 | 0.7127 | 0.7402 | 0.7130 | 0.7258 | 0.4230 | 0.6973 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | posterior | 0.7498 | 0.7125 | 0.7442 | 0.7640 | 0.7340 | 0.5071 | 0.6957 |
| nnU-Net, Mid (`nnunet_mid`) | anterior | 0.7890 | 0.7794 | 0.7965 | 0.7870 | 0.7800 | 0.5108 | 0.7537 |
| nnU-Net, Mid (`nnunet_mid`) | posterior | 0.8082 | 0.7838 | 0.7984 | 0.7341 | 0.7971 | 0.5652 | 0.7422 |
| nnU-Net, Late (`nnunet_late`) | anterior | 0.7323 | 0.7118 | 0.7337 | 0.7460 | 0.7237 | 0.5827 | 0.7211 |
| nnU-Net, Late (`nnunet_late`) | posterior | 0.7945 | 0.7726 | 0.7917 | 0.7951 | 0.7836 | 0.5344 | 0.7291 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | anterior | 0.7795 | 0.7580 | 0.7690 | 0.8316 | 0.7606 | 0.5680 | 0.7419 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | posterior | 0.7945 | 0.7782 | 0.7987 | 0.7962 | 0.7834 | 0.5415 | 0.7568 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | anterior | 0.7601 | 0.7454 | 0.7492 | 0.7998 | 0.7392 | 0.5571 | 0.7345 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | posterior | 0.6797 | 0.6772 | 0.6968 | 0.7095 | 0.6644 | 0.5113 | 0.6802 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | anterior | 0.7692 | 0.7521 | 0.7754 | 0.8070 | 0.7562 | 0.5813 | 0.7339 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | posterior | 0.7937 | 0.7903 | 0.7963 | 0.7873 | 0.7834 | 0.5525 | 0.7233 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | anterior | 0.7999 | 0.7838 | 0.8021 | 0.8266 | 0.7884 | 0.5735 | 0.7545 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | posterior | 0.7834 | 0.7581 | 0.7944 | 0.7932 | 0.7681 | 0.5943 | 0.7424 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | anterior | 0.7485 | 0.7333 | 0.7509 | 0.7585 | 0.7360 | 0.6116 | 0.7402 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | posterior | 0.7447 | 0.7427 | 0.7336 | 0.7723 | 0.7287 | 0.5394 | 0.7015 |
| SegFormer, single-task (`segformer_single`) | anterior | 0.7520 | 0.7308 | 0.7619 | 0.7197 | 0.7482 | 0.4727 | 0.7248 |
| SegFormer, single-task (`segformer_single`) | posterior | 0.8045 | 0.7853 | 0.7946 | 0.7252 | 0.7977 | 0.5187 | 0.7257 |
| SegFormer, Early (`segformer_early`) | anterior | 0.7521 | 0.7361 | 0.7521 | 0.7029 | 0.7432 | 0.5041 | 0.7251 |
| SegFormer, Early (`segformer_early`) | posterior | 0.8028 | 0.7840 | 0.8047 | 0.7433 | 0.7949 | 0.5616 | 0.7354 |
| SegFormer, Mid (`segformer_mid`) | anterior | 0.7501 | 0.7353 | 0.7512 | 0.7087 | 0.7464 | 0.4934 | 0.7157 |
| SegFormer, Mid (`segformer_mid`) | posterior | 0.7952 | 0.7764 | 0.8012 | 0.7518 | 0.7868 | 0.5704 | 0.7245 |
| SegFormer, Late (`segformer_late`) | anterior | 0.7390 | 0.7272 | 0.7356 | 0.7208 | 0.7279 | 0.5362 | 0.7156 |
| SegFormer, Late (`segformer_late`) | posterior | 0.7968 | 0.7698 | 0.7994 | 0.7868 | 0.7821 | 0.5496 | 0.7327 |

Source: `tables/uq_discrimination_by_config.csv`, which also holds the false-positive rate, average precision, and region counts per view.

## Filtering at the threshold of the validation split

A region is removed when its score is above the 95th percentile of the true-region scores of the validation split, fitted for each method, view, and class. Region sensitivity is the share of true regions kept. Region specificity is the share of false regions removed. FROC sensitivity is the hotspot sensitivity at 0.5 false positives per case when regions are removed in decreasing order of score, and the last column is the same with random order.

### Region sensitivity, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.9159 | 0.9375 | 0.9471 | 0.9279 | 0.9231 | 0.9183 | 0.9543 |
| nnU-Net, Early (`nnunet_early`) | 0.9398 | 0.9348 | 0.9373 | 0.9574 | 0.9474 | 0.9123 | 0.9298 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.9304 | 0.9330 | 0.9124 | 0.9459 | 0.9304 | 0.8892 | 0.9407 |
| nnU-Net, Mid (`nnunet_mid`) | 0.9319 | 0.9343 | 0.9366 | 0.9413 | 0.9343 | 0.9061 | 0.9554 |
| nnU-Net, Late (`nnunet_late`) | 0.9751 | 0.9751 | 0.9626 | 0.9601 | 0.9800 | 0.9601 | 0.9651 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.9456 | 0.9456 | 0.9385 | 0.9504 | 0.9409 | 0.9173 | 0.9527 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.9395 | 0.9327 | 0.9395 | 0.9395 | 0.9327 | 0.8722 | 0.9260 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.9501 | 0.9524 | 0.9637 | 0.9456 | 0.9433 | 0.9138 | 0.9592 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.9474 | 0.9402 | 0.9211 | 0.9498 | 0.9545 | 0.9091 | 0.9450 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.9661 | 0.9613 | 0.9661 | 0.9782 | 0.9637 | 0.9346 | 0.9709 |
| SegFormer, single-task (`segformer_single`) | 0.9276 | 0.9452 | 0.9298 | 0.9254 | 0.9364 | 0.6842 | 0.9254 |
| SegFormer, Early (`segformer_early`) | 0.9434 | 0.9502 | 0.9344 | 0.9299 | 0.9434 | 0.6810 | 0.9638 |
| SegFormer, Mid (`segformer_mid`) | 0.9303 | 0.9447 | 0.9385 | 0.9242 | 0.9344 | 0.6967 | 0.9426 |
| SegFormer, Late (`segformer_late`) | 0.9404 | 0.9316 | 0.9249 | 0.9139 | 0.9338 | 0.6380 | 0.9338 |

### Region specificity, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.2297 | 0.2158 | 0.1941 | 0.2099 | 0.2277 | 0.1564 | 0.1743 |
| nnU-Net, Early (`nnunet_early`) | 0.1934 | 0.2153 | 0.2409 | 0.1423 | 0.1861 | 0.2080 | 0.2518 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.1520 | 0.1667 | 0.2304 | 0.1569 | 0.1618 | 0.0784 | 0.1422 |
| nnU-Net, Mid (`nnunet_mid`) | 0.2175 | 0.2080 | 0.2340 | 0.1986 | 0.2033 | 0.0851 | 0.1655 |
| nnU-Net, Late (`nnunet_late`) | 0.1872 | 0.1330 | 0.2167 | 0.2069 | 0.1675 | 0.0887 | 0.1823 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.2229 | 0.2272 | 0.2590 | 0.2442 | 0.2335 | 0.1614 | 0.2059 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.2589 | 0.2725 | 0.2670 | 0.2480 | 0.2262 | 0.1989 | 0.2480 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.1742 | 0.1793 | 0.2601 | 0.1717 | 0.1717 | 0.1237 | 0.1439 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.2456 | 0.2426 | 0.3254 | 0.2456 | 0.2456 | 0.1302 | 0.2130 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.1556 | 0.1444 | 0.2074 | 0.1222 | 0.1407 | 0.0926 | 0.1222 |
| SegFormer, single-task (`segformer_single`) | 0.2763 | 0.2193 | 0.3377 | 0.3070 | 0.2412 | 0.2193 | 0.2982 |
| SegFormer, Early (`segformer_early`) | 0.2414 | 0.2562 | 0.2463 | 0.2167 | 0.2167 | 0.2562 | 0.1872 |
| SegFormer, Mid (`segformer_mid`) | 0.3077 | 0.3114 | 0.3407 | 0.2125 | 0.3114 | 0.2967 | 0.2601 |
| SegFormer, Late (`segformer_late`) | 0.1899 | 0.2123 | 0.2458 | 0.2179 | 0.2235 | 0.3296 | 0.2346 |

### FROC sensitivity at 0.5 false positives per case, malignant

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) | Random removal |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.3528 | 0.3499 | 0.3954 | 0.3784 | 0.3414 | 0.1750 | 0.3713 | 0.1716 |
| nnU-Net, Early (`nnunet_early`) | 0.4438 | 0.4623 | 0.4794 | 0.4595 | 0.4324 | 0.4040 | 0.4836 | 0.2971 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.4680 | 0.4708 | 0.4765 | 0.4623 | 0.4651 | 0.4026 | 0.4780 | 0.3715 |
| nnU-Net, Mid (`nnunet_mid`) | 0.4225 | 0.4125 | 0.4481 | 0.4253 | 0.4168 | 0.1778 | 0.4395 | 0.2110 |
| nnU-Net, Late (`nnunet_late`) | 0.5192 | 0.5178 | 0.5249 | 0.5334 | 0.5149 | 0.4822 | 0.5292 | 0.4011 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.3300 | 0.3471 | 0.3414 | 0.3812 | 0.3158 | 0.1750 | 0.3485 | 0.1860 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.4154 | 0.4324 | 0.4794 | 0.4282 | 0.3969 | 0.2703 | 0.4296 | 0.2530 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.4196 | 0.4509 | 0.4836 | 0.4452 | 0.4026 | 0.2347 | 0.4339 | 0.2272 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.4566 | 0.4267 | 0.4836 | 0.4737 | 0.4395 | 0.3115 | 0.4723 | 0.2521 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.4794 | 0.4737 | 0.5064 | 0.4964 | 0.4680 | 0.3969 | 0.4893 | 0.3094 |
| SegFormer, single-task (`segformer_single`) | 0.5832 | 0.5775 | 0.5875 | 0.5605 | 0.5804 | 0.3912 | 0.5676 | 0.4022 |
| SegFormer, Early (`segformer_early`) | 0.5789 | 0.5875 | 0.5832 | 0.5676 | 0.5818 | 0.4026 | 0.5861 | 0.4464 |
| SegFormer, Mid (`segformer_mid`) | 0.6131 | 0.6117 | 0.6088 | 0.5832 | 0.6174 | 0.3642 | 0.6088 | 0.3753 |
| SegFormer, Late (`segformer_late`) | 0.5989 | 0.6017 | 0.5932 | 0.5775 | 0.5989 | 0.4708 | 0.6060 | 0.4942 |

Source: `tables/filtering_effects.csv`. Region specificity is one minus the false regions left after filtering over the false regions before.

### Region sensitivity, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.9206 | 0.9254 | 0.9159 | 0.9365 | 0.9222 | 0.9365 | 0.9476 |
| nnU-Net, Early (`nnunet_early`) | 0.9331 | 0.9255 | 0.9195 | 0.9468 | 0.9331 | 0.9301 | 0.9483 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.9401 | 0.9503 | 0.9325 | 0.9325 | 0.9465 | 0.9567 | 0.9363 |
| nnU-Net, Mid (`nnunet_mid`) | 0.9424 | 0.9470 | 0.9470 | 0.9394 | 0.9470 | 0.9576 | 0.9470 |
| nnU-Net, Late (`nnunet_late`) | 0.9580 | 0.9414 | 0.9363 | 0.9580 | 0.9592 | 0.9363 | 0.9516 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.9468 | 0.9468 | 0.9419 | 0.9500 | 0.9452 | 0.9565 | 0.9597 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.9422 | 0.9468 | 0.9149 | 0.9590 | 0.9438 | 0.9498 | 0.9666 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.9415 | 0.9477 | 0.9477 | 0.9554 | 0.9400 | 0.9415 | 0.9492 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.9402 | 0.9540 | 0.9371 | 0.9371 | 0.9448 | 0.9555 | 0.9586 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.9627 | 0.9723 | 0.9373 | 0.9518 | 0.9602 | 0.9602 | 0.9771 |
| SegFormer, single-task (`segformer_single`) | 0.9474 | 0.9237 | 0.9500 | 0.9421 | 0.9461 | 0.9158 | 0.9553 |
| SegFormer, Early (`segformer_early`) | 0.9521 | 0.9421 | 0.9446 | 0.9710 | 0.9471 | 0.8678 | 0.9547 |
| SegFormer, Mid (`segformer_mid`) | 0.9609 | 0.9444 | 0.9470 | 0.9571 | 0.9545 | 0.8674 | 0.9722 |
| SegFormer, Late (`segformer_late`) | 0.9552 | 0.9334 | 0.9475 | 0.9654 | 0.9590 | 0.8566 | 0.9590 |

### Region specificity, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) |
|:---|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.3729 | 0.3564 | 0.3498 | 0.2508 | 0.3531 | 0.1221 | 0.2937 |
| nnU-Net, Early (`nnunet_early`) | 0.2483 | 0.2762 | 0.3462 | 0.1818 | 0.2448 | 0.1538 | 0.1993 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.2000 | 0.1310 | 0.2190 | 0.1881 | 0.1786 | 0.0619 | 0.1857 |
| nnU-Net, Mid (`nnunet_mid`) | 0.3421 | 0.3079 | 0.3211 | 0.2737 | 0.3000 | 0.0763 | 0.2711 |
| nnU-Net, Late (`nnunet_late`) | 0.1770 | 0.1793 | 0.1701 | 0.1540 | 0.1586 | 0.0989 | 0.2000 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.3135 | 0.3135 | 0.3103 | 0.2978 | 0.3166 | 0.1348 | 0.2633 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.2158 | 0.2374 | 0.2446 | 0.1942 | 0.2266 | 0.1151 | 0.1619 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.3013 | 0.2980 | 0.2947 | 0.3278 | 0.2914 | 0.1490 | 0.2550 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.3529 | 0.3206 | 0.3824 | 0.3765 | 0.3235 | 0.1294 | 0.2500 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.1255 | 0.1023 | 0.2085 | 0.1390 | 0.1409 | 0.0714 | 0.0946 |
| SegFormer, single-task (`segformer_single`) | 0.2250 | 0.2425 | 0.2175 | 0.1525 | 0.2175 | 0.1175 | 0.1850 |
| SegFormer, Early (`segformer_early`) | 0.1838 | 0.2059 | 0.2157 | 0.1250 | 0.1936 | 0.1691 | 0.1765 |
| SegFormer, Mid (`segformer_mid`) | 0.1624 | 0.1718 | 0.1929 | 0.1412 | 0.1929 | 0.2024 | 0.1176 |
| SegFormer, Late (`segformer_late`) | 0.1762 | 0.1687 | 0.2035 | 0.1290 | 0.1538 | 0.2233 | 0.1390 |

### FROC sensitivity at 0.5 false positives per case, benign

| Checkpoint | Predictive entropy | Local gradient UQ | MetaSeg | Standardized max logit | Max-softmax | Mahalanobis distance | Inverse area (control) | Random removal |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| nnU-Net, single-task (`nnunet_single`) | 0.4290 | 0.4371 | 0.4331 | 0.3976 | 0.4379 | 0.2879 | 0.4153 | 0.2455 |
| nnU-Net, Early (`nnunet_early`) | 0.4444 | 0.4387 | 0.4395 | 0.4355 | 0.4516 | 0.3185 | 0.4194 | 0.2530 |
| nnU-Net, Early-Mid (`nnunet_earlymid`) | 0.4492 | 0.4202 | 0.4492 | 0.3960 | 0.4395 | 0.1556 | 0.3911 | 0.2080 |
| nnU-Net, Mid (`nnunet_mid`) | 0.4355 | 0.4169 | 0.4347 | 0.3976 | 0.4258 | 0.2121 | 0.3831 | 0.1977 |
| nnU-Net, Late (`nnunet_late`) | 0.4355 | 0.4234 | 0.4460 | 0.4508 | 0.4419 | 0.2629 | 0.4137 | 0.2015 |
| nnU-Net + CBAM, single-task (`nnunetcbam_single`) | 0.4145 | 0.4129 | 0.4323 | 0.4411 | 0.4169 | 0.2750 | 0.4016 | 0.2248 |
| nnU-Net + CBAM, Early (`nnunetcbam_multidecoder`) | 0.4379 | 0.4153 | 0.4323 | 0.4524 | 0.4331 | 0.2976 | 0.4226 | 0.2609 |
| nnU-Net + CBAM, Early-Mid (`nnunetcbam_earlymid`) | 0.4581 | 0.4484 | 0.4613 | 0.4694 | 0.4605 | 0.2944 | 0.4081 | 0.2510 |
| nnU-Net + CBAM, Mid (`nnunetcbam_mid`) | 0.4363 | 0.4202 | 0.4339 | 0.4476 | 0.4290 | 0.2911 | 0.4065 | 0.2164 |
| nnU-Net + CBAM, Late (`nnunetcbam_multihead`) | 0.4387 | 0.4282 | 0.4476 | 0.4516 | 0.4234 | 0.2726 | 0.3992 | 0.1928 |
| SegFormer, single-task (`segformer_single`) | 0.4726 | 0.4540 | 0.4694 | 0.4056 | 0.4677 | 0.1774 | 0.4298 | 0.2138 |
| SegFormer, Early (`segformer_early`) | 0.4758 | 0.4718 | 0.4839 | 0.4089 | 0.4790 | 0.2387 | 0.4492 | 0.2200 |
| SegFormer, Mid (`segformer_mid`) | 0.4669 | 0.4573 | 0.4524 | 0.4210 | 0.4597 | 0.1879 | 0.4153 | 0.2089 |
| SegFormer, Late (`segformer_late`) | 0.4565 | 0.4476 | 0.4476 | 0.4315 | 0.4508 | 0.2306 | 0.4371 | 0.2270 |

Source: `tables/filtering_effects.csv`. Region specificity is one minus the false regions left after filtering over the false regions before.
