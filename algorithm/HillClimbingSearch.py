from algorithm.Cube import *

class HillClimbingSearch:
    def __init__(self, n):
        self.n = n
        self.cube = Cube(n)
    
    def solve(self):
        # Set the initial value of the cube
        current_value = self.cube.calculate_value()
        print(f"Initial Value: {current_value}")

        while True:
            # Search for the best neighbor
            better_found = False  # Flag to track whether a better move is found

            for i in range(self.n**3):
                for j in range(i + 1, self.n**3):  # Avoid redundant swaps 
                    pos1 = self.linearpos_to_3dpos(i)
                    pos2 = self.linearpos_to_3dpos(j)

                    # Swap the positions
                    self.cube.swap(pos1, pos2)
                    new_value = self.cube.calculate_value()

                    # Check if the new position is better than the current best
                    if new_value > current_value:
                        print(f"Better Value Found: {new_value} by swapping {pos1} and {pos2}")
                        current_value = new_value  # Update the current value
                        better_found = True  # Indicate that a better move was found
                        break  # Exit the inner loop since we made a move

                    # Swap back to restore original state
                    self.cube.swap(pos1, pos2)

                if better_found:  # Break the outer loop too if we found a better value
                    break

            if not better_found:  # If no better move was found, terminate the search
                print("No further improvement found. Terminating search.")
                break

    def linearpos_to_3dpos(self, num):
        i = num // (self.n**2)
        j = (num % (self.n**2)) // self.n 
        k = num % self.n
        return [i, j, k]

