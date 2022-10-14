from Dice import *
from commonFuncs import *
from typing import Sequence
from sys import argv
import numpy as np


def problem3(target: int, dieFaces: Sequence, reps: int):
    if not reps:
        return

    print("--- \n Problem 3 \n")

    wins = 0
    dice = tuple(
        Die(faces=dieFaces, proportionalDistribution=(1, 1, 1, 1, 1, 1, 1))
        for _ in range(2))
    
    for _ in range(reps):
        if np.sum([roll(die) for die in dice]) == target:
            wins += 1

    winFrequency = wins / reps

    print(f"Wins: {wins}")
    print(f"Win probability: {winFrequency}")
    print(f"Win Percentage: {100 * winFrequency}%")


def main(target=8, dieFaces=(1, 2, 3, 4, 7, 8, 9), reps=10**4):
    problem3(target, dieFaces, reps)


if __name__ == "__main__":
    if len(argv) > 1:
        main(*argv[1:])
    else:
        main()
