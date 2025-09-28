import math
from enum import Enum, auto

from ..colors import Color, Gradient
from ..layers.base import Layer
from ..math.lerp import remap
from ..math.vector import Vector


class WheelLayer(Layer):
    class Direction(Enum):
        CLOCKWISE = auto()
        COUNTERCLOCKWISE = auto()

    def __init__(
        self,
        width: int,
        height: int,
        duration: int,
        gradient: Gradient,
        direction: Direction,
        center: Vector,
    ) -> None:
        super().__init__(width, height, duration)

        self.gradient = gradient

        self.direction = direction

        self.center = center

    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        if self.direction == WheelLayer.Direction.CLOCKWISE:
            gradient_origin_rotation_angle = remap(
                0, self.duration - 1, 0, math.pi * 2, frame
            )
        elif self.direction == WheelLayer.Direction.COUNTERCLOCKWISE:
            gradient_origin_rotation_angle = remap(
                self.duration - 1, 0, math.pi * 2, 0, frame
            )
        else:
            raise RuntimeError(
                "self.direction is neither Direction.CLOCKWISE or Direction.COUNTERCLOCKWISE"
            )

        gradient_origin = Vector(0, -1).rotated_clockwise(
            gradient_origin_rotation_angle
        )

        key_vector = Vector(x, y) - self.center

        origin_key_angle = gradient_origin.clockwise_angle_between(key_vector)

        gradient_index = remap(0, math.pi * 2, 0, 1, origin_key_angle)

        return self.gradient.color_at(gradient_index)
