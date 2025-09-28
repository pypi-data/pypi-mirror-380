from ..colors import Color
from .base import Layer


class StaticLayer(Layer):
    def __init__(self, width: int, height: int, duration: int, color: Color) -> None:
        super().__init__(width, height, duration)

        self.color = color

    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        return self.color
