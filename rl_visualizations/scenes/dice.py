from manim import *
import random
from assets.Dice import Dice


class DiceExpectationExampleScene(Scene):
    def construct(self):
        print(
            "Size:",
            config.frame_width,
            "x",
            config.frame_height,
            "Pixels:",
            config.pixel_width,
            "x",
            config.pixel_height,
        )
        fair_dice_title = Text("Fair Dice Expectation", font_size=60).to_edge(UP)
        self.add(fair_dice_title)

        # Creation of dice ----------------------------

        # Set color order with each index being (lightest, darkest)
        colors = [
            (BLUE, BLUE_E),
            (TEAL, TEAL_E),
            (GREEN, GREEN_E),
            (YELLOW, YELLOW_E),
            (RED, RED_E),
            (PURPLE, PURPLE_E),
        ]

        size = 1.5
        dice_one = Dice(value=1, size=size, color=colors[0][1])
        dice_two = Dice(value=2, size=size, color=colors[1][1])
        dice_three = Dice(value=3, size=size, color=colors[2][1])
        dice_four = Dice(value=4, size=size, color=colors[3][1])
        dice_five = Dice(value=5, size=size, color=colors[4][1])
        dice_six = Dice(value=6, size=size, color=colors[5][1])

        dice_group = VGroup(
            dice_one,
            dice_two,
            dice_three,
            dice_four,
            dice_five,
            dice_six,
        )

        dice_group.arrange(RIGHT, buff=0.5)  # horizontal layout
        dice_group.move_to(ORIGIN)

        self.play(
            FadeIn(dice_group, shift=UP),
            run_time=2,
        )

        # Scaling down the dice
        self.play(dice_group.animate.scale(0.6).arrange(RIGHT, buff=1.4))

        # Create labels under each die --------------------------
        prob_scale = 0.7
        labels = VGroup(
            MathTex("p(1) = 1/6").scale(prob_scale),
            MathTex("p(2) = 1/6").scale(prob_scale),
            MathTex("p(3) = 1/6").scale(prob_scale),
            MathTex("p(4) = 1/6").scale(prob_scale),
            MathTex("p(5) = 1/6").scale(prob_scale),
            MathTex("p(6) = 1/6").scale(prob_scale),
        )

        # Position each label under corresponding die
        for die, label, color in zip(dice_group, labels, colors):
            label.next_to(die, DOWN, buff=0.3)
            label.set_color(color[0])

        self.play(
            FadeIn(labels, shift=DOWN),
        )

        # Creation of the expectation definition equation --------------------------
        expectation_definition_equation = MathTex(
            r"E[X] = \sum_{x} x ~ p(x)",
        ).next_to(labels, DOWN, buff=1)
        self.play(Create(expectation_definition_equation))

        self.wait(2)

        # Animate the shift of all elements to the top and scale down the expectation_definition_equation to get space
        up_dist = 1.3
        self.play(
            expectation_definition_equation.animate.scale(0.7)
            .shift(LEFT * 4.5)
            .shift(UP * 1.5),
            dice_group.animate.shift(UP * up_dist),
            labels.animate.shift(UP * up_dist),
        )

        # Write full expectation over fair dice roll

        fair_dice_expectation_before = (
            MathTex(
                r"=",
                r"1\cdot p(1)",
                r"+",
                r"2\cdot p(2)",
                r"+",
                r"3\cdot p(3)",
                r"+",
                r"4\cdot p(4)",
                r"+",
                r"5\cdot p(5)",
                r"+",
                r"6\cdot p(6)",
            )
            .scale(0.7)
            .next_to(expectation_definition_equation, RIGHT, buff=0.3)
            .shift(UP * 0.15)
        )

        fair_dice_expectation = (
            MathTex(
                r"=",
                r"1\cdot\frac{1}{6}",
                r"+",
                r"2\cdot\frac{1}{6}",
                r"+",
                r"3\cdot\frac{1}{6}",
                r"+",
                r"4\cdot\frac{1}{6}",
                r"+",
                r"5\cdot\frac{1}{6}",
                r"+",
                r"6\cdot\frac{1}{6}",
                r"=\frac{21}{6}=3.5",
            )
            .scale(0.7)
            .next_to(fair_dice_expectation_before, DOWN, buff=0.5, aligned_edge=LEFT)
        )

        # indices of the dice terms inside MathTex
        term_indices = [i for i in range(1, 12, 2)]

        for idx, (color, _) in zip(term_indices, colors):
            fair_dice_expectation_before[idx].set_color(color)
            fair_dice_expectation[idx].set_color(color)

        self.play(Create(fair_dice_expectation_before))

        self.wait(1)

        self.play(Create(fair_dice_expectation))

        self.wait(4)

        # Unfair Dice Example ------------------------------------
        # Each equation is will be in the exact same position for the best transition

        # Create modified title -------------------------------
        unfair_dice_title = Text(
            "Unfair Dice Expectation", font_size=60, t2c={"Un": BLUE}
        ).to_edge(UP)
        self.play(Transform(fair_dice_title, unfair_dice_title))

        # Create the modified labels ------------------------------
        self.wait(1)
        # New probabilities for each die
        new_probs = ["5/10", "3/10", "1/10", "1/10", "0.05", "0.1"]

        # Create new labels (same structure)
        new_labels = VGroup(
            *[
                MathTex(f"p({i+1}) = {prob}").scale(prob_scale)
                for i, prob in enumerate(new_probs)
            ]
        )

        # Position new labels under corresponding dice, same as before
        for die, label, color in zip(dice_group, new_labels, colors):
            label.next_to(die, DOWN, buff=0.3)
            label.set_color(color[0])

        # Animate the transition from old labels to new labels
        self.play(Transform(labels, new_labels))

        # Create last equation -------------------------------------
        self.wait(4)

        unfair_dice_expectation = MathTex(
            r"=",
            r"1\cdot\frac{5}{10}",
            r"+",
            r"2\cdot\frac{3}{10}",
            r"+",
            r"3\cdot\frac{1}{10}",
            r"+",
            r"4\cdot\frac{1}{10}",
            r"+",
            r"5\cdot\frac{1}{10}",
            r"+",
            r"6\cdot\frac{1}{10}",
            r"=2.5",
        ).scale(0.7)

        for idx, (color, _) in zip(term_indices, colors):
            unfair_dice_expectation[idx].set_color(color)

        unfair_dice_expectation.move_to(fair_dice_expectation)

        self.play(Transform(fair_dice_expectation, unfair_dice_expectation))
