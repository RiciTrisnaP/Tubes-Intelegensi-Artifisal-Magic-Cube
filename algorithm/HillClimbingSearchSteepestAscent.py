from algorithm.Cube import *
import matplotlib.pyplot as plt

class HillClimbingSearchSteepestAscent: 
    def __init__(self, n):
        self.n = n
        self.cube = Cube(n)
        self.iterasi = 0
        self.value= 0
        self.values = [] 

    def solve(self):
        self.value = self.cube.calculate_value()
        print(f"Initial Value: {self.value}")
        
        initial_config = self.cube.data
        list_swap_points = []
        
        while True:
            self.values.append(self.value)
            max_value = self.value
            max_pos1 = None
            max_pos2 = None
            found_better = False

            for i in range(self.n**3):
                for j in range(i + 1, self.n**3):
                    pos1 = self.linearpos_to_3dpos(i)
                    pos2 = self.linearpos_to_3dpos(j)

                    self.cube.swap(pos1, pos2)
                    new_value = self.cube.calculate_value()

                    if new_value > max_value:
                        # print(f"Better Value Found: {new_value} by swapping {pos1} and {pos2}")
                        max_value = new_value
                        max_pos1 = pos1
                        max_pos2 = pos2
                        found_better = True

                    self.cube.swap(pos1, pos2)
                    
            self.iterasi += 1
            if found_better:
                self.cube.swap(max_pos1, max_pos2)
                self.value = max_value
                print(f"Moved to new position with value: {self.value} by swapping {max_pos1} and {max_pos2}")
                
                list_swap_points.append([self.from_3dpos_to_linearpos(max_pos1), self.from_3dpos_to_linearpos(max_pos2)])
            else:
                print("No further improvement found.")
                print(f"Maximum iteration: {self.iterasi}")
                break 
        
        print("\nIterasi: ", self.iterasi)
        # self.plot_value()
        return list_swap_points,initial_config

    def linearpos_to_3dpos(self, num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = (num % (self.n**2)) % self.n
        return [i, j, k]

    
    def from_3dpos_to_linearpos(self,pos):
        return pos[0] * (self.n**2) + pos[1] * (self.n) + pos[2]
    
    def print_value(self):
        self.cube.print_value()
    
    def plot_value(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.values, marker='o', linestyle='-', color='b')
        plt.title("Cube Value Through Hill Climbing Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Cube Value")
        plt.grid()
        plt.tight_layout()
        plt.show()