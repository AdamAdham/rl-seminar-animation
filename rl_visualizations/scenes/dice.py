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

        self.add(Text("Dice Example", font_size=60).to_edge(UP))
        size = 1.5
        dice_one = Dice(value=1, size=size)
        dice_two = Dice(value=2, size=size)
        dice_three = Dice(value=3, size=size)
        dice_four = Dice(value=4, size=size)
        dice_five = Dice(value=5, size=size)
        dice_six = Dice(value=6, size=size)

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
        self.play(dice_group.animate.shift(UP * 1).scale(0.5).arrange(RIGHT, buff=1.5))

        # Create labels under each die
        labels = VGroup(
            MathTex("p(X = 1) = 1/6").scale(0.5),
            MathTex("p(X = 2) = 1/6").scale(0.5),
            MathTex("p(X = 3) = 1/6").scale(0.5),
            MathTex("p(X = 4) = 1/6").scale(0.5),
            MathTex("p(X = 5) = 1/6").scale(0.5),
            MathTex("p(X = 6) = 1/6").scale(0.5),
        )

        # Position each label under corresponding die
        for die, label in zip(dice_group, labels):
            label.next_to(die, DOWN, buff=0.3)

        self.play(
            FadeIn(labels, shift=DOWN),
        )

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

        # roll animation
        # for _ in range(8):
        #     value = random.randint(1, 6)
        #     self.play(
        #         Rotate(dice, angle=PI / 2),
        #         Transform(dice.pips, dice._create_pips(value)),
        #         run_time=0.25,
        #     )

        self.wait()
