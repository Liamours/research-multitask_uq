"""Resolve overlapping boxes into one class mask.

Each box gets an owner id. A pixel belongs to the box that contains it, then to the box with the highest support,
then to the nearest box centre, then to the lower box index. Every box then keeps one connected component, and an
empty box falls back to its own mask. The functions are copied from the original pipeline without change.
"""
from __future__ import annotations

from typing import Any

import cv2
import numpy as np

from .algorithm import BBox


def _resolve_owner_contract(
    owner_map: np.ndarray,
    bbox_specs: list[dict[str, Any]],
) -> dict[str, int]:
    fixed_empty = 0
    fixed_multi = 0
    for _pass_index in range(3):
        changed = False
        for spec in bbox_specs:
            bbox: BBox = spec["bbox"]
            owner_id = int(spec["owner_id"])
            fallback_roi = spec["fallback_roi"]
            roi = owner_map[bbox.ymin:bbox.ymax, bbox.xmin:bbox.xmax]
            binary = (roi == owner_id).astype("uint8")
            component_count, labels, stats, _ = cv2.connectedComponentsWithStats(binary, 8)
            component_count -= 1

            if component_count <= 0:
                if fallback_roi is not None and fallback_roi.shape == roi.shape and fallback_roi.max() > 0:
                    roi[fallback_roi > 0] = owner_id
                    fixed_empty += 1
                    changed = True
                continue

            if component_count > 1:
                keep_binary = _bbox_iou_single_component(binary)
                remove_binary = (binary > 0) & (keep_binary == 0)
                if np.any(remove_binary):
                    roi[remove_binary] = 0
                    fixed_multi += 1
                    changed = True
        if not changed:
            break

    return {
        "fixed_empty_bboxes": fixed_empty,
        "fixed_multi_patch_bboxes": fixed_multi,
    }


def _bbox_iou_single_component(binary: np.ndarray) -> np.ndarray:
    component_count, labels, stats, _ = cv2.connectedComponentsWithStats(binary.astype(np.uint8), 8)
    component_count -= 1
    if component_count <= 1:
        return (binary > 0).astype(np.uint8)

    bbox_mask = np.ones(binary.shape, dtype=np.uint8)
    best_label = 0
    best_iou = -1.0
    best_intersection = -1
    best_area = -1
    bbox_area = int(np.count_nonzero(bbox_mask))
    for label_id in range(1, int(component_count) + 1):
        component = labels == label_id
        area = int(stats[label_id, cv2.CC_STAT_AREA])
        intersection = int(np.count_nonzero(component))
        union = int(area + bbox_area - intersection)
        iou = float(intersection) / float(union) if union > 0 else 0.0
        if (
            iou > best_iou
            or (iou == best_iou and intersection > best_intersection)
            or (iou == best_iou and intersection == best_intersection and area > best_area)
        ):
            best_label = label_id
            best_iou = iou
            best_intersection = intersection
            best_area = area
    return (labels == best_label).astype(np.uint8)


def _build_owner_map(
    image_shape: tuple[int, int],
    bbox_specs: list[dict[str, Any]],
) -> np.ndarray:
    if not bbox_specs:
        return np.zeros(image_shape, dtype=np.uint16)

    owner_map = np.zeros(image_shape, dtype=np.uint16)
    best_inside = np.zeros(image_shape, dtype=np.uint8)
    best_support = np.full(image_shape, -1.0, dtype=np.float32)
    best_dist = np.full(image_shape, np.inf, dtype=np.float32)
    best_bbox_index = np.full(image_shape, np.iinfo(np.int32).max, dtype=np.int32)

    for spec in bbox_specs:
        bbox: BBox = spec["bbox"]
        owner_id = int(spec["owner_id"])
        bbox_index = int(spec["bbox_index"])
        candidate_binary = spec["full_binary"] > 0
        if not np.any(candidate_binary):
            continue

        cy = (bbox.ymin + bbox.ymax - 1) / 2.0
        cx = (bbox.xmin + bbox.xmax - 1) / 2.0
        ys, xs = np.where(candidate_binary)
        distances = (xs.astype(np.float32) - cx) ** 2 + (ys.astype(np.float32) - cy) ** 2
        support = 1.0 / (1.0 + np.sqrt(distances))
        inside = (
            (ys >= bbox.ymin)
            & (ys < bbox.ymax)
            & (xs >= bbox.xmin)
            & (xs < bbox.xmax)
        ).astype(np.uint8)

        cur_inside = best_inside[ys, xs]
        cur_support = best_support[ys, xs]
        cur_dist = best_dist[ys, xs]
        cur_bbox_index = best_bbox_index[ys, xs]

        replace = inside > cur_inside
        replace |= (
            (inside == cur_inside)
            & (support > cur_support)
        )
        replace |= (
            (inside == cur_inside)
            & np.isclose(support, cur_support)
            & (distances < cur_dist)
        )
        replace |= (
            (inside == cur_inside)
            & np.isclose(support, cur_support)
            & np.isclose(distances, cur_dist)
            & (bbox_index < cur_bbox_index)
        )

        if not np.any(replace):
            continue

        replace_y = ys[replace]
        replace_x = xs[replace]
        owner_map[replace_y, replace_x] = owner_id
        best_inside[replace_y, replace_x] = inside[replace]
        best_support[replace_y, replace_x] = support[replace]
        best_dist[replace_y, replace_x] = distances[replace]
        best_bbox_index[replace_y, replace_x] = bbox_index

    return owner_map


def _owner_to_class_mask(
    owner_map: np.ndarray,
    bbox_specs: list[dict[str, Any]],
) -> np.ndarray:
    final_mask = np.zeros(owner_map.shape, dtype=np.uint8)
    for spec in bbox_specs:
        owner_id = int(spec["owner_id"])
        label_value = int(spec["label_value"])
        final_mask[owner_map == owner_id] = label_value
    return final_mask


def _finalize_owner_map(
    owner_map: np.ndarray,
    bbox_specs: list[dict[str, Any]],
) -> tuple[np.ndarray, dict[str, int]]:
    final_owner_map = owner_map.copy()
    fixed_empty = 0
    fixed_multi = 0

    for spec in bbox_specs:
        bbox: BBox = spec["bbox"]
        owner_id = int(spec["owner_id"])
        fallback_roi = (spec["fallback_roi"] > 0).astype(np.uint8)
        owner_roi = final_owner_map[bbox.ymin:bbox.ymax, bbox.xmin:bbox.xmax]
        binary = (owner_roi == owner_id).astype(np.uint8)
        original_count, _, _, _ = cv2.connectedComponentsWithStats(binary, 8)
        original_count -= 1

        if original_count <= 0:
            binary = fallback_roi.copy()
            fixed_empty += 1
        elif original_count > 1:
            binary = _bbox_iou_single_component(binary)
            fixed_multi += 1

        if not np.any(binary):
            binary = fallback_roi.copy()
            fixed_empty += 1

        final_roi = final_owner_map[bbox.ymin:bbox.ymax, bbox.xmin:bbox.xmax]
        final_roi[final_roi == owner_id] = 0
        final_roi[binary > 0] = owner_id

    contract_stats = _resolve_owner_contract(final_owner_map, bbox_specs)
    return final_owner_map, {
        "fixed_empty_bboxes": fixed_empty + contract_stats["fixed_empty_bboxes"],
        "fixed_multi_patch_bboxes": fixed_multi + contract_stats["fixed_multi_patch_bboxes"],
    }
