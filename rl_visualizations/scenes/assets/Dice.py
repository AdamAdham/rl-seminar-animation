from manim import *


class Dice(VGroup):
    """
    A reusable 3D-looking dice object.
    Usage:
        dice = Dice(value=3)
        self.add(dice)
    """

    def __init__(
        self, value: int = 1, size: float = 2, pip_radius: float | None = None, **kwargs
    ):
        super().__init__(**kwargs)

        self.size = size
        if pip_radius is None:
            pip_radius = size / 10
        self.pip_radius = pip_radius

        if not (1 <= value <= 6):
            raise ValueError("Dice value must be between 1 and 6")

        self.square = RoundedRectangle(
            corner_radius=0.2,
            width=size,
            height=size,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=4,
        )

        self.pips = self._create_pips(value)
        self.add(self.square, self.pips)

    def _pip(self, x, y):
        return Dot(
            point=np.array([x, y, 0]),
            radius=self.pip_radius,
            color=RED,
        )

    def _create_pips(self, value):
        padding = self.size / 8
        s = (
            self.size / 2
        )  # If used directly, the pips center would be at the edge of the square
        s -= self.pip_radius  # Make edge of pip touch the edge of the square
        s -= padding  # Add some padding from the edge of the square

        layouts = {
            1: [(0, 0)],
            2: [(-s, s), (s, -s)],
            3: [(-s, s), (0, 0), (s, -s)],
            4: [(-s, s), (s, s), (-s, -s), (s, -s)],
            5: [(-s, s), (s, s), (0, 0), (-s, -s), (s, -s)],
            6: [(-s, s), (-s, 0), (-s, -s), (s, s), (s, 0), (s, -s)],
        }

        return VGroup(*[self._pip(x, y) for x, y in layouts[value]])

    def set_value(self, value):
        new_pips = self._create_pips(value)
        new_pips.move_to(self.square)
        self.pips.become(new_pips)
