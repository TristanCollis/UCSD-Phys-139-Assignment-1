from TrollsAndBridges import *
from commonFuncs import *
from typing import Sequence
from sys import argv
from copy import copy
import numpy as np


def problem5(reps: int):
    if not reps:
        return

    print("--- \n Problem 5 \n")

    rng = np.random.default_rng()

    wins = 0

    bridges = (
            Bridge(_trolls=2, _gnomes=3),
            Bridge(_trolls=1, _gnomes=4),
            Bridge(_trolls=3, _gnomes=2),
            Bridge(_trolls=0, _gnomes=5)
        )

    bridgeFreqs = (
        0.1,
        0.3,
        0.1,
        0.5
    )
    
    for _ in range(reps):
        bridge = copy(
            rng.choice(
            bridges, p=bridgeFreqs
            )
        )
        
        np.delete(
            bridge.contents,
            rng.integers(0, len(bridge.contents))
        )

        if bridge.trolls == 0:
            wins += 1

    print(f"The knight survived {wins} times.")
    print(f"Probability of survival: {wins / reps}")
    print(f"Percent probability of survival: {100 * wins / reps}%")


def main(reps=10**4):
    problem5(reps)


if __name__ == "__main__":
    if len(argv) > 1:
        main(*argv[1:])
    else:
        main()
