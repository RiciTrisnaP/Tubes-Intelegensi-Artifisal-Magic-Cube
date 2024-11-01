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

    # stochastic_cube = StochasticHillClimbing(5, 10000)
    # stochastic_cube.solve()

    stochastic_cube = SimulatedAnnealing(5, 10000)
    stochastic_cube.solve()

    end_time = time.time() 

    duration = end_time - start_time
    print(f"Stochastic Hill Climbing Algorithm Duration: {duration:.4f} seconds")

if __name__ == "__main__":
    main()