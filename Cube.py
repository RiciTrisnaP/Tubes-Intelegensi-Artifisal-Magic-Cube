import numpy as np
import random
import math

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
    
    def calculate_value(self):
        return self.calculate_column_value() + self.calculate_row_value() + self.calculate_height_value() + self.calculate_side_diagonal_value() + self.calculate_space_diagonal_value()

    def calculate_column_value(self):
        total = 0
        for i in range(self.n):
            for y in range(self.n):
                sum = 0
                for z in range(self.n):
                    sum += self.data[i,y,z]
                if sum == self.magic_number:
                    total += 1
        return total
    
    def calculate_row_value(self):
        total = 0
        for i in range(self.n):
            for z in range(self.n):
                sum = 0
                for y in range(self.n):
                    sum += self.data[i,y,z]
                if sum == self.magic_number:
                    total += 1
        return total

    def calculate_height_value(self):
        total = 0
        for y in range(self.n):
            for z in range(self.n):
                sum = 0
                for i in range(self.n):
                    sum += self.data[i,y,z]
                if sum == self.magic_number:
                    total += 1
        return total

    def calculate_side_diagonal_value(self):
        # cuma berlaku 5x5x5
        total = 0
        for z in range(self.n):
            sum = 0;       
            for i in range(self.n):
                sum +=  self.data[z, i, i]
            if sum == self.magic_number:
                total += 1

            sum = 0
            for y in range(self.n):
                sum += self.data[z,y, (self.n - 1)-y]
            if sum == self.magic_number:
                total += 1

        for y in range(self.n):
            sum = 0;       
            for z in range(self.n):
                sum +=  self.data[z, y, z]
            if sum == self.magic_number:
                total += 1
            
            sum = 0
            for i in range(self.n):
                sum += self.data[(self.n - 1)-i, y, i]
            if sum == self.magic_number:
                total += 1
            
        for i in range(self.n):
            sum = 0;       
            for y in range(self.n):
                sum +=  self.data[y,y,i]
            if sum == self.magic_number:
                total += 1
            
            sum = 0
            for z in range(self.n):
                sum += self.data[z,(self.n - 1)-z, i]
            if sum == self.magic_number:
                total += 1

        return total

    def calculate_space_diagonal_value(self):
        total = 0

        sum = 0
        for i in range(self.n):
            sum += self.data[i,i,i]
        if sum == self.magic_number:
            total += 1
        # print(sum)
        
        sum = 0
        for i in range(self.n):
            sum += self.data[i,(self.n - 1)-i, i]
        if sum == self.magic_number:
            total += 1
        # print(sum)

        sum = 0
        for i in range(self.n):
            sum += self.data[i, i, (self.n - 1)-i]
        if sum == self.magic_number:
            total += 1
        # print(sum)

        sum = 0
        for i in range(self.n):
            sum += self.data[i, (self.n - 1)-i, (self.n - 1)-i]
        if sum == self.magic_number:
            total += 1
        # print(sum)
        
        # print(total)
        return total


class simulated_annealing:
    def __init__(self, n):
        self.cube = Cube(n)
        self.t = 100
        self.minimum_prob = 0.9

    def main_sa(self):
        temp = self.t

        while temp > 0:
            end = self.compare_state(self.generate_random_point(), self.generate_random_point(), temp)
            if end :
                # print(self.cube.data)
                break
            temp = temp * 0.95

        # for i in range(self.t, 0, -0.2):
        #     end = self.compare_state(self.generate_random_point(), self.generate_random_point(), i)
        #     if end :
        #         # print(self.cube.data)
        #         break

    def compare_state(self,pos1,pos2, time_value):
        current_value = self.calculate_value()
        self.cube.swap(pos1,pos2)
        neighbor_value = self.calculate_value()

        print("pos1 : " , pos1 , "  pos2: ", pos2 , "time value", time_value, "  current value : " , current_value , ", neighbor value" , neighbor_value)

        if current_value > neighbor_value:
            self.cube.swap(pos1,pos2)
            chance = self.calculate_prob(current_value, neighbor_value, time_value)
            if chance > self.minimum_prob:
                self.cube.swap(pos1,pos2)
        
        return neighbor_value == 109

    def generate_random_point(self):
        generated_point = []
        for i in range(self.cube.n):
            value = random.randint(0, self.cube.n - 1)  # Generate a random value
            generated_point.append(value)
        return generated_point

    def calculate_prob(self, c_value, n_value, t_value):
        prob = 0
        delta_E = n_value - c_value
        prob = math.exp(delta_E/t_value)
        print(prob)
        return prob


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
            return total
        
        

    
random_cube = simulated_annealing(5)

random_cube.main_sa()
# random_cube.main_sa()