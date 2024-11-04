from algorithm.Cube import *
import matplotlib.pyplot as plt
import copy
import time

class StochasticHillClimbing:
    def __init__(self, iterations, n=5):
        self.n = n
        self.cube = Cube(n)
        self.iterations = iterations
        self.list_swap_points = []
        self.values = [] 
        self.num_iterations = 0
        
    def solve(self):
        initial_configuration = copy.deepcopy(self.cube.data)

        start_time = time.time()
        
        for i in range(self.iterations):
            self.num_iterations += 1
            end =  self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point())
            if end:
                break
        
        end_time = time.time() 
        duration = end_time - start_time
        print(f"\n\nSteepest Ascent Algorithm Duration: {duration:.4f} seconds")

        print("\nBest value: ", self.values[-1])
        print("Number of iterations: ", self.num_iterations)

        self.plot_value(initial_configuration, self.cube.data)
        return self.list_swap_points, initial_configuration
    
    def compare_state(self, pos1, pos2):
        current_value = self.cube.calculate_value()
        self.values.append(current_value)
        self.cube.swap(pos1, pos2)
        neighbor_value = self.cube.calculate_value()

        if current_value >= neighbor_value:
            self.cube.swap(pos1, pos2)
        else:
            print(f"Swap {pos1} and {pos2}, current value = {current_value}")
            self.list_swap_points.append([self.from_3dpos_to_linearpos(pos1), self.from_3dpos_to_linearpos(pos2)])
        
        return neighbor_value == 109
    
    def print_value(self):
        self.cube.print_value()
        
    def from_3dpos_to_linearpos(self,pos):
        return pos[0] * (self.n**2) + pos[1] * (self.n) + pos[2]
    
    def plot_value(self, initial_cube_data, final_cube_data):
        # Cube plot
        fig1 = plt.figure(figsize=(12, 6))
        ax1 = fig1.add_subplot(121, projection='3d') 
        self.cube.plot_number_cube(ax1, initial_cube_data, "Initial Configuration")
        ax2 = fig1.add_subplot(122, projection='3d')
        self.cube.plot_number_cube(ax2, final_cube_data, "Final Configuration")
        ax1.view_init(elev=30, azim=30)
        ax2.view_init(elev=30, azim=30)
        plt.tight_layout() 

        # Graph plot
        plt.figure(figsize=(12, 6))
        plt.plot(self.values, linestyle='-')
        plt.title("Stochastic Hill Climbing")
        plt.xlabel("Iteration")
        plt.ylabel("Objective Function Value")
        plt.grid()

        plt.show()
