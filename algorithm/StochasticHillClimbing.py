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
        self.plot_value()
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
    
    def plot_value(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.values, linestyle='-', color='b')
        plt.title("Cube Value Through Stochastic Hill Climbing Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Cube Value")
        plt.grid()
        plt.tight_layout()
        plt.show()