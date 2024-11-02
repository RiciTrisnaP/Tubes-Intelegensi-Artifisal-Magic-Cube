from algorithm.Cube import *

class HillClimbingSidewaysMove:
    def __init__(self, n, max_sideways_moves):
        self.n = n
        self.cube = Cube(n)
        self.max_sideways_moves = max_sideways_moves

    def solve(self):
        sideways_moves_count = 0
        while True:
            print("Sideways: ", sideways_moves_count)
            end, pos1, pos2 = self.search_best_neighbor()
            if end:
                break
            
            self.cube.swap(pos1, pos2)
            
            if pos1 is not None and pos2 is not None:
                if self.cube.calculate_value() == self.cube.calculate_value():
                    sideways_moves_count += 1
                    
                    if sideways_moves_count >= self.max_sideways_moves:
                        print("Maximum sideways moves reached.")
                        break
        
    def search_best_neighbor(self):
        initial_value = self.cube.calculate_value()
        max_value = initial_value
        max_pos1 = None
        max_pos2 = None
        sideways_moves = []

        print(f"Initial Value: {initial_value}")

        for i in range(self.n**3):
            for j in range(i, self.n**3):
                pos1 = self.linearpos_to_3dpos(i)
                pos2 = self.linearpos_to_3dpos(j)
                self.cube.swap(pos1, pos2)
                current_value = self.cube.calculate_value()

                if current_value > max_value:
                    max_value = current_value
                    max_pos1 = pos1
                    max_pos2 = pos2
                elif current_value == max_value:
                    sideways_moves.append((pos1, pos2))

                self.cube.swap(pos1, pos2)

        print(f"Max Value: {max_value}")

        if max_value == initial_value and sideways_moves:
            best_pos1, best_pos2 = sideways_moves[0]
            return False, best_pos1, best_pos2 
        else:
            return max_value <= initial_value, max_pos1, max_pos2  
        
    def linearpos_to_3dpos(self, num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = num % self.n
        return [i, j, k]
    
    def print_value(self):
        self.cube.print_value()