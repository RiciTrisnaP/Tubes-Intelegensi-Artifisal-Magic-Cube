from algorithm.Cube import *
from algorithm.HillClimbingSearch import *
import matplotlib.pyplot as plt
import time

class RandomRestartHillClimbing:
    def __init__(self, max_restarts, n=5):
        self.n = n
        self.max_restarts = max_restarts
        self.cube = Cube(5)
        self.all_values = []
        self.restart = 0
        self.best_initial_state = []
        self.best_final_state = []
        self.best_value = 0

    def solve(self):
        listSwaps = []
        listInits = []
        
        start_time = time.time()

        for i in range(self.max_restarts):
            print(f"\nRandom Restart Hill Climbing iteration {i + 1}")
            self.restart += 1
            
            cube = HillClimbingSearch(5)
            tempSwap, tempInit = cube.solve()
            listSwaps.append(tempSwap)
            listInits.append(tempInit)

            print(f"\nHill Climbing with {cube.getIterations()} iterations and best value {cube.getCurrentValue()}")

            self.all_values.append(cube.list_of_values())

            if cube.getCurrentValue() >= self.best_value:
                self.best_value = cube.getCurrentValue()
                self.best_initial_state = cube.getInitialState()
                self.best_final_state = cube.getFinalState()
            
            if (cube.getCurrentValue() == 109):
                print("Solved")
                break

        end_time = time.time() 
        duration = end_time - start_time
        print(f"\n\nSteepest Ascent Algorithm Duration: {duration:.4f} seconds")

        self.cube = cube.cube
        
        print("\nNumber of restarts: ", self.restart)
        self.plot_value()
        return listSwaps, listInits 

    def print_value(self):
        self.cube.print_value()

    def plot_value(self):
        # Cube plot
        fig1 = plt.figure(figsize=(12, 6))
        ax1 = fig1.add_subplot(121, projection='3d') 
        self.cube.plot_number_cube(ax1, self.best_initial_state, "Best Initial Configuration")
        ax2 = fig1.add_subplot(122, projection='3d')
        self.cube.plot_number_cube(ax2, self.best_final_state, "Best Final Configuration")
        ax1.view_init(elev=30, azim=30)
        ax2.view_init(elev=30, azim=30)
        plt.tight_layout() 
        
        plt.figure(figsize=(12, 6))

        for i, values in enumerate(self.all_values):
            plt.plot(values, marker='o', linestyle='-', label=f"Restart {i + 1}")

        plt.title("Cube Value Through Hill Climbing Iterations for Each Restart")
        plt.xlabel("Iteration")
        plt.ylabel("Cube Value")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()