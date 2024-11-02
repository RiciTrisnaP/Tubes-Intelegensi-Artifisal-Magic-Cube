from algorithm.Cube import *

class GeneticAlgorithm:
    def __init__(self, population_size, nmax, n):
        self.population_size = population_size
        self.nmax = nmax
        self.n = n
        self.population = []
        for i in range(population_size):
            self.population.append(Cube(n))
        
    def main_ga(self):
        for i in range(self.nmax):
            parent_population = []
            IsEnd, population_strip = self.generate_random_selection_probability()

            if IsEnd:
                break

            for individu in range(self.population_size):
                rand = random.uniform(0,100)
                # print (rand)
                n = 0
                for strip in population_strip:
                    if strip >= rand :
                        parent_population.append(self.population[n])
                        # print(n)
                        break
                    n += 1

            for i in range (0, self.population_size, 2):
                cx1, cx2 = self.crossover(parent_population[i], parent_population[i+1])
                parent_population[i].data = cx1.reshape(5,5,5)  
                parent_population[i+1].data = cx2.reshape(5,5,5)

            for individu in parent_population:
                temp = self.mutation(individu.data)
                temp = np.array(temp)
                individu.data = temp.reshape(5,5,5)
            
            self.population = parent_population
        
    def generate_random_selection_probability(self):
        population_value = []
        total = 0
        IsEnd = False

        for i in self.population:
            temp = i.calculate_value()
            population_value.append(temp)
            total += temp
            if temp == 105:
                IsEnd = True

        print(population_value)
        last_strip_percentage = 0
        population_strip = []
        for i in population_value:
            tmp = i/total * 100
            population_strip.append(last_strip_percentage + (tmp))
            last_strip_percentage += tmp
        print(population_strip)
        return IsEnd, population_strip

    def crossover(self, parent1, parent2):
        temp1 = parent1.data.reshape(125)
        temp2 = parent2.data.reshape(125)

        middle_index = random.randint(0, 125) 

        offspring1 = np.concatenate((temp1[:middle_index], temp2[middle_index:]))
        offspring2 = np.concatenate((temp2[:middle_index], temp1[middle_index:]))

        # Print the results
        return offspring1, offspring2

    def mutation(self, parent):
        original_array = parent.reshape(125)

        n = self.n**3

        # Buat set untuk melacak angka yang sudah ada
        existing_numbers = set()
        result_array = []

        # Tambahkan angka unik ke result_array
        for num in original_array:
            if num in existing_numbers:
                result_array.append(None)  # Tempat penampung untuk angka yang kembar
            else:
                result_array.append(num)
                existing_numbers.add(num)

        # Temukan angka yang hilang dari 1 hingga n
        missing_numbers = set(range(1, n + 1)) - existing_numbers

        # Ganti None dengan angka yang hilang
        missing_numbers = iter(sorted(missing_numbers))  # Urutkan angka yang hilang
        for i in range(len(result_array)):
            if result_array[i] is None:
                result_array[i] = next(missing_numbers)

        return result_array