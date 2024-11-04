from algorithm.StochasticHillClimbing import *
from algorithm.GeneticAlgorithm import *
from algorithm.HillClimbingSearch import *
from algorithm.HillClimbingSearchSteepestAscent import *
from algorithm.HillClimbingSidewaysMove import *
from algorithm.RandomRestartHillClimbing import *
from algorithm.SimulatedAnnealing import *
from scene import CubeWithNumbers
from sceneRandomRestart import CubeWithNumbersRR
from sceneGenetic import CubeGenetic


def main():
    print("""1. Steepest Ascent
2. Sideways Move
3. Random Restart Hill Climbing
4. Simulated Anealing
5. Stochastic Hill Climbing
6. Genetic Algorithm""")  

    try:
        inp = int(input("Choose Algorithm:"))  
    except ValueError:
        print("Input must be a number.")
        return
    
    if inp == 1:
        print("\nRunning Steepest Ascent Algorithm\n")
        solve_cube = HillClimbingSearchSteepestAscent() 
    elif inp == 2:
        try:
            print("\nRunning Sideways Move Algorithm\n")
            num_max_sideways_moves = int(input("Number of maximum sideways moves: "))
            solve_cube = HillClimbingSidewaysMove(num_max_sideways_moves)
        except ValueError:
            print("Input must be a number.")
            return
    elif inp == 3:
        try:
            print("\nRunning Random Restart Hill Climbing Algorithm\n")
            num_max_restarts = int(input("Number of maximum restarts: "))
            solve_cube = RandomRestartHillClimbing(num_max_restarts)
        except ValueError:
            print("Input must be a number.")
            return
    elif inp == 4:
        print("\nRunning Simulated Anealing Algorithm\n")
        solve_cube = SimulatedAnnealing()
    elif inp == 5:
        try:
            print("\nRunning Stochastic Hill Climbing Algorithm\n")
            num_iteration = int(input("Number of iteration: "))
            solve_cube = StochasticHillClimbing(num_iteration)
        except ValueError:
            print("Input must be a number.")
            return
    elif inp == 6:
        try:
            print("\nRunning Genetic Algorithm\n")
            num_population = int(input("Number of population: "))
            num_iteration = int(input("Number of iteration: "))
            solve_cube = GeneticAlgorithm(num_population, num_iteration)
        except ValueError:
            print("Input must be a number.")
            return
    else:
        print("Invalid choice")
        return
    
    if inp == 6:
        vis = solve_cube.best_per_iteration
        solve_cube.solve()
    else:
        print("Initial State:")
        solve_cube.print_value()
        list_swap, init= solve_cube.solve()
        print("Last State:")
        solve_cube.print_value()

    inp2 = input("Do you want to render the video? (Y/T): ").strip().lower()
    while inp2 not in ["y", "t"]:
        inp2 = input("Invalid choice. Do you want to render the video? (Y/T): ").strip().lower()

    if (inp2 == "Y" or inp2=="y"):
        if inp == 3:
            scene = CubeWithNumbersRR(list_swap, init)
            scene.render()
        elif inp == 6:
            scene = CubeGenetic(vis)
            scene.render()
        else:
            scene = CubeWithNumbers(list_swap, init)
            scene.render()


if __name__ == "__main__":
    main()