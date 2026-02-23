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
            expected_reward_function[-2].animate.set_color(GREEN),
            # No dynamics
            expected_reward_function_no_dynamics[-1].animate.set_color(RED),
            expected_reward_function_no_dynamics[-2].animate.set_color(GREEN),
            expected_reward_function_no_dynamics[-3].animate.set_color(GREEN),
            expected_reward_function_no_dynamics[-4].animate.set_color(GREEN),
        )

        # Use marginalization
        self.wait(2)
        self.play(
            expected_reward_function.animate.shift(UP * 0.9).scale(0.8),
            expected_reward_function_no_dynamics.animate.shift(UP * 1.8).scale(0.8),
        )

        combined_marginalization = (
            MathTex(
                r"\text{Using marginalization:} ~ p(x)",
                r"=",
                r"\sum_{y} p(x, y)",
                r", \text{where }",
                r"x",
                r"=",
                r"(r \mid s,a)",
                r"\text{ and }",
                r"y",
                r"=",
                r"s' ",
            )
            .scale(0.8)
            .next_to(expected_reward_function_no_dynamics, DOWN, buff=0.5)
        )

        # Apply colors by index and character slices
        combined_marginalization[0][-2].set_color(GOLD_D)
        combined_marginalization[2][-4].set_color(GOLD_D)
        combined_marginalization[4].set_color(GOLD_D)
        combined_marginalization[6].set_color(GOLD_D)

        combined_marginalization[2][-2].set_color(TEAL)
        combined_marginalization[2][-7].set_color(TEAL)
        combined_marginalization[-3].set_color(TEAL)
        combined_marginalization[-1].set_color(TEAL)

        self.play(Create(combined_marginalization))

        marginal_r = MathTex(
            r"p(",
            r"r",
            r" \mid s, a",
            r")",
            r"=",
            r"\sum_{",
            r"s'",
            r"}",
            r" p(",
            r"s'",
            r",",
            r"r \mid s, a",
            r")",
        ).next_to(combined_marginalization, DOWN, buff=0.4)

        # Coloring by index
        marginal_r[1].set_color(GOLD_D)  # first r
        marginal_r[2].set_color(GOLD_D)  # r | s,a
        marginal_r[6].set_color(TEAL)  # s' in summation
        marginal_r[7].set_color(TEAL)  # s' inside joint
        marginal_r[9].set_color(TEAL)  # r inside joint
        marginal_r[11].set_color(GOLD_D)  # r inside joint

        self.play(Create(marginal_r))

        # Make the equation of no dynamics transform into the the one with
        self.wait(3)
        # Create a copy in its future state
        expected_target = expected_reward_function.copy()
        expected_target.scale(1.26).shift(DOWN * 0.7)

        # Animate both at once
        self.play(
            Transform(expected_reward_function, expected_target),
            Transform(expected_reward_function_no_dynamics, expected_target),
        )
