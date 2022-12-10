from math import prod
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()

        teams = [(skill[i], skill[n - 1 - i]) for i in range(n // 2)]

        if len(set(map(sum, teams))) != 1:
            return -1

        return sum(map(prod, teams))
