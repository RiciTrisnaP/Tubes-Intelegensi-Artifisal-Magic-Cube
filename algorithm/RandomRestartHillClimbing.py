from algorithm.Cube import *
from algorithm.HillClimbingSearch import *
import random

class RandomRestartHillClimbing:
    def __init__(self, n, max_restarts, max_iterations_per_restart):
        self.n = n
        self.max_restarts = max_restarts
        self.max_iterations_per_restart = max_iterations_per_restart

    def solve(self):
        return