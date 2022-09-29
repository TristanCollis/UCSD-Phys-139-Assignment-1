from problem1 import Coin, flip, probNHeads
import matplotlib.pyplot as plt
import numpy as np

coins = tuple(
    Coin(pHeads = p)
    for p in (0.35, 0.65, 0.60)
)

expectationVals = np.array(
    [
        probNHeads(coins, i)
        for i in range(len(coins) + 1)
    ]
)

print(f"expectation values: {expectationVals}")

frequencies = np.zeros(len(coins) + 1)
reps = 10 ** 5

for _ in range(reps):
    results = [
        flip(coin) for coin in coins
    ]
    frequencies[len(frequencies) - np.count_nonzero(results) - 1] += 1

normalizedFreqs = frequencies / reps
print(f"occurrences in {reps} reps: {frequencies}")
print(f"normalized: {normalizedFreqs}")

percentAccuracy = 100 * abs(expectationVals - normalizedFreqs) / expectationVals

print(f"percent accuracy: {percentAccuracy}")