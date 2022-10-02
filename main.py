from Coin import *
import matplotlib.pyplot as plt
import numpy as np


def problem1(coinProbabilities: tuple):
    coins = tuple(Coin(pHeads=p) for p in coinProbabilities)

    expectationVals = np.array(
        [probNHeads(coins, i) for i in range(len(coins) + 1)])

    print(f"expectation values: {expectationVals}")

    outcomeFrequencies = np.zeros(len(coins) + 1)
    reps = 10**5

    for _ in range(reps):
        results = [flip(coin) for coin in coins]
        outcomeFrequencies[len(outcomeFrequencies) - np.count_nonzero(results) - 1] += 1

    normalizedFrequencies = outcomeFrequencies / reps
    print(f"occurrences in {reps} reps: {outcomeFrequencies}")
    print(f"normalized: {normalizedFrequencies}")

    print(f"percent error: {percentError(expectationVals, normalizedFrequencies)}")


def problem2(probability, precision):
    outcomeCounts = np.zeros(2)
    reps = 10**4

    for _ in range(reps):
        if probFromFairCoin(probability, precision):
            outcomeCounts[1] += 1
        else:
            outcomeCounts[0] += 1

    outcomeFreqs = outcomeCounts / reps

    print(f"Reults: {outcomeCounts}")
    print(f"Normalized: {outcomeFreqs}")


def percentError(expectation, outcome):
    return 100 * abs(expectation - outcome) / expectation


def main(runProblem1=True, runProblem2=True):
    if runProblem1:
        problem1((0.35, 0.65, 0.60))

    if runProblem2:
        problem2(1/3, 4)


if __name__ == "__main__":
    main(False, True)
