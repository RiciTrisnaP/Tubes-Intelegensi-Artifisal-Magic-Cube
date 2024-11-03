import numpy as np
import random
from algorithm.Cube import Cube

class GeneticAlgorithm:
    def __init__(self, population_size, nmax, n, elite_count=1, crossover_rate=0.8, mutation_rate=0.1):
        self.population_size = population_size
        self.nmax = nmax
        self.n = n
        self.elite_count = elite_count
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = [Cube(n) for _ in range(population_size)]
        
    def main_ga(self):
        for gen in range(self.nmax):
            parent_population = []
            IsEnd, population_strip = self.generate_random_selection_probability()

            if IsEnd:
                break

            sorted_population = sorted(self.population, key=lambda x: x.calculate_value(), reverse=True)
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

        
    def generate_random_selection_probability(self):
        population_value = [cube.calculate_value() for cube in self.population]
        total = sum(population_value)
        IsEnd = any(value == 109 for value in population_value)

        print(population_value)

        if total == 0:
            population_strip = [100 * (i + 1) / self.population_size for i in range(self.population_size)]
        else:
            population_strip = np.cumsum([val / total * 100 for val in population_value]).tolist()

        # print(population_strip)
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
        temp1 = np.array(parent1.data).reshape(125)
        temp2 = np.array(parent2.data).reshape(125)
        crossover_point = random.randint(1, 124)

        offspring1 = np.concatenate((temp1[:crossover_point], temp2[crossover_point:]))
        offspring2 = np.concatenate((temp2[:crossover_point], temp1[crossover_point:]))

        return offspring1, offspring2

    def mutation(self, individual):
        mutated = individual.flatten()
        n = self.n**3

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
