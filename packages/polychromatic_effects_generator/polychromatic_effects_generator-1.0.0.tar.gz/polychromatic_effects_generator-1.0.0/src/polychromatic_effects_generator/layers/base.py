from abc import ABC, abstractmethod

from ..colors import Color


class Layer(ABC):
    def __init__(self, width: int, height: int, duration: int) -> None:
        self.width = width
        self.height = height
        self.duration = duration

    @abstractmethod
    def render_pixel_at(self, x: int, y: int, frame: int) -> Color:
        raise NotImplementedError
