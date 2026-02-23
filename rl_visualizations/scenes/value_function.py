# Expected Return → Value Function → Bellman Expansion
# Manim CE scene

from manim import *


class ExpectedReturnScene(Scene):
    def construct(self):

        # --------------------------------------------------
        # 1. Motivation text
        # --------------------------------------------------
        title = Text("Expected Return", font_size=40).to_edge(UP)

        description = Text(
            "The agent wants to maximize its expected returns also called 'value function'.",
            font_size=24,
            t2c={"maximize": BLUE, "expected returns": BLUE, "'value function'": BLUE},
        ).next_to(title, DOWN, buff=0.5)

        self.add(title)
        self.play(Write(description))
        self.wait(1)

        value_expectation = MathTex(
            r"v_{\pi}(s) = \mathbb{E}_{\pi}\left[ G_t \mid S_t = s \right]"
        ).scale(1.0)

        value_expectation.next_to(description, DOWN, buff=0.5)

        self.play(Write(value_expectation))
        self.wait(0.5)

        # --------------------------------------------------
        # 3. Expand return definition
        # --------------------------------------------------
        value_return = MathTex(
            r"v_{\pi}(s) = \mathbb{E}_{\pi}\left[ R_{t+1} + \gamma G_{t+1} \mid S_t=s \right]"
        ).scale(1.0)

        value_return.next_to(value_expectation, DOWN, buff=0.5)

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
            r"\right]",  # 10
        ).next_to(value_return, DOWN, buff=0.5)

        self.play(Create(final_value_function))

        # --- RECTANGLE AROUND DISTRIBUTION ---
        self.wait(3)
        dist_box = SurroundingRectangle(
            final_value_function[2:5], color=BLUE, buff=0.15
        )

        self.play(Create(dist_box))

        # --- ARROWS FROM DISTRIBUTION TO r AND V(s') ---
        arrow_to_r = CurvedArrow(
            dist_box.get_top(),
            final_value_function[6].get_top() + UP * 0.1,
            angle=-0.6,
            color=RED,
        )

        arrow_to_v = CurvedArrow(
            dist_box.get_bottom(),
            final_value_function[9].get_bottom(),
            angle=0.6,
            color=GREEN,
        )

        self.play(
            Create(arrow_to_r),
        )

        self.wait(3)

        self.play(Create(arrow_to_v))

        # Shift whole final equation group
        self.wait(3)
        final_equation_group = VGroup(
            dist_box, arrow_to_r, arrow_to_v, final_value_function
        )
        self.play(final_equation_group.animate.shift(UP * 0.9).scale(0.8))

        # v_pi(s) =
        lhs_equation = MathTex(r"v_{\pi}(s)", r"=").next_to(
            final_value_function, DOWN, buff=0.6, aligned_edge=LEFT
        )

        # -------- LEFT TERM (RED) --------
        #  Σ π Σ Σ p(...) r
        left_term = (
            MathTex(
                r"\sum_{a}\pi(a\mid s)\sum_{r}\sum_{s'}p(r,s'\mid s,a)",
                r"\, r",
            )
            .next_to(lhs_equation, RIGHT, buff=0.1)
            .shift(DOWN * 0.25)
        )

        left_term.set_color(RED)

        # -------- PLUS SIGN (SEPARATE OBJECT) --------
        plus_sign = MathTex(r"+").next_to(left_term, RIGHT, buff=0.1).shift(UP * 0.1)

        # -------- RIGHT TERM (GREEN) --------
        #  Σ π Σ Σ p(...) γ Vπ(s')
        right_term = MathTex(
            r"\sum_{a}\pi(a\mid s)\sum_{r}\sum_{s'}p(r,s'\mid s,a)",
            r"\, \gamma V^{\pi}(s')",
        ).next_to(left_term, DOWN, buff=0.3)

        right_term.set_color(GREEN)

        # --------------------------------------------------
        # ANIMATION
        # --------------------------------------------------

        self.play(
            Write(lhs_equation),
            Write(left_term),
            Write(plus_sign),
            Write(right_term),
        )

        # self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in [left_term, title]])
