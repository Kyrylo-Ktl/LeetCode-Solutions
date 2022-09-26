from random import randint
from string import ascii_lowercase
from typing import Iterable, List


class DSU:
    """
    Disjoint set system with rank and path compression heuristics

    Memory:
        creation - O(n)
        'find' - O(log(n))
        'union' - O(log(n))

    Time:
        creation - O(n)
        'find' - O(log(n))
        'union' - O(log(n))

    On average, operations 'find' and 'union' take O(1) time and space
    """

    def __init__(self, nodes: Iterable):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 1 for n in nodes}

    def find(self, a: int) -> int:
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return

        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        elif self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = b_root
        else:
            if randint(0, 1) & 1:
                a_root, b_root = b_root, a_root
            self.parent[b_root] = a_root
            self.rank[a_root] += 1


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    EQUAL = '='
    NOT_EQUAL = '!'

    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU(ascii_lowercase)

        for eq in equations:
            i, sign, _, j = list(eq)
            if sign == self.EQUAL:
                dsu.union(i, j)

        for eq in equations:
            i, sign, _, j = list(eq)
            if sign == self.NOT_EQUAL and dsu.find(i) == dsu.find(j):
                return False

        return True
