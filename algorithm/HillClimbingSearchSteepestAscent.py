from algorithm.Cube import *

class HillClimbingSearchSteepestAscent:
    def __init__(self, n):
        self.n = n
        self.cube = Cube(n)

    def solve(self):
        while True:
            end, pos1, pos2 = self.search_best_neighbor()
            if end:
                break
            self.cube.swap(pos1, pos2)
        
    def search_best_neighbor(self):
        initial_value = self.cube.calculate_value()
        max_value = initial_value
        max_pos1 = None
        max_pos2 = None

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

                self.cube.swap(pos1, pos2)

        print(f"Max Value: {max_value}")
        
        return max_value <= initial_value, max_pos1, max_pos2
        
    
    def linearpos_to_3dpos(self,num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = (i % (self.n**2)) % self.n
        return [i,j,k]
    
    def print_value(self):
        self.cube.print_value()