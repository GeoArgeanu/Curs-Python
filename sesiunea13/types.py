from dataclasses import dataclass, field
from typing import List, Dict, Set
def init_sizes():
    return {'s', 'm', 'l'}
@dataclass

class Trial:
    is_valid: bool
    numbers: List[int]
    grades: Dict[str, int]  # cheia de tipul str si val de int
    sizes: Set= field(default_factory=init_sizes, init=False)  # acest atribut nu apare la constructor si foloseste fct init_sizes ca si val implicita

t = Trial(False, [1, 2, 3], {'Andrei':7, 'Ana':9})