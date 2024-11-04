from algorithm.Cube import *
import matplotlib.pyplot as plt
import copy

class HillClimbingSearch:
    def __init__(self, n):
        self.n = n
        self.cube = Cube(n)
        self.values = []
        self.current_value = 0
        self.iteration = 0
        self.initial_state = []
        self.final_state = []
    
    def solve(self):
        self.current_value = self.cube.calculate_value()
        print(f"Initial Value: {self.current_value}")
        
        initial_config = copy.deepcopy(self.cube.data)
        list_swap_points = []

        while True:
            self.values.append(self.current_value)
            self.iteration += 1
            better_found = False

            for i in range(self.n**3):
                for j in range(i + 1, self.n**3):
                    pos1 = self.linearpos_to_3dpos(i)
                    pos2 = self.linearpos_to_3dpos(j)

                    self.cube.swap(pos1, pos2)
                    new_value = self.cube.calculate_value()

                    if new_value > self.current_value:
                        print(f"Better Value Found: {new_value} by swapping {pos1} and {pos2}")
                        self.current_value = new_value  
                        better_found = True 
                        break

                    self.cube.swap(pos1, pos2)

                if better_found:
                    list_swap_points.append([self.from_3dpos_to_linearpos(pos1), self.from_3dpos_to_linearpos(pos2)])
                    break

            if not better_found:
                print("No further improvement found. Terminating search.")
                break
        
        self.initial_state = initial_config
        self.final_state = self.cube.data
        
        return list_swap_points, initial_config

    def linearpos_to_3dpos(self, num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = (num % (self.n**2)) % self.n
        return [i, j, k]
    
    def from_3dpos_to_linearpos(self,pos):
        return pos[0] * (self.n**2) + pos[1] * (self.n) + pos[2]
    
    def print_value(self):
        self.cube.print_value()
    
    def getIterations(self):
        return self.iteration
    
    def getCurrentValue(self):
        return self.current_value

    def list_of_values(self):
        return self.values