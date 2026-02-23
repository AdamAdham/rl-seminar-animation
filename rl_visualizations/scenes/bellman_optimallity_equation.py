# Expected Return → Value Function → Bellman Expansion
# Manim CE scene

from manim import *


class BellmanOptimalityEquationScene(Scene):
    def construct(self):

        # --------------------------------------------------
        # 1. Motivation text
        # --------------------------------------------------
        title = Text("Bellman Optimality Equation", font_size=60).to_edge(UP)

        description = Text(
            "Same exact equation but while maximizing it using our policy",
            font_size=32,
            t2c={"maximizing": GREEN, "policy": BLUE_D},
        ).next_to(title, DOWN, buff=1.5)

        self.add(title)
        self.play(Write(description))
        self.wait(1)

        # assumes this is inside a Scene construct()

        # --- VALUE FUNCTION EQUATION ---
        final_value_function = (
            MathTex(
                r"v_{*}(s)",
                r"=",
                r"max_{\pi}",
                r"v_{\pi}(s)",
            )
            .next_to(description, DOWN, buff=1.2)
            .scale(1.2)
        )

        final_value_function[-2][0:3].set_color(GREEN)
        final_value_function[-2][3:].set_color(BLUE_D)
        final_value_function[-1][-4:-3].set_color(BLUE_D)

        self.play(Create(final_value_function))
