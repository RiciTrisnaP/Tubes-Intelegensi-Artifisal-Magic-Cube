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

    # stochastic_cube = HillClimbingSidewaysMove(5, 20)
    # stochastic_cube.solve()

    stochastic_cube = HillClimbingSearchSteepestAscent(5)
    stochastic_cube.solve()

    cube = SimulatedAnnealing(5,100)
    cube.print_value()
    cube.solve()
    cube.print_value()

    end_time = time.time() 

    duration = end_time - start_time
    print(f"Stochastic Hill Climbing Algorithm Duration: {duration:.4f} seconds")

if __name__ == "__main__":
    main()