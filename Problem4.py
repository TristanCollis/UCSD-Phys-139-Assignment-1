from MontyHall import *
from commonFuncs import *
from typing import Sequence
from sys import argv
import numpy as np


def problem4(reps: int):
    if not reps:
        return

    print("--- \n Problem 4 \n")

    nonSwitchWins = 0
    switchWins = 0
    for _ in range(reps):
        if montyHallProblem(switch=False):
            nonSwitchWins += 1

    for _ in range(reps):
        if montyHallProblem(switch=True):
            switchWins += 1

    print(f"Switch wins: {switchWins} -> {100*switchWins / reps}%")
    print(f"Non-switch wins: {nonSwitchWins} -> {100*nonSwitchWins / reps}%")


def main(reps=10**4):
    problem4(reps)


if __name__ == "__main__":
    if len(argv) > 1:
        main(*argv[1:])
    else:
        main()
