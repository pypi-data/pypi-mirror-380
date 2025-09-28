from ..colors import Color, Gradient
from ..layers.base import Layer
from ..math.lerp import inv_lerp


class SpectrumLayer(Layer):
    def __init__(
        self, width: int, height: int, duration: int, gradient: Gradient
    ) -> None:
        super().__init__(width, height, duration)

        self.gradient = gradient

    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        gradient_index = inv_lerp(0, self.duration - 1, frame)

        return self.gradient.color_at(gradient_index)
