from algorithm.Cube import *
import matplotlib.pyplot as plt
import copy

class StochasticHillClimbing:
    def __init__(self, n, iterations):
        self.n = n
        self.cube = Cube(n)
        self.iterations = iterations
        self.list_swap_points = []
        self.values = [] 
        self.num_iterations = 0
        
    def solve(self):
        initial_configuration = copy.deepcopy(self.cube.data)
        
        for i in range(self.iterations):
            self.num_iterations += 1
            end =  self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point())
            if end:
                break
        
        print("\nIterasi: ", self.num_iterations)
        self.plot_value(initial_configuration, self.cube.data)
        return self.list_swap_points, initial_configuration
    
    def compare_state(self, pos1, pos2):
        current_value = self.cube.calculate_value()
        self.values.append(current_value)
        self.cube.swap(pos1, pos2)
        neighbor_value = self.cube.calculate_value()

        print("pos1:", pos1, "pos2:", pos2, "current value:", current_value, "neighbor value:", neighbor_value)

        if current_value >= neighbor_value:
            self.cube.swap(pos1, pos2)
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
        plt.plot(self.values, marker='o', linestyle='-', color='b')
        plt.title("Cube Value Through Hill Climbing Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Cube Value")
        plt.grid()
        plt.legend()

        plt.show()
