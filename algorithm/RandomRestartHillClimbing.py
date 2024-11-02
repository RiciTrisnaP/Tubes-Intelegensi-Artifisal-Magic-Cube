from algorithm.Cube import *
from algorithm.HillClimbingSearchSteepestAscent import *
import random

class RandomRestartHillClimbing:
    def __init__(self, n, max_restarts):
        self.n = n
        self.max_restarts = max_restarts
        self.cube = Cube(5)

    def solve(self):
        listSwaps = []
        listInits = []
        
        for i in range(self.max_restarts):
            print(f"Random Restart Hill Climbing iteration-{i}")
            print(" ")
            cube = HillClimbingSearchSteepestAscent(5)
            tempSwap, tempInit = cube.solve()
            listSwaps.append(tempSwap)
            listInits.append(tempInit)

            if (cube.value == 109):
                print("Solved")
                break
        self.cube = cube
        
        return listSwaps, listInits 

    def print_value(self):
        self.cube.print_value()

