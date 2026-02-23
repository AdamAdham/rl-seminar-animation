# Expected Return → Value Function → Bellman Expansion
# Manim CE scene

from manim import *


class BellmanEquationScene(Scene):
    def construct(self):

        # --------------------------------------------------
        # 1. Motivation text
        # --------------------------------------------------
        title = Text("Bellman Equation", font_size=60).to_edge(UP)

        description = Text(
            "We have explained the logic behind this equation, but why this \n"
            "specific definition? This equation is defined recursively, such \n that many algorithms (eg: DP) can compute efficiently.",
            font_size=30,
            t2c={"recursively": BLUE_D},
        ).next_to(title, DOWN, buff=1)

        self.add(title)
        self.play(Write(description))
        self.wait(1)

        # assumes this is inside a Scene construct()

        # --- VALUE FUNCTION EQUATION ---
        final_value_function = MathTex(
            r"v_{\pi}(s)",  # 0
            r"=",  # 1
            r"\sum_{a} \pi(a \mid s)",  # 2
            r"\sum_{r}",  # 3
            r"\sum_{s'} p(r, s' \mid s, a)",  # 4  <-- distribution
            r"\left[",  # 5
            r"r",  # 6  <-- reward
            r"+",  # 7
            r"\gamma",  # 8
            r"v_{\pi}(s')",  # 9  <-- next value
            r"\right])",  # 10
        ).next_to(description, DOWN, buff=1)

        final_value_function[-2].set_color(BLUE_D)

        self.play(Create(final_value_function))
