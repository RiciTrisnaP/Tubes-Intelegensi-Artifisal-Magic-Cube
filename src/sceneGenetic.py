from manim import *
from manim import Cube as C
import time
from algorithm.GeneticAlgorithm import *


class CubeGenetic(ThreeDScene):
    def __init__(self, list_best, **kwargs):
        super().__init__(**kwargs)
        self.list_best = list_best

    def construct(self):
        self.set_camera_orientation(phi=30 * DEGREES, theta=0 * DEGREES, gamma=90 * DEGREES, frame_center=[0,1,0])
        
        side_length = 0.6 
        spacing = 1.0   
        cubes = VGroup()  
        
        for i in range (len(self.list_best)):
            temp = self.list_best[i]
            for x in range(0, 5):
                for y in range(0, 5):
                    for z in range(0, 5):
                        small_cube = C(side_length=side_length, fill_opacity=0.7)
                        small_cube.shift(x * spacing * RIGHT + y * spacing * UP + z * spacing * OUT)
                        
                        number = Text(str(temp[x][y][z]), font_size=18, color=WHITE)
                        number.move_to(small_cube.get_center())
                        small_cube_with_number = VGroup(small_cube, number)
                        cubes.add(small_cube_with_number)
            
            self.add(cubes)
            self.begin_ambient_camera_rotation(rate=0, about="phi")
            self.wait(2)
        
            self.remove(cubes)
            cubes = VGroup()