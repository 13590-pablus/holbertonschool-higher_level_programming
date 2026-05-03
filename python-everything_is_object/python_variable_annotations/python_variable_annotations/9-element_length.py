#!/usr/bin/env python3
"""Let's annotate a function's parameters"""
from typing import Iterable, Sequence, List, Tuple
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
