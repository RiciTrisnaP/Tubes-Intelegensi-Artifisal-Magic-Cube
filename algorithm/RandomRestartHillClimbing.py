from algorithm.Cube import *
from algorithm.HillClimbingSearchSteepestAscent import *
import random

class RandomRestartHillClimbing:
    def __init__(self, n, max_restarts):
        self.n = n
        self.max_restarts = max_restarts
        self.cube = Cube(5)
        self.values = []
        self.restart = 0
        self.iteration = 0

    def solve(self):
        listSwaps = []
        listInits = []
        
        for i in range(self.max_restarts):
            self.restart += 1
            print(f"Random Restart Hill Climbing iteration-{i + 1}")
            print(" ")
            cube = HillClimbingSearchSteepestAscent(5)
            tempSwap, tempInit = cube.solve()
            listSwaps.append(tempSwap)
            listInits.append(tempInit)

            self.values.append(cube.value)
            if (cube.value == 109):
                print("Solved")
                break

        self.cube = cube
        
        print("Jumlah restart: ", self.restart)
        self.plot_value()
        return listSwaps, listInits 

    def print_value(self):
        self.cube.print_value()

    def plot_value(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.values, marker='o', linestyle='-', color='b')
        plt.title("Cube Value Through Hill Climbing Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Cube Value")
        plt.grid()
        plt.tight_layout()
        plt.show()