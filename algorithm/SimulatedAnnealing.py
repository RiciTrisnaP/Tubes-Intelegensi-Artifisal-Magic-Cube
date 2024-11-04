import math
import random
import matplotlib.pyplot as plt
from algorithm.Cube import *
import copy

class SimulatedAnnealing:
    def __init__(self, n, max_iterations=10000, initial_temperature=1000, cooling_rate=0.99):
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
        while True and self.iteration < self.max_iterations:
            T = self.temperature(self.iteration)
            if T <= 0:
                break
            print("Temp: ", T)
            self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point(), T)

            current_value = self.cube.calculate_value()
            self.values.append(current_value)

            self.iteration += 1

        print("Stuck: ", self.stuck)
        self.plot_value(initial_config, self.cube.data)
        return self.list_swap_points, initial_config

    def temperature(self, i):
        return self.initial_temperature * pow(self.cooling_rate, i) 
    
    def compare_state(self, pos1, pos2, T):        
        current_value = self.cube.calculate_value()
        self.cube.swap(pos1, pos2)
        neighbor_value = self.cube.calculate_value()

        deltaE = (neighbor_value - current_value)

        print("pos1: ", pos1, "pos2: ", pos2, "current value: ", current_value, "neighbor value: ", neighbor_value, "difference: ", deltaE)

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
            print("Prob: ", prob, " threshold: ", threshold)
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
        plt.title("Cube Value Through Hill Climbing Steepest Ascent")
        plt.xlabel("Iteration")
        plt.ylabel("Value")
        plt.grid()

        plt.show()

