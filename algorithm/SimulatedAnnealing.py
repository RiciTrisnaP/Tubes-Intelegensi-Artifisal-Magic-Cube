import math
from algorithm.Cube import *

class SimulatedAnnealing:
    def __init__(self, n, iterations, initial_temperature = 1000, cooling_rate = 0.99):
        self.cube = Cube(n)
        self.iterations = iterations
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.list_swap_points = []
        self.n = n
    
    def solve(self):
        initial_config = self.cube.data
        for i in range(self.iterations):
            T = self.temperature(i)
            if T == 0:
                break
            print("Temp: ", T)
            self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point(), T)
        
        return self.list_swap_points, initial_config

    def temperature(self, i):
        return self.initial_temperature * pow(self.cooling_rate, i) 
    
    def compare_state(self, pos1, pos2, T):
        if T <= 0:
            return
        
        current_value = self.cube.calculate_value()
        self.cube.swap(pos1, pos2)
        neighbor_value = self.cube.calculate_value()

        deltaE = (neighbor_value - current_value)

        print("pos1: ", pos1, "pos2: ", pos2, "current value: ", current_value, "neighbor value: ", neighbor_value, "difference: ", deltaE)

        if deltaE >= 0:
            return
        else:
            threshold = 0.3
            prob = math.exp(deltaE / T) 
            print("Prob: ", prob, " threshold: ", threshold)
            if T > 0 and prob >= threshold:
                return
            else:
                self.cube.swap(pos1, pos2)
                self.list_swap_points.append([self.from_3dpos_to_linearpos(pos1), self.from_3dpos_to_linearpos(pos2)])
    
    def from_3dpos_to_linearpos(self,pos):
        return pos[0] * (self.n**2) + pos[1] * (self.n) + pos[2]

    def print_value(self):
        self.cube.print_value()
