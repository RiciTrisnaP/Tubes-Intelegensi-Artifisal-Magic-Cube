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
        inp = int(input("Pilih Algoritma:"))  
    except ValueError:
        print("Input harus berupa angka.")
        return
    
    if inp == 1:
        print("\n\nMenjalankan Algoritma Steepest Ascent\n")
        solve_cube = HillClimbingSearchSteepestAscent() 
    elif inp == 2:
        try:
            print("\n\nMenjalankan Algoritma Sideways Move\n")
            num_max_sideways_moves = int(input("Number of maximum sideways moves: "))
            solve_cube = HillClimbingSidewaysMove(num_max_sideways_moves)
        except ValueError:
            print("Input should be a number.")
            return
    elif inp == 3:
        try:
            print("\n\nMenjalankan Algoritma Random Restart Hill Climbing\n")
            num_max_restarts = int(input("Number of maximum restarts: "))
            solve_cube = RandomRestartHillClimbing(num_max_restarts)
        except ValueError:
            print("Input should be a number.")
            return
    elif inp == 4:
        print("\n\nMenjalankan Algoritma Simulated Anealing\n")
        solve_cube = SimulatedAnnealing()
    elif inp == 5:
        try:
            print("\n\nMenjalankan Algoritma Stochastic Hill Climbing\n")
            num_iteration = int(input("Number of iteration: "))
            solve_cube = StochasticHillClimbing(num_iteration)
        except ValueError:
            print("Input should be a number.")
            return
    elif inp == 6:
        try:
            print("\n\nMenjalankan Algoritma Genetic Algorithm\n")
            num_population = int(input("Number of population: "))
            num_iteration = int(input("Number of iteration: "))
            solve_cube = GeneticAlgorithm(num_population, num_iteration)
        except ValueError:
            print("Input should be a number.")
            return
    else:
        print("Pilihan tidak valid.")
        return
    
    if inp == 6:
        vis = solve_cube.best_per_iteration
        solve_cube.solve()
    else:
        solve_cube.print_value()
        list_swap, init= solve_cube.solve()
        solve_cube.print_value()

    inp2 = input("Apakah ingin render video? (Y/T): ").strip().lower()
    while inp2 not in ["y", "t"]:
        inp2 = input("Input tidak valid. Apakah ingin render video? (Y/T): ").strip().lower()

    if (inp2 == "Y" or inp2=="y"):
        if inp == 3: #random restart
            scene = CubeWithNumbersRR(list_swap, init)
            scene.render()
        elif inp == 6: #GA
            scene = CubeGenetic(vis)
            scene.render()
        else:
            scene = CubeWithNumbers(list_swap, init)
            scene.render()


if __name__ == "__main__":
    main()