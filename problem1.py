import numpy as np
from dataclasses import dataclass, InitVar, field
from typing import Sequence
from random import random


@dataclass
class Coin:
    pHeads: InitVar[float]

    p: dict = field(init=False, default_factory=dict)

    def __post_init__(self, pHeads):
        self.p = {"heads": pHeads, "tails": 1 - pHeads}


def flip(coin: Coin) -> bool:
    return random() > coin.p["heads"]


def probNHeads(coins: Sequence[Coin], n: int) -> float:
    if n > len(coins):
        return 0

    if n == 0:
        return np.product([coin.p["tails"] for coin in coins])

    if len(coins) == 0:
        return 1

    return coins[0].p["heads"] * probNHeads(coins[1:], n-1) + coins[0].p["tails"] * probNHeads(coins[1:], n)