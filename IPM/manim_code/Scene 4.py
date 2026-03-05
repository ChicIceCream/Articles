from manim import *

class Scene4_NuScenesTransformation(Scene):
    def construct(self):
        # 1. Load the Images (Centered inward instead of pinned to the edges!)
        img_left = ImageMobject("trial_img.jpg").scale(0.35).move_to(LEFT * 4)
        img_right = ImageMobject("bev_img.jpg").scale(0.35).move_to(RIGHT * 4)

        title_left = Text("Perspective (Camera)", font_size=20).next_to(img_left, UP)
        title_right = Text("Metric (Bird's-Eye)", font_size=20).next_to(img_right, UP)

        self.play(FadeIn(img_left), Write(title_left))
        self.play(FadeIn(img_right), Write(title_right))
        self.wait(0.5)

        # 2. Add the Basis Vectors to show the Coordinate Frame Shift
        
        # CAMERA FRAME (Top Left, OUTSIDE the image)
        # HOW TO TWEAK: Change the np.array([-0.5, 0.5, 0]). 
        # Negative X moves it further left. Positive Y moves it further up.
        cam_origin = img_left.get_corner(UL) + np.array([-0.5, 0.5, 0])
        cam_x = Arrow(cam_origin, cam_origin + RIGHT*0.8, color=RED, buff=0, max_tip_length_to_length_ratio=0.15)
        cam_y = Arrow(cam_origin, cam_origin + DOWN*0.8, color=RED, buff=0, max_tip_length_to_length_ratio=0.15)
        cam_label = MathTex(r"\hat{i}_{cam}", color=RED, font_size=24).next_to(cam_x, UP, buff=0.1)
        
        # EGO FRAME (Bottom Right, OUTSIDE the image)
        # HOW TO TWEAK: Change the np.array([0.5, -0.5, 0]).
        # Positive X moves it further right. Negative Y moves it further down.
        ego_origin = img_right.get_corner(DR) + np.array([0.5, -0.5, 0])
        ego_x = Arrow(ego_origin, ego_origin + UP*1.2, color=BLUE, buff=0, max_tip_length_to_length_ratio=0.1)
        ego_y = Arrow(ego_origin, ego_origin + LEFT*0.8, color=BLUE, buff=0, max_tip_length_to_length_ratio=0.15)
        ego_label = MathTex(r"\hat{i}_{ego}", color=BLUE, font_size=24).next_to(ego_x, RIGHT, buff=0.1)

        self.play(Create(cam_x), Create(cam_y), Write(cam_label))
        self.play(Create(ego_x), Create(ego_y), Write(ego_label))
        self.wait(0.5)

        # 3. Create the Floating NuScenes Matrix in the center
        h_matrix = Matrix([
            ["h_{11}", "h_{12}", "h_{13}"],
            ["h_{21}", "h_{22}", "h_{23}"],
            ["h_{31}", "h_{32}", "h_{33}"]
        ]).scale(0.5).move_to(ORIGIN)
        
        matrix_box = SurroundingRectangle(h_matrix, color=YELLOW, buff=0.2)
        h_label = MathTex("H_{nuScenes}", color=YELLOW).next_to(matrix_box, UP)

        self.play(Write(h_matrix), Create(matrix_box), Write(h_label))
        self.wait(0.5)

        # 4. Target a specific pixel on the truck
        red_dot = Dot(color=RED, radius=0.08).move_to(img_left.get_center() + DOWN*0.8 + LEFT*0.4)
        red_label = MathTex(r"(u, v)", color=RED, font_size=24).next_to(red_dot, DOWN)
        
        reticle = Circle(radius=0.2, color=RED).move_to(red_dot)

        self.play(Create(reticle))
        self.play(reticle.animate.scale(0.1).set_opacity(0), FadeIn(red_dot), Write(red_label))
        self.wait(0.5)

        # 5. The Transformation Ray (Pixel -> Matrix)
        ray_in = Line(start=red_dot.get_center(), end=matrix_box.get_left(), color=RED)
        moving_pixel = Square(side_length=0.1, color=RED, fill_opacity=1).move_to(red_dot)
        
        self.play(Create(ray_in))
        self.play(MoveAlongPath(moving_pixel, ray_in), run_time=1)
        
        self.play(Indicate(matrix_box, color=GREEN, scale_factor=1.2), FadeOut(moving_pixel))
        self.wait(0.5)

        # 6. The Landing Ray (Matrix -> Ground)
        green_dot = Dot(color=GREEN, radius=0.08).move_to(img_right.get_center() + DOWN*0.6 + LEFT*0.1)
        green_label = MathTex(r"(X, Y)", color=GREEN, font_size=24).next_to(green_dot, DOWN)

        ray_out = Line(start=matrix_box.get_right(), end=green_dot.get_center(), color=GREEN)
        moving_metric = Circle(radius=0.06, color=GREEN, fill_opacity=1).move_to(matrix_box.get_right())

        self.play(Create(ray_out))
        self.play(MoveAlongPath(moving_metric, ray_out), run_time=1)
        self.play(Transform(moving_metric, green_dot), Write(green_label))
        
        # Final flourish
        self.play(Flash(green_dot, color=GREEN, line_length=0.2))
        self.wait(3)