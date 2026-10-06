"""Otsu thresholding with morphology and a guarded smooth-percentile fallback, applied inside one bounding box."""
from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np


@dataclass(frozen=True)
class BBox:
    xmin: int
    ymin: int
    xmax: int
    ymax: int
    label: str

    @property
    def width(self) -> int:
        return max(0, self.xmax - self.xmin)

    @property
    def height(self) -> int:
        return max(0, self.ymax - self.ymin)

    @property
    def area(self) -> int:
        return self.width * self.height

    @property
    def is_valid(self) -> bool:
        return self.width > 0 and self.height > 0 and self.area >= 4


def ellipse_kernel(size: int) -> np.ndarray:
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))


def peak_ellipse(roi: np.ndarray) -> np.ndarray:
    mask = np.zeros_like(roi, dtype=np.uint8)
    if roi.size == 0:
        return mask
    y_peak, x_peak = np.unravel_index(int(np.argmax(roi)), roi.shape)
    height, width = roi.shape
    cv2.ellipse(mask, (int(x_peak), int(y_peak)), (max(2, width // 5), max(2, height // 5)), 0, 0, 360, 255, -1)
    return mask


def coverage(mask: np.ndarray) -> float:
    return 0.0 if mask.size == 0 else float(np.count_nonzero(mask)) / float(mask.shape[0] * mask.shape[1])


def border_contact(mask: np.ndarray) -> float:
    if mask.size == 0:
        return 0.0
    binary = mask > 0
    return float(np.mean(np.concatenate([binary[0, :], binary[-1, :], binary[:, 0], binary[:, -1]])))


def clean_mask(mask: np.ndarray) -> np.ndarray:
    if mask.max() == 0:
        return mask
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
    if count > 1:
        mask = ((labels == 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))) * 255).astype(np.uint8)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        filled = np.zeros_like(mask)
        cv2.drawContours(filled, contours, -1, 255, cv2.FILLED)
        mask = filled
    if min(mask.shape[:2]) >= 6:
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, ellipse_kernel(3), iterations=1)
    return mask


def smooth_percentile_mask(roi: np.ndarray, percentile: float, sigma: float) -> np.ndarray:
    blurred = cv2.GaussianBlur(roi, (0, 0), sigmaX=sigma, sigmaY=sigma)
    mask = (blurred >= np.percentile(blurred, percentile)).astype(np.uint8) * 255
    return clean_mask(mask)


def box_mask(image: np.ndarray, box: BBox, params: dict) -> tuple[np.ndarray, str]:
    """Return the mask of one box (box-sized, values 0 or 255) and the path it took: otsu, percentile, or ellipse."""
    roi = image[box.ymin:box.ymax, box.xmin:box.xmax].copy()
    if roi.size == 0:
        return np.zeros((box.height, box.width), dtype=np.uint8), "empty"
    kernel = ellipse_kernel(int(params["kernel_size"]))
    _, mask = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=int(params["close_iterations"]))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=int(params["open_iterations"]))
    path = "otsu"
    if mask.max() == 0 or coverage(mask) > params["max_coverage"] or border_contact(mask) > params["max_border_contact"]:
        mask = smooth_percentile_mask(roi, params["percentile"], params["smoothing_sigma"])
        path = "percentile"
    if mask.max() == 0:
        mask, path = peak_ellipse(roi), "ellipse"
    return mask, path
