from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def clockwise_angle_between(self, other: Vector) -> float:
        det = self.x * other.y - self.y * other.x
        dot = self.x * other.x + self.y * other.y

        return math.atan2(-det, -dot) + math.pi

    def rotated_clockwise(self, angle: float) -> Vector:
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)

        return Vector(x, y)
