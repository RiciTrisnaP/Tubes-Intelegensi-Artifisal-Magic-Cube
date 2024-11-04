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

class CubeWithNumbersRR(ThreeDScene):
    def __init__(self, list_swaps, list_inits, **kwargs):
        super().__init__(**kwargs)
        self.list_swaps = list_swaps
        self.list_inits = list_inits

    def construct(self):
        self.set_camera_orientation(phi=30 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES, frame_center=[0,1,0])
        
        side_length = 0.6 
        spacing = 1.0    
        
        cubes = VGroup() 
        cube_dict = {}  

        for i in range (len(self.list_swaps)):
            swap = self.list_swaps[i]
            init = self.list_inits[i]
            count = 0
            for x in range(0, 5):
                for y in range(0, 5):
                    for z in range(0, 5):
                        # Buat kubus kecil
                        small_cube = C(side_length=side_length, fill_opacity=0.7)
                        small_cube.shift(x * spacing * RIGHT + y * spacing * UP + z * spacing * OUT)
                        
                        # Masukan angka
                        number = Text(str(init[x][y][z]), font_size=18, color=WHITE)
                        number.move_to(small_cube.get_center())
                        small_cube_with_number = VGroup(small_cube, number)
                        cubes.add(small_cube_with_number)
                        cube_dict[count] = small_cube_with_number
                        count += 1

            self.add(cubes)
            self.begin_ambient_camera_rotation(rate=0, about="phi")
            self.wait(2)
            
            for swap_points in swap:
                cubeA = cube_dict[swap_points[0]]
                cubeB = cube_dict[swap_points[1]]
                posA = cubeA.get_center()
                posB = cubeB.get_center()

                self.play(
                    cubeB.animate.move_to(posA),
                    run_time=0.5
                )
                
                self.play(
                    cubeA.animate.move_to(posB),
                    run_time=0.5
                )
                
                temp = cube_dict[swap_points[0]]
                cube_dict[swap_points[0]] = cube_dict[swap_points[1]]
                cube_dict[swap_points[1]] = temp

                self.wait(1)
                
            self.remove(cubes)
            cubes = VGroup()