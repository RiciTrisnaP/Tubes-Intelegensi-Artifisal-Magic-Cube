import time
from algorithm.StochasticHillClimbing import *
from algorithm.GeneticAlgorithm import *
from algorithm.HillClimbingSearch import *
from algorithm.HillClimbingSearchSteepestAscent import *
from algorithm.HillClimbingSidewaysMove import *
from algorithm.RandomRestartHillClimbing import *
from algorithm.SimulatedAnnealing import *
from scene import CubeWithNumbers
from sceneRandomRestart import CubeWithNumbersRR

def main():
    start_time = time.time()

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
        solve_cube = HillClimbingSearchSteepestAscent(5) #render aman
    elif inp == 2:
        print("\n\nMenjalankan Algoritma Sideways Move\n")
        solve_cube = HillClimbingSidewaysMove(5,10)
    elif inp == 3:
        print("\n\nMenjalankan Algoritma Random Restart Hill Climbing\n")
        solve_cube = RandomRestartHillClimbing(5,2) #render aman
    elif inp == 4:
        print("\n\nMenjalankan Algoritma Simulated Anealing\n")
        solve_cube = SimulatedAnnealing(5) #render aman
    elif inp == 5:
        print("\n\nMenjalankan Algoritma Stochastic Hill Climbing\n")
        solve_cube = StochasticHillClimbing(5,10000) #render aman
    elif inp == 6:
        print("\n\nMenjalankan Algoritma Genetic Algorithm\n")
        solve_cube = GeneticAlgorithm(5, 1000, 5)
    else:
        print("Pilihan tidak valid.")
        return

    if inp == 6:
        solve_cube.solve()
        end_time = time.time() 
        duration = end_time - start_time
        print(f"Algorithm Duration: {duration:.4f} seconds")
        return
    else:
        solve_cube.print_value()
        list_swap, init= solve_cube.solve()
        solve_cube.print_value()

    end_time = time.time() 
    duration = end_time - start_time
    print(f"\n\nAlgorithm Duration: {duration:.4f} seconds")


    inp2 = input("Apakah ingin render video? (Y/T): ").strip().lower()
    while inp2 not in ["y", "t"]:
        inp2 = input("Input tidak valid. Apakah ingin render video? (Y/T): ").strip().lower()

    if (inp2 == "Y" or inp2=="y"):
        if inp == 3: #random restart
            scene = CubeWithNumbersRR(list_swap, init)
            scene.render()
        else:
            scene = CubeWithNumbers(list_swap, init)
            scene.render()


if __name__ == "__main__":
    main()