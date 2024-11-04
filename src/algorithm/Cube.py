import numpy as np
import random

class Cube:
    def __init__(self, n):
        self.n = n
        self.magic_number = (self.n ** 3 + 1) / 2 * n
        self.data = self.generate_random_config(n)

    def generate_random_config(self, n):
        unique_numbers = random.sample(range(1, (n ** 3) + 1), n ** 3)
        data = np.array(unique_numbers).reshape((n, n, n))
        return data

    def swap(self, pos1, pos2):
        temp = self.data[pos1[0], pos1[1], pos1[2]]
        self.data[pos1[0], pos1[1], pos1[2]] = self.data[pos2[0], pos2[1], pos2[2]]
        self.data[pos2[0], pos2[1], pos2[2]] = temp
    
    def calculate_value(self):
        return (self.calculate_column_value() +
                self.calculate_row_value() +
                self.calculate_height_value() +
                self.calculate_side_diagonal_value() +
                self.calculate_space_diagonal_value())

    def calculate_column_value(self):
        total = 0
        for i in range(self.n):
            for y in range(self.n):
                if np.sum(self.data[i, y, :]) == self.magic_number:
                    total += 1
        return total

    def calculate_row_value(self):
        total = 0
        for i in range(self.n):
            for z in range(self.n):
                if np.sum(self.data[i, :, z]) == self.magic_number:
                    total += 1
        return total

    def calculate_height_value(self):
        total = 0
        for y in range(self.n):
            for z in range(self.n):
                if np.sum(self.data[:, y, z]) == self.magic_number:
                    total += 1
        return total

    def calculate_side_diagonal_value(self):
        total = 0
        for z in range(self.n):
            if np.sum(self.data[z, np.arange(self.n), np.arange(self.n)]) == self.magic_number:  
                total += 1
            if np.sum(self.data[z, np.arange(self.n), np.arange(self.n - 1, -1, -1)]) == self.magic_number:  
                total += 1

        for y in range(self.n):
            if np.sum(self.data[np.arange(self.n), y, np.arange(self.n)]) == self.magic_number:  
                total += 1
            if np.sum(self.data[np.arange(self.n), y, np.arange(self.n - 1, -1, -1)]) == self.magic_number:  
                total += 1
        
        for i in range(self.n):
            if np.sum(self.data[np.arange(self.n), np.arange(self.n), i]) == self.magic_number:  
                total += 1
            if np.sum(self.data[np.arange(self.n - 1, -1, -1), np.arange(self.n), i]) == self.magic_number:  
                total += 1

        return total

    def calculate_space_diagonal_value(self):
        total = 0
        diagonals = [
            np.sum(self.data[np.arange(self.n), np.arange(self.n), np.arange(self.n)]),
            np.sum(self.data[np.arange(self.n), np.arange(self.n - 1, -1, -1), np.arange(self.n)]),
            np.sum(self.data[np.arange(self.n), np.arange(self.n), np.arange(self.n - 1, -1, -1)]),
            np.sum(self.data[np.arange(self.n), np.arange(self.n - 1, -1, -1), np.arange(self.n - 1, -1, -1)])
        ]
        total += sum(1 for x in diagonals if x == self.magic_number)
        return total

    def generate_random_point(self):
        return [random.randint(0, self.n - 1) for _ in range(3)]
    
    def print_value(self):
        counter = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    print(self.data[i, j, k], end=" ")
                    counter += 1
                    if counter % 25 == 0:
                        print() 
        print()
    
    
    def plot_number_cube(self, ax, cube_data, title):
        spacing = 1
        colors = ['red', 'blue', 'green', 'purple', 'orange']
         
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    x_center = i * spacing + spacing / 2
                    y_center = j * spacing + spacing / 2
                    z_center = k * spacing + spacing / 2
                    
                    color = colors[k % len(colors)]

                    # Plot the number in the center
                    ax.text(x_center, y_center, z_center, str(cube_data[i, j, k]),
                            ha='center', va='center',  color=color, fontsize=10)

        ax.set_xlim([0, self.n])
        ax.set_ylim([0, self.n])
        ax.set_zlim([0, self.n])

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        ax.set_title(title)