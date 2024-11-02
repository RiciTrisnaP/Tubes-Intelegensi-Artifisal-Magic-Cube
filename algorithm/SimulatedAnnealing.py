import math
from algorithm.Cube import *

class SimulatedAnnealing:
    def __init__(self, n, iterations, initial_temperature = 1000, cooling_rate = 0.99):
        self.cube = Cube(n)
        self.iterations = iterations
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
    
    def solve(self):
        for i in range(self.iterations):
            T = self.temperature(i)
            if T == 0:
                break
            print("Temp: ", T)
            self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point(), T)

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
