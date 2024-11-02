from algorithm.Cube import *

class HillClimbingSearch:
    def __init__(self, n):
        self.n = n
        self.cube = Cube(n)
    
    def solve(self):
        current_value = self.cube.calculate_value()
        print(f"Initial Value: {current_value}")

        while True:
            better_found = False

            for i in range(self.n**3):
                for j in range(i + 1, self.n**3):
                    pos1 = self.linearpos_to_3dpos(i)
                    pos2 = self.linearpos_to_3dpos(j)

                    self.cube.swap(pos1, pos2)
                    new_value = self.cube.calculate_value()

                    if new_value > current_value:
                        print(f"Better Value Found: {new_value} by swapping {pos1} and {pos2}")
                        current_value = new_value  
                        better_found = True 
                        break

                    self.cube.swap(pos1, pos2)

                if better_found:
                    break

            if not better_found:
                print("No further improvement found. Terminating search.")
                break

    def linearpos_to_3dpos(self, num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = (num % (self.n**2)) % self.n
        return [i, j, k]
    
    def print_value(self):
        self.cube.print_value()

