from manim import *


class Introduction(Scene):
    def construct(self):
        title = Text("What is Next?", font_size=72).to_edge(UP)
        self.add(title)

        description = Text(
            "We have defined how the environment works and the Markov property. \n"
            "The next important step is to understand how the agent chooses its \n next action. \n",
            font_size=30,
            t2c={"agent chooses its \n next action.": BLUE},
        ).next_to(title, DOWN, buff=1)

        description_two = Text(
            "This is done by maximizing the return function:",
            font_size=30,
            t2c={"maximizing": BLUE, "return": BLUE},
        ).next_to(description, DOWN, buff=0.6, aligned_edge=LEFT)

        return_function = MathTex(
            r"G_t = \sum_{k=0}^{\infty} \gamma^{k} R_{t+k+1}"
        ).next_to(description_two, RIGHT, buff=0.4)

        self.play(Write(description), run_time=4)

        self.wait(4)

        self.play(Write(description_two))

        self.play(Create(return_function))

        description_three = Text(
            "This is a complex task since it is the sum of all future rewards. \n"
            "So let's start with the expectation of only the next reward.",
            font_size=30,
            t2c={
                "complex": RED,
                "sum of all future rewards": RED,
                "start": BLUE,
                "expectation": BLUE,
                "next reward": BLUE,
            },
        ).next_to(description_two, DOWN, buff=1, aligned_edge=LEFT)

        self.play(Write(description_three))
