from algorithm.Cube import *
from algorithm.HillClimbingSearch import *
import matplotlib.pyplot as plt

class RandomRestartHillClimbing:
    def __init__(self, n, max_restarts):
        self.n = n
        self.max_restarts = max_restarts
        self.cube = Cube(5)
        self.all_values = []
        self.restart = 0

    def solve(self):
        listSwaps = []
        listInits = []
        
        for i in range(self.max_restarts):
            print(f"Random Restart Hill Climbing iteration-{i + 1}")
            self.restart += 1
            
            cube = HillClimbingSearch(5)
            tempSwap, tempInit = cube.solve()
            listSwaps.append(tempSwap)
            listInits.append(tempInit)

            print(f"Random Restart Hill Climbing iteration-{i + 1} with iterations-{cube.getIterations()}")

            self.all_values.append(cube.list_of_values())

            if (cube.getCurrentValue() == 109):
                print("Solved")
                break

        self.cube = cube
        
        print("Jumlah restart: ", self.restart)
        self.plot_value()
        return listSwaps, listInits 

    def print_value(self):
        self.cube.print_value()

    def plot_value(self):
        # Cube plot
        fig1 = plt.figure(figsize=(12, 6))
        ax1 = fig1.add_subplot(121, projection='3d') 
        self.cube.plot_number_cube(ax1, initial_cube_data, "Initial Configuration")
        ax2 = fig1.add_subplot(122, projection='3d')
        self.cube.plot_number_cube(ax2, final_cube_data, "Final Configuration")
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