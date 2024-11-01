import numpy as np
import random

class Cube:
    def __init__(self, n):
        self.n = n
        self.magic_number = (self.n**3 + 1) / 2 * n
        self.data = self.generate_random_config(n)
    
    def generate_random_config(self, n):
        # Generate a list of unique numbers from 1 to 125
        unique_numbers = random.sample(range(1, (n**3)+1), n**3)
        
        # Create a 5x5x5 data and fill it with unique random integers
        data = np.array(unique_numbers).reshape((n, n, n))
        return data

    def swap(self, pos1, pos2):
        # Swap the values at the specified positions in the data
        temp = self.data[pos1[0],pos1[1],pos1[2]]
        self.data[pos1[0],pos1[1],pos1[2]] = self.data[pos2[0],pos2[1],pos2[2]]
        self.data[pos2[0],pos2[1],pos2[2]] = temp
    


class stochastic_hill_climbing:
    def __init__(self, n):
        self.cube = Cube(n)
    
    def main_shc(self,nmax):
        for i in range(nmax):
            end = self.compare_state(self.generate_random_point(), self.generate_random_point())
            if end :
                # print(self.cube.data)
                break
    
    def compare_state(self,pos1,pos2):
        current_value = self.calculate_value()
        self.cube.swap(pos1,pos2)
        neighbor_value = self.calculate_value()

        print("pos1 : " , pos1 , "  pos2: ", pos2 , "  current value : " , current_value , ", neighbor value" , neighbor_value)

        if current_value >= neighbor_value:
            self.cube.swap(pos1,pos2)
        
        return neighbor_value == 109

    def generate_random_point(self):
        generated_point = []
        for i in range(self.cube.n):
            value = random.randint(0, self.cube.n - 1)  # Generate a random value
            generated_point.append(value)
        return generated_point

    def calculate_value(self):
        return self.calculate_column_value() + self.calculate_row_value() + self.calculate_height_value() + self.calculate_side_diagonal_value() + self.calculate_space_diagonal_value()

    def calculate_column_value(self):
        total = 0
        for i in range(self.cube.n):
            for y in range(self.cube.n):
                sum = 0
                for z in range(self.cube.n):
                    sum += self.cube.data[i,y,z]
                if sum == self.cube.magic_number:
                    total += 1
        return total
    
    def calculate_row_value(self):
        total = 0
        for i in range(self.cube.n):
            for z in range(self.cube.n):
                sum = 0
                for y in range(self.cube.n):
                    sum += self.cube.data[i,y,z]
                if sum == self.cube.magic_number:
                    total += 1
        return total

    def calculate_height_value(self):
        total = 0
        for y in range(self.cube.n):
            for z in range(self.cube.n):
                sum = 0
                for i in range(self.cube.n):
                    sum += self.cube.data[i,y,z]
                if sum == self.cube.magic_number:
                    total += 1
        return total

    def calculate_side_diagonal_value(self):
        # cuma berlaku 5x5x5
        total = 0
        for z in range(self.cube.n):
            sum = 0;       
            for i in range(self.cube.n):
                sum +=  self.cube.data[z, i, i]
            if sum == self.cube.magic_number:
                total += 1

            sum = 0
            for y in range(self.cube.n):
                sum += self.cube.data[z,y, (self.cube.n - 1)-y]
            if sum == self.cube.magic_number:
                total += 1

        for y in range(self.cube.n):
            sum = 0;       
            for z in range(self.cube.n):
                sum +=  self.cube.data[z, y, z]
            if sum == self.cube.magic_number:
                total += 1
            
            sum = 0
            for i in range(self.cube.n):
                sum += self.cube.data[(self.cube.n - 1)-i, y, i]
            if sum == self.cube.magic_number:
                total += 1
            
        for i in range(self.cube.n):
            sum = 0;       
            for y in range(self.cube.n):
                sum +=  self.cube.data[y,y,i]
            if sum == self.cube.magic_number:
                total += 1
            
            sum = 0
            for z in range(self.cube.n):
                sum += self.cube.data[z,(self.cube.n - 1)-z, i]
            if sum == self.cube.magic_number:
                total += 1

        return total

    def calculate_space_diagonal_value(self):
            total = 0

            sum = 0
            for i in range(self.cube.n):
                sum += self.cube.data[i,i,i]
            if sum == self.cube.magic_number:
                total += 1
            # print(sum)
            
            sum = 0
            for i in range(self.cube.n):
                sum += self.cube.data[i,(self.cube.n - 1)-i, i]
            if sum == self.cube.magic_number:
                total += 1
            # print(sum)

            sum = 0
            for i in range(self.cube.n):
                sum += self.cube.data[i, i, (self.cube.n - 1)-i]
            if sum == self.cube.magic_number:
                total += 1
            # print(sum)

            sum = 0
            for i in range(self.cube.n):
                sum += self.cube.data[i, (self.cube.n - 1)-i, (self.cube.n - 1)-i]
            if sum == self.cube.magic_number:
                total += 1
            # print(sum)
            
            # print(total)
            return total



    
# Example usage
random_cube = stochastic_hill_climbing(5)

random_cube.main_shc(3)