from manim import *


class ExpectationScene(Scene):
    def construct(self):
        title = Text("Expectation", font_size=72).to_edge(UP)
        self.add(title)

        # Description text
        description = Text(
            "Expectation is the weighted average of a random variable's value over \n"
            "its probability.",
            font_size=30,
            t2c={"Expectation": GREEN, "value": RED, "probability": BLUE},
        ).next_to(title, DOWN, buff=1)

        self.play(Write(description), run_time=4)

        # Math equation
        equation = MathTex(
            r"E[X] = \sum_{x} x ~ p(x)",
            substrings_to_isolate=["E[X]", "x", "p(x)"],  # ✅ list of substrings
        ).next_to(description, DOWN, buff=1.5)
        # .next_to(description, DOWN, buff=0.5)

        # Set colors AFTER creation
        equation.set_color_by_tex("E[X]", GREEN)
        equation.set_color_by_tex("x", RED)
        equation.set_color_by_tex("p(x)", BLUE)

        self.play(Create(equation))
