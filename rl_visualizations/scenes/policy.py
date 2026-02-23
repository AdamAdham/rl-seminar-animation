from manim import *


class PolicyScene(Scene):
    def construct(self):
        # Title / description
        title = Text("Policy in RL", font_size=60).to_edge(UP)
        description = Text(
            "A policy is a probability distribution over available actions, so it \n"
            "just assigns a probability to each action given the current state.",
            t2c={"assigns": BLUE, "probability": BLUE, "each action": BLUE},
            font_size=28,
        ).next_to(title, DOWN, buff=0.5)

        self.play(FadeIn(title))
        self.play(Write(description))
        self.wait(1)

        # Policy equation

        policy_eq = (
            MathTex(r"\pi(a \mid s) = \text{p}(a \mid s)")
            .scale(1.0)
            .next_to(description, DOWN, buff=0.5)
        )
        self.play(Write(policy_eq))

        # Multi-armed bandit illustration
        self.wait(3)

        arm_colors = [BLUE, GREEN, YELLOW, RED]
        arm_labels = ["A1", "A2", "A3", "A4"]
        probabilities = [0.1, 0.3, 0.4, 0.2]

        # Create rectangles as colored arms
        arms = VGroup()
        sticks = VGroup()  # for lever sticks
        knobs = VGroup()  # for circles at the top

        for color in arm_colors:
            # Main arm rectangle
            rect = Rectangle(
                width=0.5,
                height=2.0,
                fill_color=color,
                fill_opacity=0.7,
                stroke_color=WHITE,
            )
            arms.add(rect)

            # Lever stick (rotated thin rectangle)
            stick = Rectangle(
                width=0.2,
                height=0.8,
                fill_color=WHITE,
                fill_opacity=1.0,
                stroke_color=BLACK,
                stroke_width=2,
            )
            sticks.add(stick)

            # Circle knob at the end of the stick
            knob = (
                Circle(
                    radius=0.17,
                    fill_color=BLACK,
                    fill_opacity=1.0,
                    stroke_color=WHITE,
                    stroke_width=2.5,
                )
                .next_to(stick.get_top(), UP, buff=0)
                .shift(RIGHT * 0.6)
            )
            knobs.add(knob)

        # Arrange arms horizontally
        arms.arrange(RIGHT, buff=1.0).next_to(policy_eq, DOWN, buff=0.85)

        # Position lever sticks on top of arms
        for arm, stick, knob in zip(arms, sticks, knobs):
            stick.move_to(arm.get_top())
            knob.move_to(stick.get_top())  # circle at end of stick

        # Action labels under each arm
        labels = VGroup(
            *[
                Text(label, font_size=24, color=color).next_to(arm, DOWN, buff=0.2)
                for arm, label, color in zip(arms, arm_labels, arm_colors)
            ]
        )

        # Probability labels under each action
        prob_labels = VGroup(
            *[
                MathTex(p).set_color(c).scale(0.8).next_to(arm, DOWN, buff=0.8)
                for arm, p, c in zip(arms, probabilities, arm_colors)
            ]
        )

        # Animate all elements
        self.play(
            FadeIn(arms, shift=UP),
            FadeIn(sticks, shift=UP),
            FadeIn(knobs, shift=UP),
        )
        self.play(
            *[Write(p) for p in prob_labels],
            Write(labels),
        )

        # Shift multi arm example to the left
        self.wait(4)

        multi_arm_group = VGroup(
            arms,
            sticks,
            knobs,
            *[p for p in prob_labels],
            labels,
        )

        self.play(multi_arm_group.animate.shift(LEFT * 3.2 + DOWN * 0.2))

        # Graph

        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 1, 0.1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE},
        )

        axes_labels = axes.get_axis_labels(
            x_label=Text("Arm", font_size=24),
            y_label=MathTex(r"\pi(a \mid s)").scale(0.8),
        )

        # X-axis ticks and labels
        x_ticks = VGroup()
        for i, label in enumerate(arm_labels):
            tick = Text(label, font_size=24).next_to(
                axes.c2p(i + 0.5, 0), DOWN, buff=0.1
            )
            x_ticks.add(tick)

        # Y-axis probabilities as dots
        prob_dots = VGroup()
        for i, (p, color) in enumerate(zip(probabilities, arm_colors)):
            dot = Dot(axes.c2p(i + 0.5, p), radius=0.1, color=color)
            prob_dots.add(dot)

        # Lines
        prob_lines = VGroup()
        for i, dot in enumerate(prob_dots):
            line = Line(
                axes.c2p(i + 0.5, 0),
                dot.get_center(),
                color=arm_colors[i],
                stroke_width=6,
            )
            prob_lines.add(line)

        # Probability labels
        prob_texts = VGroup()
        for i, (p, dot) in enumerate(zip(probabilities, prob_dots)):
            text = MathTex(f"{p}").scale(0.7).next_to(dot, UP, buff=0.1)
            text.set_color(arm_colors[i])
            prob_texts.add(text)

        # Group graph to adjust postion
        graph_group = VGroup(
            axes,
            axes_labels,
            x_ticks,
            prob_lines,
            prob_dots,
            prob_texts,
        )

        # Move entire graph wherever you want
        graph_group.next_to(multi_arm_group, RIGHT, buff=1.4)
        graph_group.scale(0.8)

        # Animations
        self.play(Create(axes), Write(axes_labels))
        self.play(*[Write(t) for t in x_ticks])
        self.play(*[Create(l) for l in prob_lines], *[FadeIn(d) for d in prob_dots])
        self.play(*[Write(t) for t in prob_texts])
