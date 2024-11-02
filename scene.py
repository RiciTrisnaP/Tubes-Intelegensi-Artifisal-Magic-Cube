from manim import *

class CubeWithNumbers(ThreeDScene):
    def construct(self):
        # Set up the camera orientation
        self.set_camera_orientation(phi=30 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES)
        
        # Parameters for the small cubes
        side_length = 0.6  # Side length of each smaller cube
        spacing = 1.0      # Spacing between cubes

        # Create the 3x3x3 grid of cubes with numbers
        cubes = VGroup()  # Group to hold all small cubes

        count = 1  # Start numbering from 1
        for x in range(-1, 4):
            for y in range(-1, 4):
                for z in range(-1, 4):
                    # Create a small cube
                    small_cube = Cube(side_length=side_length, fill_opacity=0.7)
                    small_cube.shift(x * spacing * RIGHT + y * spacing * UP + z * spacing * OUT)
                    
                    # Create a number for the small cube
                    number = Text(str(count), font_size=18, color=WHITE)
                    number.move_to(small_cube.get_center())  # Position the number at the center of the cube
                    
                    # Group the cube and its number together
                    small_cube_with_number = VGroup(small_cube, number)
                    cubes.add(small_cube_with_number)  # Add to the group of all cubes
                    
                    count += 1  # Increment the number for the next cube

        # Animate the entire group of cubes
        self.add(cubes)  # Add the group to the scene
        self.begin_ambient_camera_rotation(rate=0, about="phi")  # Rotate the camera around the cubes
        self.wait(8)
