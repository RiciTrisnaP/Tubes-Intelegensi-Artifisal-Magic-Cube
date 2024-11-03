import time
from algorithm.StochasticHillClimbing import *
from algorithm.GeneticAlgorithm import *
from algorithm.HillClimbingSearch import *
from algorithm.HillClimbingSearchSteepestAscent import *
from algorithm.HillClimbingSidewaysMove import *
from algorithm.RandomRestartHillClimbing import *
from algorithm.SimulatedAnnealing import *

def main():
    start_time = time.time()

    # Random Restart Hill climbing
    # cube = RandomRestartHillClimbing(5,3)
    # cube.solve()
    # cube.print_value()

    # Stochastic Hill Climbing
    # stochastic_cube = StochasticHillClimbing(5, 10000)
    # stochastic_cube.solve()

    # Hill Climbing Sideways
    # stochastic_cube = HillClimbingSidewaysMove(5, 20)
    # stochastic_cube.solve()

    # Hill Climbing Steepest Ascent
    stochastic_cube = HillClimbingSearchSteepestAscent(5)
    list_swap, init = stochastic_cube.solve()
    stochastic_cube.plot_value()

    # Simulated Annealing
    # cube = SimulatedAnnealing(5)
    # cube.solve()
    
    # Genetic Algorithm
    # cube = GeneticAlgorithm(5, 1000, 5)
    # cube.main_ga()

    # print(list_swap)
    # cube = SimulatedAnnealing(5, 2000)
    # # cube.print_value()
    # cube.solve()
    # cube.print_value()
    
    # list1 = [1,3,4,2,5,8,7,6]
    # list2 = [7,5,6,1,2,4,3,8]
    
    # start = random.randint(0,len(list1)-1)
    # last = random.randint(start+1, len(list1))
    
    # print(start, last)
    # print(list1[start:last])
    

    end_time = time.time() 

    duration = end_time - start_time
    print(f"Algorithm Duration: {duration:.4f} seconds")

if __name__ == "__main__":
    main()