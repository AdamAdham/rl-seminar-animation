from manim import *


class ExpectedReward(Scene):
    def construct(self):
        title = Text("Expected Reward", font_size=72).to_edge(UP)
        self.add(title)

        expected_reward_function = MathTex(
            r"r(s,a)",
            r"=",
            r"\mathbb{E}\!\left[ R_{t+1} \mid S_t=s,\; A_t=a \right]",
            r"=",
            r"\sum_{r} r ",
            r"\sum_{s'}\, p(s', r \mid s,a)",
        )

        self.add(expected_reward_function)

        # Highlight expectation as in progress (blue)
        self.wait(2)
        self.play(expected_reward_function[2].animate.set_color(BLUE))

        # Change color to done (green)
        self.wait(2)
        self.play(expected_reward_function[2].animate.set_color(GREEN))

        # Write the expected reward with no dynamics function
        self.wait(2)
        expected_reward_function_no_dynamics = MathTex(
            r"r(s,a)",
            r"=",
            r"\mathbb{E}\!\left[ R_{t+1} \mid S_t=s,\; A_t=a \right]",
            r"=",
            r"\sum_{r} r ~ ",
            r"p(r \mid s,a)",
        ).next_to(expected_reward_function, DOWN, buff=0.8)

        self.play(
            Create(expected_reward_function_no_dynamics),
            expected_reward_function.animate.shift(UP * 0.5),
        )

        # Highlight the difference with and without dynamics function
        self.wait(2)

        self.play(
            expected_reward_function[-1].animate.set_color(RED),
            expected_reward_function_no_dynamics[-1].animate.set_color(RED),
        )

        #
        self.wait(2)
