import numpy as np
import matplotlib.pyplot as plt
import random
from algorithm.Cube import Cube
import time

class GeneticAlgorithm:
    def __init__(self, population_size, nmax, n = 5, elite_count=1, crossover_rate=0.8, mutation_rate=0.1):
        self.population_size = population_size
        self.nmax = nmax
        self.n = n
        self.elite_count = elite_count
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = [Cube(n) for _ in range(population_size)]
        self.max_values = []
        self.mean_values = []
        self.iteration = 0
        self.best_per_iteration = []
        self.two_best_initial = []
        self.two_best_last = []
        self.best_value = 0
        
    def solve(self):
        sorted_population = sorted(self.population, key=lambda x: x.calculate_value(), reverse=True)
        self.two_best_initial.append(sorted_population[0].data.copy())
        self.two_best_initial.append(sorted_population[1].data.copy())
        
        start_time = time.time()
        for gen in range(self.nmax):
            self.iteration += 1
            parent_population = []
            IsEnd, population_strip = self.generate_random_selection_probability()

            if IsEnd:
                break

            sorted_population = sorted(self.population, key=lambda x: x.calculate_value(), reverse=True)
            self.best_per_iteration.append(sorted_population[0].data.copy())
            new_population = sorted_population[:self.elite_count]

            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents(population_strip)
                
                if random.random() < self.crossover_rate:
                    offspring1, offspring2 = self.crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1.data.copy(), parent2.data.copy()

                if random.random() < self.mutation_rate:
                    offspring1 = self.mutation(offspring1)
                if random.random() < self.mutation_rate:
                    offspring2 = self.mutation(offspring2)

                new_population.append(Cube(self.n))
                new_population[-1].data = offspring1.reshape(5, 5, 5) 
                
                if len(new_population) < self.population_size:
                    new_population.append(Cube(self.n)) 
                    new_population[-1].data = offspring2.reshape(5, 5, 5)

            self.population = new_population
            
        print("\nRESULT")
        end_time = time.time() 
        duration = end_time - start_time
        print(f"Genetic Algorithm Duration: {duration:.4f} seconds")

        self.two_best_last.append(sorted_population[0].data.copy())
        self.two_best_last.append(sorted_population[1].data.copy())

        print("Best value: ", self.best_value)
        print("Number of population: ", self.population_size)
        print("Number of iterations: ", self.iteration)
        
        self.plot_value()
        
    def generate_random_selection_probability(self):
        population_value = [cube.calculate_value() for cube in self.population]

        self.max_values.append(max(population_value))
        self.mean_values.append(np.mean(population_value))

        total = sum(population_value)
        IsEnd = any(value == 109 for value in population_value)

        self.best_value = max(population_value)

        if total == 0:
            population_strip = [100 * (i + 1) / self.population_size for i in range(self.population_size)]
        else:
            population_strip = np.cumsum([val / total * 100 for val in population_value]).tolist()

        return IsEnd, population_strip

    def select_parents(self, population_strip):
        parent1 = self.roulette_selection(population_strip)
        parent2 = self.roulette_selection(population_strip)
        return parent1, parent2

    def roulette_selection(self, population_strip):
        rand = random.uniform(0, 100)
        for idx, strip in enumerate(population_strip):
            if rand <= strip:
                return self.population[idx]
        return self.population[-1]

    def crossover(self, parent1, parent2):
        # Flatten parent data arrays
        temp1 = np.array(parent1.data).reshape(125)
        temp2 = np.array(parent2.data).reshape(125)
        
        start, end = sorted(random.sample(range(125), 2))
        
        offspring1 = [None] * 125
        offspring2 = [None] * 125
        
        offspring1[start:end] = temp1[start:end]
        offspring2[start:end] = temp2[start:end]
        
        def fill_offspring(offspring, parent_data, start, end):
            current_pos = end
            for val in parent_data:
                if val not in offspring:
                    if current_pos >= 125:
                        current_pos = 0
                    while start <= current_pos < end:
                        current_pos += 1
                    offspring[current_pos] = val
                    current_pos += 1
            return offspring

        offspring1 = fill_offspring(offspring1, temp2, start, end)
        offspring2 = fill_offspring(offspring2, temp1, start, end)

        offspring1 = np.array(offspring1).reshape(5, 5, 5)
        offspring2 = np.array(offspring2).reshape(5, 5, 5)

        return offspring1, offspring2


    def mutation(self, individual):
        mutated = individual.flatten()

        for idx in range(len(mutated)):
            if random.random() < 0.05:
                swap_idx = random.randint(0, len(mutated) - 1)
                mutated[idx], mutated[swap_idx] = mutated[swap_idx], mutated[idx]

        return np.array(mutated).reshape(5, 5, 5)

    def ordered_crossover(self, parent1, parent2):
        child = [None] * len(parent1)
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child[start:end] = parent1[start:end]

        current_pos = end
        for elem in parent2:
            if elem not in child:
                if current_pos >= len(parent1):
                    current_pos = 0
                child[current_pos] = elem
                current_pos += 1

        return np.array(child)

    def plot_value(self):
        # Cube plot
        fig1 = plt.figure(figsize=(12, 6))
        
        grid = fig1.add_gridspec(2,2,height_ratios = [1,1])
        ax1 = fig1.add_subplot(grid[0,0], projection='3d') 
        self.population[0].plot_number_cube(ax1, self.two_best_initial[0], "Initial Cube 1")
        ax2 = fig1.add_subplot(grid[0,1], projection='3d')
        self.population[0].plot_number_cube(ax2, self.two_best_initial[1], "Initial Cube 2")
        ax3 = fig1.add_subplot(grid[1,0], projection='3d')
        self.population[0].plot_number_cube(ax3, self.two_best_last[0], "Final Cube 1")
        ax4 = fig1.add_subplot(grid[1,1], projection='3d')
        self.population[0].plot_number_cube(ax4, self.two_best_last[1], "Final Cube 1")
        
        ax1.view_init(elev=30, azim=30)
        ax2.view_init(elev=30, azim=30)
        ax3.view_init(elev=30, azim=30)
        ax4.view_init(elev=30, azim=30)
        
        plt.tight_layout() 
        
        plt.figure(figsize=(12, 6))
        
        plt.plot(self.mean_values, linestyle='-', color='r', label='Mean Value', linewidth = 0.5)

        plt.plot(self.max_values, linestyle='-', color='b', label='Max Value')
        
        plt.title("Max and Mean Cube Values Over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Cube Value")
        plt.grid()
        
        plt.legend()
        
        plt.tight_layout()
        plt.show()
