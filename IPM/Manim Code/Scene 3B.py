from manim import *

class Scene3B_Project3DVisual(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create Ground Plane
        ground = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3], v_range=[-3, 3],
            fill_color=BLUE, fill_opacity=0.3, checkerboard_colors=[BLUE_D, BLUE_E]
        )
        
        # Create Camera Center (Origin of rays)
        camera_center = Dot3D(point=np.array([0, 0, 4]), color=WHITE)
        camera_label = Text("Camera", font_size=24).next_to(camera_center, UP)
        self.add_fixed_orientation_mobjects(camera_label)

        # Create Image Plane
        image_plane = Surface(
            lambda u, v: np.array([u, v, 2]),
            u_range=[-1, 1], v_range=[-1, 1],
            fill_color=RED, fill_opacity=0.3
        )

        self.play(Create(ground), Create(image_plane), FadeIn(camera_center), FadeIn(camera_label))
        self.wait(1)

        # Points for the ray
        pixel_point = np.array([0.5, 0.5, 2])
        ground_point = np.array([1, 1, 0])

        # Draw Ray
        ray = Line3D(start=camera_center.get_center(), end=ground_point, color=YELLOW)
        self.play(Create(ray))
        
        # The Dot (representing our coordinate) moving
        moving_dot = Dot3D(point=pixel_point, color=YELLOW, radius=0.1)
        self.play(FadeIn(moving_dot))
        
        pixel_label = Text("(u, v)", font_size=20, color=RED).next_to(moving_dot, RIGHT)
        self.add_fixed_orientation_mobjects(pixel_label)
        self.play(FadeIn(pixel_label))
        self.wait(1)

        # Project down to ground
        self.play(
            moving_dot.animate.move_to(ground_point),
            FadeOut(pixel_label)
        )
        
        ground_label = Text("(X, Y)", font_size=24, color=GREEN).next_to(moving_dot, RIGHT)
        self.add_fixed_orientation_mobjects(ground_label)
        self.play(FadeIn(ground_label))
        
        # Rotate camera slightly to show off the 3D effect
        self.move_camera(theta=60 * DEGREES, run_time=3)
        self.wait(2)