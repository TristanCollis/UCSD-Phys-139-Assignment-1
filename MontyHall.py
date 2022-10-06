import numpy as np

def montyHallProblem(switch: bool, numDoors=3) -> bool:
    rng = np.random.default_rng()
    
    doors = [True] + [False] * (numDoors - 1)
    choice = rng.integers(0, len(doors))

    if switch:
        doors = doors[:choice] + doors[choice+1:]
        doors.remove(False)
        choice = rng.integers(0, len(doors))

    return doors[choice]