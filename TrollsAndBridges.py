import numpy as np
from dataclasses import dataclass, InitVar, field
from typing import List

@dataclass
class Bridge:
    _trolls: InitVar[int]
    _gnomes: InitVar[int]

    contents: List[int] = field(init=False)

    def __post_init__(self, trolls, gnomes):
        self.contents = ['t'] * trolls + ['g'] * gnomes

    
    @property
    def trolls(self) -> int:
        return self.contents.count('t')

    
    @property
    def gnomes(self) -> int:
        return self.contents.count('g')