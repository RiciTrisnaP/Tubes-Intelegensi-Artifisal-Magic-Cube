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
        cube_dict = {}    # Dictionary to store cube positions for easy access
        
        count = 1  # Start numbering from 1
        for x in range(-1, 4):
            for y in range(-1, 4):
                for z in range(-1, 4):
                    # Create a small cube
                    small_cube = Cube(side_length=side_length, fill_opacity=0.7)
                    small_cube.shift(x * spacing * RIGHT + y * spacing * UP + z * spacing * OUT)
                    
                    # Create a number for the small cube
                    number = Text(str(count), font_size=18, color=WHITE)
                    number.move_to(small_cube.get_center())
                    
                    # Group the cube and its number together
                    small_cube_with_number = VGroup(small_cube, number)
                    cubes.add(small_cube_with_number)
                    
                    # Store in dictionary for easy access
                    cube_dict[count] = small_cube_with_number
                    
                    count += 1
        
        # Add the initial configuration to the scene
        self.add(cubes)
        self.begin_ambient_camera_rotation(rate=0, about="phi")
        self.wait(2)
        
        # Example of swapping cubes (let's swap cube 1 and cube 27)
        cube1 = cube_dict[5]
        cube27 = cube_dict[105]
        
        # Store original positions
        pos1 = cube1.get_center()
        pos27 = cube27.get_center()
        
        # Create the swapping animation
        # First, move cube1 up and out
        self.play(
            cube1.animate.shift(UP * 1.5 + OUT * 1.5),
            run_time=0.5
        )
        
        # Move cube27 to cube1's position
        self.play(
            cube27.animate.move_to(pos1),
            run_time=0.5
        )
        
        # Finally, move cube1 to cube27's original position
        self.play(
            cube1.animate.move_to(pos27),
            run_time=0.5
        )
        
        # Wait at the end to show the final configuration
        self.wait(3)