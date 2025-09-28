from enum import Enum, auto

from ..colors import Color, Gradient
from ..math.lerp import inv_lerp
from .base import Layer


class WaveLayer(Layer):
    class Direction(Enum):
        LEFT = auto()
        RIGHT = auto()

    def __init__(
        self,
        width: int,
        height: int,
        duration: int,
        gradient: Gradient,
        direction: Direction = Direction.RIGHT,
    ) -> None:
        super().__init__(width, height, duration)

        self.gradient = gradient
        self.direction = direction

    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        index = inv_lerp(0, self.width - 1, x)
        index_shift = inv_lerp(0, self.duration - 1, frame)

        if self.direction == self.Direction.LEFT:
            result_index = index - index_shift
            if result_index < 0:
                result_index += 1
        elif self.direction == self.Direction.RIGHT:
            result_index = index + index_shift
            if result_index > 1:
                result_index -= 1
        else:
            raise RuntimeError(
                f"self.direction is neither Direction.LEFT or Direction.RIGHT"
            )

        return self.gradient.color_at(result_index)
