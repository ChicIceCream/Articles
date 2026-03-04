from manim import *

class Scene2_TheTransform(Scene):
    def construct(self):
        # 1. Define all our math objects first
        H_matrix = Matrix([
            ["h_{11}", "h_{12}", "h_{13}"],
            ["h_{21}", "h_{22}", "h_{23}"],
            ["h_{31}", "h_{32}", "h_{33}"]
        ])
        uv1_vector = Matrix([["u"], ["v"], ["1"]])
        equals = MathTex("=")

        expanded_matrix = Matrix([
            ["h_{11}u + h_{12}v + h_{13}"],
            ["h_{21}u + h_{22}v + h_{23}"],
            ["h_{31}u + h_{32}v + h_{33}"]
        ])

        # 2. Arrange everything in a perfect horizontal line
        full_equation = VGroup(H_matrix, uv1_vector, equals, expanded_matrix).arrange(RIGHT, buff=0.2)
        full_equation.scale(0.85).move_to(ORIGIN)

        # 3. Animate the left side and the expanded matrix
        self.play(Write(H_matrix), Write(uv1_vector), Write(equals))
        self.wait(1)
        self.play(Write(expanded_matrix))
        self.wait(2)

        # 4. Create our clean collapsed matrix
        collapsed_matrix = Matrix([
            ["x'"],
            ["y'"],
            ["w'"]
        ]).scale(0.85)
        
        # Position it exactly where the big matrix currently is
        collapsed_matrix.move_to(expanded_matrix.get_center())

        # Use ReplacementTransform to smoothly swap them out
        self.play(ReplacementTransform(expanded_matrix, collapsed_matrix))
        
        # 5. TIGHTEN AND RE-CENTER
        # Group the remaining items and animate them sliding back together
        final_equation = VGroup(H_matrix, uv1_vector, equals, collapsed_matrix)
        self.play(final_equation.animate.arrange(RIGHT, buff=0.2).move_to(ORIGIN))
        self.wait(1)

        # 6. THE FIX: Highlight w' and properly place the text
        scaling_box = SurroundingRectangle(collapsed_matrix.get_entries()[2], color=YELLOW)
        scaling_text = Text("Scaling Factor", color=YELLOW, font_size=24)
        scaling_text.next_to(collapsed_matrix, RIGHT, buff=0.3).match_y(scaling_box)
        
        self.play(Create(scaling_box), Write(scaling_text))
        self.wait(2)