from .colors import Color
from .layers.base import Layer
from .layers.static import StaticLayer


class Effect:
    def __init__(self, width: int, height: int, duration: int, fps: int) -> None:
        self.width = width
        self.height = height

        self.duration = duration
        self.fps = fps

        background = StaticLayer(self.width, self.height, self.duration, Color(0, 0, 0))

        self.grid: list[list[list[Layer]]] = [
            [[background] for _ in range(self.height)] for _ in range(self.width)
        ]

    def add_layer_to_pixel(self, x: int, y: int, layer: Layer):
        self.grid[x][y].append(layer)

    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        result = Color(0, 0, 0, 0)

        for layer in reversed(self.grid[x][y]):
            color = layer.render_pixel_at(x, y, frame)

            result = result.over(color)

            if result.alpha == 1.0:
                break

        return result
