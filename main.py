from Coins import *
from Dice import *
from MontyHall import *
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


def problem3(target: int, reps: int):
    if not reps:
        return

    print("--- \n Problem 3 \n")

    wins = 0
    dice = tuple(
        Die(faces=(1, 2, 3, 4, 7, 8, 9),
            proportionalDistribution=(1, 1, 1, 1, 1, 1, 1)) for _ in range(2))
    for _ in range(reps):
        if np.sum([roll(die) for die in dice]) == target:
            wins += 1

    winFrequency = wins / reps

    print(f"Wins: {wins}")
    print(f"Win probability: {winFrequency}")
    print(f"Win Percentage: {100 * winFrequency}%")


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


def percentError(expectation, outcome):
    return 100 * abs(expectation - outcome) / expectation


def main(p1Reps=0, p2Reps=0, p3Reps=0, p4Reps=0):
    problem1(coinProbabilities=(0.35, 0.65, 0.60), reps=p1Reps)

    problem2(probability=1 / 3, precision=4, reps=p2Reps)

    problem3(target=8, reps=p3Reps)

    problem4(reps=p4Reps)


if __name__ == "__main__":
    main(
        p1Reps=10**3,
        p2Reps=10**3,
        p3Reps=10**3,
        p4Reps=10**3,
    )
