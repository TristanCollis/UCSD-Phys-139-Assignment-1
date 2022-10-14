from Coins import *
from commonFuncs import *
from sys import argv
import numpy as np


def problem2(probability: float, precision: int, reps: int):
    if not reps:
        return

    print("--- \n Problem 2 \n")

    outcomeCounts = np.zeros(2)

    for _ in range(reps):
        if probFromFairCoin(probability, precision):
            outcomeCounts[1] += 1
        else:
            outcomeCounts[0] += 1

    outcomeFreqs = outcomeCounts / reps

    print(f"Reults: {outcomeCounts}")
    print(f"Normalized: {outcomeFreqs}")


def main(probability=1 / 3, precision=4, reps=10**4):
    problem2(probability, precision, reps)


if __name__ == "__main__":
    if len(argv) > 1:
        main(*argv[1:])
    else:
        main()
