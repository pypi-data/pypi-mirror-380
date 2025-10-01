import math
from typing import List
import numpy as np
from stardust.components.annotations.point import Point
from stardust.components.annotations.point3d import Point3D
from stardust.components.annotations.box import Box2D
from stardust.components.annotations.box3d import Box3D


def euclidean_distance(p1: Point, p2: Point) -> float:
    """
    Compute Euclidean distance of p1 and p2

    Args:
        p1: Point

        p2: Point

    Returns
        float
    """
    assert isinstance(p1, Point) and isinstance(p1, Point)
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def euclidean_distance_3d(p1: Point3D, p2: Point3D) -> float:
    """
    Compute Euclidean distance of p1 and p2

    Args:
        p1: Point3D

        p2: Point3D

    Returns
        float
    """
    assert isinstance(p1, Point3D) and isinstance(p1, Point3D)
    x1, y1, z1 = p1.x, p1.y, p1.z
    x2, y2, z2 = p2.x, p2.y, p2.z
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def bounding_box(box1: Box2D, box2: Box2D) -> Box2D:
    """
    Compute bounding_box of box1 and box2

    Args:
        box1: Box2D

        box2: Box2D

    Returns
        Box2D
    """
    x11, y11, x12, y12 = box1.p1[0], box1.p1[1], box1.p2[0], box1.p2[1]
    x21, y21, x22, y22 = box2.p1[0], box2.p1[1], box2.p2[0], box2.p2[1]
    x1 = min(x11, x21)
    y1 = min(y11, y21)
    x2 = max(x12, x22)
    y2 = max(y12, y22)
    return Box2D(Point(x1, y1), Point(x2, y2))


def intersection_box(box1: Box2D, box2: Box2D) -> Box2D:
    """
    Compute intersection box of box1 and box2

    Args:
        box1: Box2D

        box2: Box2D

    Returns:
        Box2D
    """
    x11, y11, x12, y12 = box1.p1[0], box1.p1[1], box1.p2[0], box1.p2[1]
    x21, y21, x22, y22 = box2.p1[0], box2.p1[1], box2.p2[0], box2.p2[1]
    x1, y1 = max(x11, x21), max(y11, y21)
    x2, y2 = min(x12, x22), min(y12, y22)
    if x1 >= x2 or y1 >= y2:
        return Box2D(Point(0, 0), Point(0, 0))
    return Box2D(Point(x1, y1), Point(x2, y2))


def box_corners_bev(box: Box3D):
    """
    Get box corners of box in bev

    Args:
        box: Box3D

    Returns
        Box2D
    """
    x, y, l, w, r = box.center[0], box.center[1], box.size[0], box.size[1], box.rotation[2]
    BottomPlaneCenter = np.array([x, y])
    cos, sin = np.cos(r), np.sin(r)
    pc0 = np.array([x + cos * l / 2 + sin * w / 2,
                    y + sin * l / 2 - cos * w / 2])
    pc1 = 2 * BottomPlaneCenter - pc0
    return Box2D(p1=Point(pc1[0], pc1[1]), p2=Point(pc0[0], pc0[1]))
