from dataclasses import dataclass, field
from typing import List, Dict, Set


def init_sizes():
    return {'s', 'm', 'l'}


@dataclass
class Trial:
    is_valid: bool
    numbers: List[int]
    grades: Dict[str, int]  # cheia de tipul string si valoarea de tipul int
    sizes: Set = field(default_factory=init_sizes,
                       init=False)  # acest atribut nu apare la constructor si foloseste functia init_sizes ca sa ia valoarea implicita


t = Trial(False, [1, 2, 3], {'Andrei': 7, 'Ana': 9})
print(t)