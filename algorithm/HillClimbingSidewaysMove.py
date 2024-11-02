from algorithm.Cube import *

class HillClimbingSidewaysMove:
    def __init__(self, n, max_sideways_moves):
        self.n = n
        self.cube = Cube(n)
        self.max_sideways_moves = max_sideways_moves

    def solve(self):
        current_value = self.cube.calculate_value()
        print(f"Initial Value: {current_value}")
        sideways_moves_count = 0

        while True:
            max_value = current_value
            max_pos1 = None
            max_pos2 = None
            found_better = False
            sideways_moves = []

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

            if found_better:
                self.cube.swap(max_pos1, max_pos2)
                current_value = max_value
                print(f"Moved to new position with value: {current_value}")
                # sideways_moves_count = 0 
            elif sideways_moves:
                    best_pos1, best_pos2 = sideways_moves[0]
                    self.cube.swap(best_pos1, best_pos2)
                    current_value = self.cube.calculate_value()
                    sideways_moves_count += 1 
                    print(f"Sideways Move: Swapped {best_pos1} and {best_pos2}. New Value: {current_value}")
                    if sideways_moves_count >= self.max_sideways_moves:
                        print("Maximum sideways moves reached.")
                        break
            else:
                print("No further improvement found.")
                break

    def linearpos_to_3dpos(self, num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = (num % (self.n**2)) % self.n
        return [i, j, k]
    
    def print_value(self):
        self.cube.print_value()