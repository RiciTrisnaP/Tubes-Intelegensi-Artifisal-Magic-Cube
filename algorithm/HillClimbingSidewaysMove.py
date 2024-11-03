from algorithm.Cube import *
import matplotlib.pyplot as plt

class HillClimbingSidewaysMove:
    def __init__(self, n, max_sideways_moves):
        self.n = n
        self.cube = Cube(n)
        self.max_sideways_moves = max_sideways_moves
        self.values = []
        self.value = 0
        self.iterasi = 0

    def solve(self):
        self.value = self.cube.calculate_value()
        print(f"Initial Value: {self.value}")
        sideways_moves_count = 0
        
        initial_config = self.cube.data
        list_swap_points = []

        while True:
            self.values.append(self.value)
            max_value = self.value
            max_pos1 = None
            max_pos2 = None
            found_better = False
            sideways_moves = []
            
            initial_config = self.cube.data
            list_swap_points = []

            for i in range(self.n**3):
                for j in range(i + 1, self.n**3):
                    pos1 = self.linearpos_to_3dpos(i)
                    pos2 = self.linearpos_to_3dpos(j)

                    self.cube.swap(pos1, pos2)
                    new_value = self.cube.calculate_value()

                    if new_value > max_value:
                        print(f"Better Value Found: {new_value} by swapping {pos1} and {pos2}")
                        max_value = new_value
                        max_pos1 = pos1
                        max_pos2 = pos2
                        found_better = True
                    elif new_value == max_value:
                        sideways_moves.append((pos1, pos2))

                    self.cube.swap(pos1, pos2)
            
            self.iterasi += 1
            if found_better:
                self.cube.swap(max_pos1, max_pos2)
                self.value = max_value
                print(f"Moved to new position with value: {self.value}")
                # sideways_moves_count = 0 
                
                list_swap_points.append([self.from_3dpos_to_linearpos(max_pos1), self.from_3dpos_to_linearpos(max_pos2)])
            elif sideways_moves:
                    best_pos1, best_pos2 = sideways_moves[0]
                    self.cube.swap(best_pos1, best_pos2)
                    self.value = self.cube.calculate_value()
                    sideways_moves_count += 1 
                    print(f"Sideways Move: Swapped {best_pos1} and {best_pos2}. New Value: {self.value}")
                    if sideways_moves_count >= self.max_sideways_moves:
                        print("Maximum sideways moves reached.")
                        break
            else:
                print("No further improvement found.")
                break
        
        print("\nIterasi: ", self.iterasi)
        self.plot_value()
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
    
    def plot_value(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.values, marker='o', linestyle='-', color='b')
        plt.title("Cube Value Through Hill Climbing Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("Cube Value")
        plt.grid()
        plt.tight_layout()
        plt.show()