from algorithm.Cube import *
import matplotlib.pyplot as plt
import random
import copy
import time

class HillClimbingSidewaysMove:
    def __init__(self, max_sideways_moves, n=5):
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
        
        initial_config = copy.deepcopy(self.cube.data)
        list_swap_points = []
        sideways_moves = [] 

        start_time = time.time()

        while True:
            self.values.append(self.value)
            max_value = self.value
            max_pos1 = None
            max_pos2 = None
            found_better = False

            for i in range(self.n**3):
                for j in range(i + 1, self.n**3):
                    pos1 = self.linearpos_to_3dpos(random.randint(0, i))
                    pos2 = self.linearpos_to_3dpos(random.randint(0, j))

                    self.cube.swap(pos1, pos2)
                    new_value = self.cube.calculate_value()

                    if new_value > max_value:
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
                
                list_swap_points.append([self.from_3dpos_to_linearpos(max_pos1), self.from_3dpos_to_linearpos(max_pos2)])
            elif sideways_moves:
                best_pos1, best_pos2 = sideways_moves[-1]
                self.cube.swap(best_pos1, best_pos2)
                self.value = self.cube.calculate_value()
                sideways_moves_count += 1 
                list_swap_points.append([self.from_3dpos_to_linearpos(best_pos1), self.from_3dpos_to_linearpos(best_pos2)])
                print(f"Sideways Move: Swapped {best_pos1} and {best_pos2}. New Value: {self.value}")
                if sideways_moves_count >= self.max_sideways_moves:
                    print("Maximum sideways moves reached.")
                    break
            else:
                break
        
        end_time = time.time() 
        duration = end_time - start_time
        print(f"\n\nHill Climbing Sideways Algorithm Duration: {duration:.4f} seconds")

        print("\nBest value: ", self.values[-1])
        print("Number of iterations: ", self.iterasi)
        self.plot_value(initial_config, self.cube.data)
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
    
    def plot_value(self, initial_cube_data, final_cube_data):
        fig1 = plt.figure(figsize=(12, 6))
        ax1 = fig1.add_subplot(121, projection='3d') 
        self.cube.plot_number_cube(ax1, initial_cube_data, "Initial Configuration")
        ax2 = fig1.add_subplot(122, projection='3d')
        self.cube.plot_number_cube(ax2, final_cube_data, "Final Configuration")
        ax1.view_init(elev=30, azim=30)
        ax2.view_init(elev=30, azim=30)
        plt.tight_layout() 

        plt.figure(figsize=(12, 6))
        plt.plot(self.values, marker='o', linestyle='-', color='b')
        plt.title("Cube Value Through Hill Climbing Sideways Move Ascent")
        plt.xlabel("Iteration")
        plt.ylabel("Value")
        plt.grid()

        plt.show()