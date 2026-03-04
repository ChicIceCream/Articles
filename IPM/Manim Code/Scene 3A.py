from manim import *

class Scene3A_ProjectMath(Scene):
    def construct(self):
        # Start with the 3D homogeneous vector
        prime_vector = Matrix([["x'"], ["y'"], ["w'"]])
        self.play(Write(prime_vector))
        self.wait(1)

        # Pull out 1/w'
        pull_out = MathTex(r"\frac{1}{w'}").next_to(prime_vector, LEFT)
        xy_vector = Matrix([["x'"], ["y'"], ["w'"]]) # Keeping it temporarily to show transition
        
        group1 = VGroup(pull_out, xy_vector).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
        self.play(Transform(prime_vector, group1))
        self.wait(1)

        # Push the division inside
        divided_matrix = Matrix([
            [r"\frac{x'}{w'}"],
            [r"\frac{y'}{w'}"],
            [r"\frac{w'}{w'}"]
        ]).move_to(ORIGIN)

        self.play(Transform(prime_vector, divided_matrix))
        self.wait(1)

        # Simplify down to 2D Ground Coordinates
        ground_matrix = Matrix([
            ["X"],
            ["Y"]
        ]).move_to(ORIGIN)

        ground_label = Text("Ground Coordinates!", color=GREEN, font_size=30).next_to(ground_matrix, DOWN)

        self.play(Transform(prime_vector, ground_matrix), Write(ground_label))
        self.wait(2)