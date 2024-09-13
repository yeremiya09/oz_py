# mymath.py

import math

def triangle_area(base: float, height: float) -> float:
    """삼각형의 넓이를 계산합니다."""
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    """원의 넓이를 계산합니다."""
    return math.pi * radius * radius

def rectangular_prism_volume(length: float, width: float, height: float) -> float:
    """직육면체의 부피를 계산합니다."""
    return length * width * height
