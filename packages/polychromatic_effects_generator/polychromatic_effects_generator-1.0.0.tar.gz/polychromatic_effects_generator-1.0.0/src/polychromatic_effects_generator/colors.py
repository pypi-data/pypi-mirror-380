from __future__ import annotations

from .math.lerp import inv_lerp, lerp


class Color:
    def __init__(self, red: int, green: int, blue: int, alpha: float = 1.0) -> None:
        u8_range = range(0, 256)

        if not red in u8_range or not green in u8_range or not blue in u8_range:
            raise ValueError("red, green, blue parameters must be in range 0-255")

        if alpha < 0.0 or alpha > 1.0:
            raise ValueError("alpha must be in range 0.0-1.0")

        self.red = red
        self.green = green
        self.blue = blue

        self.alpha = alpha

    def __repr__(self) -> str:
        return f"Color({self.red}, {self.green}, {self.blue}, {self.alpha})"

    def as_html(self) -> str:
        return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"

    def over(self, b: Color) -> Color:
        alpha_a = self.alpha
        alpha_b = b.alpha

        result_alpha = alpha_a + alpha_b * (1 - alpha_a)

        def c_o(c_a: int, c_b: int) -> float:
            return (c_a * alpha_a + c_b * alpha_b * (1 - alpha_a)) / result_alpha

        result_red = round(c_o(self.red, b.red))
        result_green = round(c_o(self.green, b.green))
        result_blue = round(c_o(self.blue, b.blue))

        return Color(result_red, result_green, result_blue, result_alpha)


class Gradient:
    def __init__(self, colors: dict[float, Color]) -> None:
        # Check that all indexes are in range 0.0-1.0
        for index in colors.keys():
            if index < 0 or index > 1:
                raise ValueError("all indexes must be in range 0.0-1.0")

        # Check that colors has a color at index 0 ana a color at index 1
        if 0 not in colors or 1 not in colors:
            raise ValueError(
                "colors must contain a color at index 0 and a color at index 1"
            )

        self.colors = colors

    def color_at(self, val: float) -> Color:
        if val in self.colors:
            return self.colors[val]

        # Find color before val and color after val
        color_a_index: float | None = None
        color_b_index: float | None = None

        previous_index: float = 0.0
        for index in sorted(self.colors.keys()):
            if index > val:
                color_a_index = previous_index
                color_b_index = index

                break

            previous_index = index

        if color_a_index is None or color_b_index is None:
            raise RuntimeError(
                "could not find color before val or color after val; "
                "possibly due to an invalid colors dict"
            )

        color_a = self.colors[color_a_index]
        color_b = self.colors[color_b_index]

        # Lerp colors
        t = inv_lerp(color_a_index, color_b_index, val)

        red = round(lerp(color_a.red, color_b.red, t))
        green = round(lerp(color_a.green, color_b.green, t))
        blue = round(lerp(color_a.blue, color_b.blue, t))

        alpha = lerp(color_a.alpha, color_b.alpha, t)

        return Color(red, green, blue, alpha)
