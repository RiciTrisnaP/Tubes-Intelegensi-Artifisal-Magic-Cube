import math
import random
import matplotlib.pyplot as plt
from algorithm.Cube import *
import copy
import time

class SimulatedAnnealing:
    def __init__(self, max_iterations = 10000, initial_temperature = 1000, cooling_rate = 0.99, n = 5):
        self.cube = Cube(n)
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.list_swap_points = []
        self.probabilities = []
        self.threshold = [] 
        self.n = n
        self.stuck = 0
        self.values = [] 
        self.max_iterations = max_iterations
        self.iteration = 0

    def solve(self):
        initial_config = copy.deepcopy(self.cube.data)

        start_time = time.time()

        while True and self.iteration < self.max_iterations:
            T = self.temperature(self.iteration)
            if T <= 0:
                break

            self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point(), T)

            current_value = self.cube.calculate_value()
            self.values.append(current_value)

            self.iteration += 1
        
        end_time = time.time() 
        duration = end_time - start_time
        print(f"\n\nSteepest Ascent Algorithm Duration: {duration:.4f} seconds")

        print("\nLast value: ", self.values[-1])
        print("Number of stucks: ", self.stuck, end = "\n\n")
        self.plot_value(initial_config, self.cube.data)
        return self.list_swap_points, initial_config

    def temperature(self, i):
        return self.initial_temperature * pow(self.cooling_rate, i) 
    
    def compare_state(self, pos1, pos2, T):        
        current_value = self.cube.calculate_value()
        self.cube.swap(pos1, pos2)
        neighbor_value = self.cube.calculate_value()

        deltaE = (neighbor_value - current_value)

        if deltaE >= 0:
            self.probabilities.append(1.0)
            self.threshold.append(0)
            return
        else:
            self.stuck += 1
            threshold = random.uniform(0, 1)
            self.threshold.append(threshold)
            prob = math.exp(deltaE / T) 
            self.probabilities.append(prob)
            if T > 0 and prob >= threshold:
                return
            else:
                self.cube.swap(pos1, pos2)
                self.list_swap_points.append([self.from_3dpos_to_linearpos(pos1), self.from_3dpos_to_linearpos(pos2)])

    def from_3dpos_to_linearpos(self, pos):
        return pos[0] * (self.n**2) + pos[1] * (self.n) + pos[2]

    def print_value(self):
        self.cube.print_value()

    def plot_value(self, initial_cube_data, final_cube_data):
        fig1 = plt.figure(figsize=(12, 6))
        ax1 = fig1.add_subplot(121, projection='3d') 
        self.cube.plot_number_cube(ax1, initial_cube_data, "Initial Configuration")
        ax2 = fig1.add_subplot(122, projection='3d')
        self.cube.plot_number_cube(ax2, final_cube_data, "Final Configuration")
        ax1.view_init(elev=30, azim=30)
        ax2.view_init(elev=30, azim=30)
        plt.tight_layout() 

        fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        filtered_probabilities = [prob for prob in self.probabilities if prob < 1.0]
        filtered_indices = [idx for idx, prob in enumerate(self.probabilities) if prob < 1.0]
        
        ax1.plot(filtered_indices, filtered_probabilities, label='Probability', linestyle='-')
        ax1.set_title("Probability Values")
        ax1.set_xlabel("Iteration")
        ax1.set_ylabel("Probability Values")
        ax1.grid()
        ax1.legend()

        ax2.plot(self.values, color='g', label='Cube Value', linestyle='-')
        ax2.set_title("Cube Values Throughout Simulated Annealing")
        ax2.set_xlabel("Iteration")
        ax2.set_ylabel("Cube Value")
        ax2.grid()
        ax2.legend()
        
        plt.show()