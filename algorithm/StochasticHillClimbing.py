from algorithm.Cube import *
import matplotlib.pyplot as plt

class StochasticHillClimbing:
    def __init__(self, n, iterations):
        self.n = n
        self.cube = Cube(n)
        self.iterations = iterations
        self.list_swap_points = []
        self.values = [] 
        self.num_iterations = 0
        
    def solve(self):
        initial_configuration = self.cube.data
        
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
        fig = plt.figure(figsize=(12, 12))

        ax1 = fig.add_subplot(221, projection='3d')
        self.plot_number_cube(ax1, initial_cube_data, "Initial Configuration")

        ax2 = fig.add_subplot(222, projection='3d')
        self.plot_number_cube(ax2, final_cube_data, "Final Configuration")

        plt.subplots_adjust(hspace=0.4)

        ax3 = fig.add_subplot(223)
        ax3.plot(self.values, marker='o', linestyle='-', color='b')
        ax3.set_title("Cube Value Through Hill Climbing Iterations")
        ax3.set_xlabel("Iteration")
        ax3.set_ylabel("Cube Value")
        ax3.grid()

        plt.tight_layout()
        plt.show()

    def plot_number_cube(self, ax, cube_data, title):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    ax.text(i, j, k, str(cube_data[i, j, k]),
                            color='black', fontsize=8, ha='center', va='center', alpha=1.0)

        ax.set_xlim([0, self.n])
        ax.set_ylim([0, self.n])
        ax.set_zlim([0, self.n])

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.set_title(title)