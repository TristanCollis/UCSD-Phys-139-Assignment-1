from Coins import *
from commonFuncs import *
from sys import argv
import numpy as np


def problem1(coinProbabilities: tuple, reps: int):
    if not reps:
        return

    print("--- \n Problem 1 \n")

    coins = tuple(Coin(pHeads=p) for p in coinProbabilities)

    expectationVals = np.array(
        [probNHeads(coins, i) for i in range(len(coins) + 1)])

    print(f"expectation values: {expectationVals}")

    outcomeCounts = np.zeros(len(coins) + 1)

    for _ in range(reps):
        results = [flip(coin) for coin in coins]
        outcomeCounts[len(outcomeCounts) - np.count_nonzero(results) - 1] += 1

    outcomeFrequencies = outcomeCounts / reps
    print(f"occurrences in {reps} reps: {outcomeCounts}")
    print(f"normalized: {outcomeFrequencies}")

    print(
        f"percent error: {percentError(expectationVals, outcomeFrequencies)}")


def main(coinProbabilities=(0.35, 0.65, 0.60), reps=10**5):
    problem1(coinProbabilities, reps)


if __name__ == "__main__":
    if len(argv) > 1:
        main(*argv[1:])
    else:
        main()
