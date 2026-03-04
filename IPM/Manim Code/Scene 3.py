from manim import *

class Scene3A_ProjectMath(Scene):
    def construct(self):
        # 1. Start with the 3D homogeneous vector
        prime_vector = Matrix([["x'"], ["y'"], ["w'"]]).move_to(ORIGIN)
        self.play(Write(prime_vector))
        self.wait(1)

        # 2. Slide the vector and add the 1/w' scalar multiplier
        pull_out = MathTex(r"\frac{1}{w'}")
        
        # Group them temporarily to calculate the perfect center
        group1 = VGroup(pull_out, prime_vector.copy()).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
        
        # Animate the slide and write the fraction
        self.play(
            prime_vector.animate.move_to(group1[1].get_center()),
            Write(pull_out.move_to(group1[0].get_center()))
        )
        self.wait(1)

        # 3. Push the division inside using INLINE fractions
        # This completely removes the chaotic vertical stretching!
        divided_matrix = Matrix([
            ["x' / w'"],
            ["y' / w'"],
            ["w' / w'"]
        ]).move_to(ORIGIN)

        # Group and transform
        current_equation = VGroup(pull_out, prime_vector)
        self.play(ReplacementTransform(current_equation, divided_matrix))
        self.wait(1)

        # 4. Simplify down to our final 2D Ground Coordinates
        ground_matrix = Matrix([
            ["X"],
            ["Y"]
        ]).move_to(ORIGIN)

        ground_label = Text("Ground Coordinates!", color=GREEN, font_size=30).next_to(ground_matrix, DOWN, buff=0.5)

        self.play(
            ReplacementTransform(divided_matrix, ground_matrix), 
            Write(ground_label)
        )
        self.wait(2)