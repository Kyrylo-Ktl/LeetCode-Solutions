from collections import defaultdict, deque
from typing import Dict, List, Set


class Solution:
    ANY_CHARACTER = '*'

    def ladderLength(self, begin_word: str, end_word: str, words: List[str]) -> int:
        graph = self.construct_graph(set(words) | {begin_word})
        visited = {begin_word}
        queue = deque([(begin_word, 0)])

        while queue:
            word, length = queue.popleft()
            length += 1

            if word == end_word:
                return length

            for i in range(len(word)):
                for neighbour in graph[self.get_masked(word, i)]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, length))

        return 0

    @classmethod
    def construct_graph(cls, words: Set[str]) -> Dict:
        graph = defaultdict(set)
        for word in words:
            for i in range(len(word)):
                graph[cls.get_masked(word, i)].add(word)
        return graph

    @staticmethod
    def get_masked(word: str, ind: int) -> str:
        return word[:ind] + Solution.ANY_CHARACTER + word[ind + 1:]
