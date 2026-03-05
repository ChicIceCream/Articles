from manim import *

class Scene1_TheLift(Scene):
    def construct(self):
        # Define the 3x3 Homography Matrix
        H_matrix = Matrix([
            ["h_{11}", "h_{12}", "h_{13}"],
            ["h_{21}", "h_{22}", "h_{23}"],
            ["h_{31}", "h_{32}", "h_{33}"]
        ])
        
        # Define the initial 2x1 Pixel Vector
        uv_vector = Matrix([
            ["u"],
            ["v"]
        ])

        # Group them with a multiplication sign
        equation = VGroup(H_matrix, MathTex(r"\times"), uv_vector).arrange(RIGHT, buff=0.5)
        
        self.play(Write(equation))
        self.wait(1)

        # Show dimensions underneath
        dim_H = Text("3x3", font_size=24).next_to(H_matrix, DOWN)
        dim_uv = Text("2x1", font_size=24).next_to(uv_vector, DOWN)
        
        self.play(FadeIn(dim_H), FadeIn(dim_uv))
        self.wait(1)

        # Highlight mismatch
        mismatch_text = Text("Dimension Mismatch!", color=RED, font_size=30).next_to(equation, UP)
        self.play(Write(mismatch_text), Indicate(dim_uv, color=RED))
        self.wait(1)

        # The Lift: Add the 1 to make it 3x1
        uv1_vector = Matrix([
            ["u"],
            ["v"],
            ["1"]
        ]).move_to(uv_vector.get_center())

        dim_uv1 = Text("3x1", font_size=24, color=GREEN).next_to(uv1_vector, DOWN)
        match_text = Text("Ready to Multiply!", color=GREEN, font_size=30).move_to(mismatch_text.get_center())

        self.play(
            Transform(uv_vector, uv1_vector),
            Transform(dim_uv, dim_uv1),
            Transform(mismatch_text, match_text)
        )
        self.wait(2)