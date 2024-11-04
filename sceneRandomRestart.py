from manim import *
from manim import Cube as C
import time
from algorithm.StochasticHillClimbing import *
from algorithm.GeneticAlgorithm import *
from algorithm.HillClimbingSearch import *
from algorithm.HillClimbingSearchSteepestAscent import *
from algorithm.HillClimbingSidewaysMove import *
from algorithm.RandomRestartHillClimbing import *
from algorithm.SimulatedAnnealing import *

class CubeWithNumbers(ThreeDScene):
    def construct(self):
        # Set up the camera orientation
        self.set_camera_orientation(phi=30 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES, frame_center=[0,1,0])
        
        # Parameters for the small cubes
        side_length = 0.6  # Side length of each smaller cube
        spacing = 1.0      # Spacing between cubes
        
        # Create the 3x3x3 grid of cubes with numbers
        cubes = VGroup()  # Group to hold all small cubes
        cube_dict = {}    # Dictionary to store cube positions for easy access

        # list_swaps = []
        # list_inits = []

        # for i in range (4):
        #     # swap = [1,25]
        #     temp = Cube(5).data
        #     # list_swaps.append(swap)
        #     list_inits.append(temp)
        
        # list_swap = [[1, 83]]
        
        stochastic_cube = RandomRestartHillClimbing(5, 2)
        list_swaps, list_inits = stochastic_cube.solve()
        
         # Start numbering from 1
        for i in range (len(list_swaps)):
            swap = list_swaps[i]
            init = list_inits[i]
            count = 0
            for x in range(0, 5):
                for y in range(0, 5):
                    for z in range(0, 5):
                        # Create a small cube
                        small_cube = C(side_length=side_length, fill_opacity=0.7)
                        small_cube.shift(x * spacing * RIGHT + y * spacing * UP + z * spacing * OUT)
                        
                        # Create a number for the small cube
                        number = Text(str(init[x][y][z]), font_size=18, color=WHITE)
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
            
            for swap_points in swap:
            
                # Example of swapping cubes (let's swap cube 1 and cube 27)
                cubeA = cube_dict[swap_points[0]]
                cubeB = cube_dict[swap_points[1]]
                
                # Store original positions
                posA = cubeA.get_center()
                posB = cubeB.get_center()
                
                # Create the swapping animation
                # First, move cubeA up and out
                
                # Move cubeB to cubeA's position
                self.play(
                    cubeB.animate.move_to(posA),
                    run_time=0.5
                )
                
                # Finally, move cubeA to cubeB's original position
                self.play(
                    cubeA.animate.move_to(posB),
                    run_time=0.5
                )
                
                temp = cube_dict[swap_points[0]]
                cube_dict[swap_points[0]] = cube_dict[swap_points[1]]
                cube_dict[swap_points[1]] = temp
                
                # Wait at the end to show the final configuration
                self.wait(1)
                
            self.remove(cubes)
            cubes = VGroup()
            
            