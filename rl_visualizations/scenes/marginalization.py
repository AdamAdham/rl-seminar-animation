from manim import *


class MarginalizationScene(Scene):
    def construct(self):
        title = Text("Marginalization", font_size=72).to_edge(UP)
        self.add(title)

        # Joint distribution
        description = Text(
            "Given a known joint distribution of two discrete random variables, say, X and Y.",
            font_size=27,
            t2c={"joint distribution": GREEN},
        ).next_to(title, DOWN, buff=1)

        joint_prob_known_equation = MathTex(
            r"p(x, y)", r" = \; \text{known value}"
        ).next_to(description, DOWN, buff=0.3)
        joint_prob_known_equation[0].set_color(GREEN)

        self.play(Write(description), set_time=3)
        self.play(Create(joint_prob_known_equation), set_time=2)

        # Want we want "p(x)"
        self.wait(2)
        description_two = Text(
            "We want the probability of only x:",
            font_size=27,
            t2c={"agent chooses its \n next action.": BLUE},
        ).next_to(description, DOWN, aligned_edge=LEFT, buff=1.3)

        prob_x_equation = MathTex(r"p(x)").next_to(description_two, RIGHT, buff=0.3)
        prob_x_equation.set_color(BLUE)

        self.play(Write(description_two))
        self.play(Create(prob_x_equation))

        # Marginal Distribution
        self.wait(3)
        description_three = Text(
            "Marginalization is the process of summing out a variable (y) from a joint  \n"
            "distribution to get the marginal distribution of the remaining variables (x).",
            font_size=27,
            t2c={"summing": RED},
        ).next_to(description_two, DOWN, buff=0.4, aligned_edge=LEFT)

        marginalization_equation = MathTex(
            r"p(x)", r"=", r"\sum_{y}", r"p(x, y)"
        ).next_to(description_three, DOWN, buff=0.5)
        marginalization_equation[0].set_color(BLUE)
        marginalization_equation[2].set_color(RED)
        marginalization_equation[-1].set_color(GREEN)

        self.play(Write(description_three))
        self.play(Create(marginalization_equation))
