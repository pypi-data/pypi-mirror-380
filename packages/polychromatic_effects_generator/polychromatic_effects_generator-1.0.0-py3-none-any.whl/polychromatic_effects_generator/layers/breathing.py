import math

from ..colors import Color, Gradient
from ..layers.base import Layer


class BreathingLayer(Layer):
    def __init__(
        self, width: int, height: int, duration: int, colors: list[Color]
    ) -> None:
        super().__init__(width, height, duration)

        self.colors = colors

    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        color_index = math.floor(frame / self.duration * len(self.colors))
        color = self.colors[color_index]

        period = self.duration / len(self.colors)

        # Calculate alpha using a sine wave that pulses between 0 and 1
        color.alpha = (
            0.5 * math.cos((2 * math.pi / period) * (frame - period / 2)) + 0.5
        )

        return color.over(Color(0, 0, 0))
