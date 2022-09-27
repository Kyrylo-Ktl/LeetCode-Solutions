from bisect import bisect
from itertools import accumulate
from random import randint, random
from typing import List


class Solution:
    """
    Memory:
        creation - O(n)
        pick - O(1)

    Time:
        creation - O(n)
        pick - O(log(n))
    """

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        w = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in self.rects]
        self.weights = [i / sum(w) for i in accumulate(w)]

    def pick(self) -> List[int]:
        i = bisect(self.weights, random())
        x1, y1, x2, y2 = self.rects[i]
        return [randint(x1, x2), randint(y1, y2)]
