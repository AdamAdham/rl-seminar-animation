from manim import *


class PolicyIterationExample(Scene):
    def construct(self):
        # Title
        title = Text("Policy Iteration", font_size=48).to_edge(UP)
        title_eval = Text("Policy Evaluation", font_size=48).move_to(title)
        title_improvement = Text("Policy Improvement", font_size=48).move_to(title)
        self.add(title)
        self.wait(1)

        # Create states as boxes
        s1 = Square(side_length=2)
        s2 = Square(side_length=2)
        s3 = Square(side_length=2)

        # Arrange horizontally
        states = VGroup(s1, s2, s3).arrange(RIGHT, buff=2)
        self.play(FadeIn(states))

        # Labels inside boxes
        label_s1 = Text("S1", font_size=24).move_to(s1.get_center())
        label_s2 = Text("S2", font_size=24).move_to(s2.get_center())
        label_s3 = Text("S3", font_size=24).move_to(s3.get_center())

        # v_pi(s1) = ?
        v_s1 = MathTex(r"v_{\pi}(s_1) = ?").scale(0.9).next_to(s1, DOWN, buff=0.4)

        # v_pi(s2) = ?
        v_s2 = MathTex(r"v_{\pi}(s_2) = ?").scale(0.9).next_to(s2, DOWN, buff=0.4)

        # v_pi(s3) = ?
        v_s3 = MathTex(r"v_{\pi}(s_3) = ?").scale(0.9).next_to(s3, DOWN, buff=0.4)

        # optional: group them for later control
        value_initializations = VGroup(v_s1, v_s2, v_s3)

        # --- ANIMATION ---
        self.play(
            FadeIn(label_s1),
            FadeIn(label_s2),
            FadeIn(label_s3),
            Write(v_s1),
            Write(v_s2),
            Write(v_s3),
        )

        self.wait(2)

        # Define actions: left, right, nothing
        # Only arrows for visual policy
        arrow_s2 = Arrow(start=s2.get_left(), end=s1.get_right())
        # S3 is terminal, no arrow

        # Highlight terminal state
        self.play(s3.animate.set_fill(GREEN, opacity=0.3))

        # Random initial policy: S1 -> nothing (no arrow), S2 -> left (arrow to S1)
        self.wait(2)
        # Loop arrow from S1 to itself
        loop_s1 = ArcBetweenPoints(start=s1.get_top(), end=s1.get_left(), angle=PI)
        loop_arrow_s1 = Arrow(
            max_stroke_width_to_length_ratio=0, end=loop_s1.get_end(), buff=0
        ).shift(LEFT * 0.2)

        self.play(FadeIn(arrow_s2), FadeIn(loop_s1), FadeIn(loop_arrow_s1))

        illustration_group = VGroup(
            states,
            label_s1,
            label_s2,
            label_s3,
            value_initializations,
            arrow_s2,
            loop_s1,
            loop_arrow_s1,
        )

        # Equation
        self.wait(2)
        value_function_expectation = MathTex(
            r"v_{\pi}(s)",
            r"=",
            r"\mathbb{E}_{\pi}",
            r"\left[",
            r"R\right]",
            r"+",
            r"\gamma v_{\pi}(s')",
            r"\qquad ",
            r"\text{**Simplified Version}",
        ).next_to(states, DOWN, buff=1)

        self.play(
            Write(value_function_expectation),
            illustration_group.animate.shift(UP * 0.5),
        )

        reward_description = (
            Tex(r"The only reward given is $+1$ when entering state $s_{3}$.")
            .scale(0.8)
            .next_to(value_function_expectation, DOWN, buff=0.5)
        )
        reward_description[-4:].set_color(GREEN)

        self.play(Write(reward_description))

        # Policy evaluation 1
        self.wait(2)
        self.play(FadeOut(title), FadeIn(title_eval))

        v_s1_1 = MathTex(r"v_{\pi}(s_1) = 0").scale(0.9).move_to(v_s1)
        self.play(Transform(v_s1, v_s1_1))

        self.wait(2)
        v_s2_1 = MathTex(r"v_{\pi}(s_2) = 0").scale(0.9).move_to(v_s2)
        self.play(Transform(v_s2, v_s2_1))

        self.wait(2)
        v_s3_1 = MathTex(r"v_{\pi}(s_3) = 0").scale(0.9).move_to(v_s3)
        self.play(Transform(v_s3, v_s3_1))

        # Policy Improvement 1
        self.wait(2)
        self.play(FadeOut(title_eval), FadeIn(title_improvement))

        # State 1
        self.play(FadeOut(arrow_s2))
        arrow_s1_s2 = Arrow(start=s1.get_right(), end=s2.get_left())
        self.play(FadeIn(arrow_s1_s2))

        self.wait(2)
        policy_value_s1_nothing_1 = (
            Tex("$0$").move_to(loop_s1.get_center()).shift(UP * 1)
        )
        policy_value_s1_right_1 = (
            Tex("$0$").move_to(arrow_s1_s2.get_center()).shift(UP * 0.4)
        )

        self.play(Write(policy_value_s1_nothing_1))
        self.wait(2)
        self.play(Write(policy_value_s1_right_1))

        # Policy choice
        self.wait(2)
        self.play(
            FadeOut(policy_value_s1_right_1),
            FadeOut(policy_value_s1_nothing_1),
            FadeOut(arrow_s1_s2),
        )

        # State 2
        self.wait(2)
        loop_s2 = ArcBetweenPoints(start=s2.get_top(), end=s2.get_left(), angle=PI)
        arrow_s2_s3 = Arrow(start=s2.get_right(), end=s3.get_left())

        self.play(
            FadeOut(loop_s1, loop_arrow_s1),
            FadeIn(arrow_s2),
            FadeIn(loop_s2),
            FadeIn(arrow_s2_s3),
        )

        policy_value_s2_left_1 = (
            Tex("$0$").move_to(arrow_s1_s2.get_center()).shift(UP * 0.4)
        )
        policy_value_s2_nothing_1 = (
            Tex("$0$").move_to(loop_s2.get_center()).shift(UP * 1)
        )
        policy_value_s2_right_1 = (
            Tex("$1$").move_to(arrow_s2_s3.get_center()).shift(UP * 0.4)
        )

        self.play(Write(policy_value_s2_left_1))
        self.wait(2)
        self.play(Write(policy_value_s2_nothing_1))
        self.wait(2)
        self.play(Write(policy_value_s2_right_1))
        self.wait(2)

        # Choice
        self.play(
            FadeOut(policy_value_s2_left_1),
            FadeOut(policy_value_s2_nothing_1),
            FadeOut(arrow_s2),
            FadeOut(loop_s2),
            FadeIn(loop_arrow_s1),
            FadeIn(loop_s1),
            FadeIn(policy_value_s1_nothing_1),
        )

        # Policy Evaluation 2
        self.wait(2)
        self.play(FadeOut(title_improvement), FadeIn(title_eval))

        v_s2_2 = MathTex(r"v_{\pi}(s_2) = 1").scale(0.9).move_to(v_s2)
        self.play(Transform(v_s2_1, v_s2_2), FadeOut(v_s2))

        # Policy Improvement 2
        self.wait(2)
        self.play(FadeOut(title_eval), FadeIn(title_improvement))

        self.play(
            FadeIn(arrow_s1_s2),
            FadeIn(loop_s1),
            FadeIn(loop_arrow_s1),
            FadeOut(arrow_s2_s3),
            FadeOut(policy_value_s2_right_1),
        )

        policy_value_s1_nothing_2 = (
            Tex("$0$").move_to(loop_s1.get_center()).shift(UP * 1)
        )
        policy_value_s1_right_2 = (
            Tex("$1$").move_to(arrow_s1_s2.get_center()).shift(UP * 0.4)
        )

        self.play(Write(policy_value_s1_nothing_2))
        self.wait(2)
        self.play(Write(policy_value_s1_right_2))

        # Choice
        self.play(
            FadeOut(policy_value_s1_nothing_2),
            FadeOut(policy_value_s1_nothing_1),
            FadeOut(loop_arrow_s1),
            FadeOut(loop_s1),
        )

        # Policy Evaluation 3
        self.wait(2)
        self.play(FadeOut(title_improvement), FadeIn(title_eval))

        self.play(FadeOut(policy_value_s1_right_2), FadeIn(arrow_s2_s3))

        self.wait(2)
        v_s1_2 = MathTex(r"v_{\pi}(s_1) = 1").scale(0.9).move_to(v_s1_1)
        self.play(Transform(v_s1_1, v_s1_2), FadeOut(v_s1))
