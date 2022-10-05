import numpy as np
from dataclasses import dataclass, InitVar, field
from typing import Sequence

@dataclass
class Die:
    faces: Sequence[int]
    
    proportionalDistribution: InitVar[Sequence]
    distribution: tuple = field(init=False)

    def __post_init__(self, proportionalDistribution):
        self.distribution = np.array(proportionalDistribution) / np.sum(proportionalDistribution)


def roll(die: Die) -> int:
    return np.random.default_rng().choice(die.faces, p=die.distribution)