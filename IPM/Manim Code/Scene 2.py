from manim import *

class Scene2_TheTransform(Scene):
    def construct(self):
        # Starting setup
        H_matrix = Matrix([
            ["h_{11}", "h_{12}", "h_{13}"],
            ["h_{21}", "h_{22}", "h_{23}"],
            ["h_{31}", "h_{32}", "h_{33}"]
        ])
        uv1_vector = Matrix([["u"], ["v"], ["1"]])
        
        lhs = VGroup(H_matrix, uv1_vector).arrange(RIGHT, buff=0.2)
        equals = MathTex("=").next_to(lhs, RIGHT, buff=0.5)
        
        self.play(Write(lhs), Write(equals))
        self.wait(1)

        # The Expanded Multiplication
        expanded_matrix = Matrix([
            ["h_{11}u + h_{12}v + h_{13}(1)"],
            ["h_{21}u + h_{22}v + h_{23}(1)"],
            ["h_{31}u + h_{32}v + h_{33}(1)"]
        ]).next_to(equals, RIGHT, buff=0.5)

        self.play(Write(expanded_matrix))
        self.wait(2)

        # Collapse into new variables
        collapsed_matrix = Matrix([
            ["x'"],
            ["y'"],
            ["w'"]
        ]).next_to(equals, RIGHT, buff=0.5)

        self.play(Transform(expanded_matrix, collapsed_matrix))
        
        # Highlight w' as the scaling factor
        scaling_box = SurroundingRectangle(collapsed_matrix.get_entries()[2], color=YELLOW)
        scaling_text = Text("Scaling Factor", color=YELLOW, font_size=24).next_to(scaling_box, RIGHT)
        
        self.play(Create(scaling_box), Write(scaling_text))
        self.wait(2)