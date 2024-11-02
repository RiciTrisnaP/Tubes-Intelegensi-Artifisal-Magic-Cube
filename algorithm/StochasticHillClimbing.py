from algorithm.Cube import *

class StochasticHillClimbing:
    def __init__(self, n, iterations):
        self.cube = Cube(n)
        self.iterations = iterations
        
    def solve(self):
        for i in range(self.iterations):
            end =  self.compare_state(self.cube.generate_random_point(), self.cube.generate_random_point())
            if end:
                break
    
    def compare_state(self, pos1, pos2):
        current_value = self.cube.calculate_value()
        self.cube.swap(pos1, pos2)
        neighbor_value = self.cube.calculate_value()

        print("pos1:", pos1, "pos2:", pos2, "current value:", current_value, "neighbor value:", neighbor_value)

        if current_value >= neighbor_value:
            self.cube.swap(pos1, pos2)
        
        return neighbor_value == 109