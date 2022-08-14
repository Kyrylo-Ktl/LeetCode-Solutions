from collections import defaultdict, deque
from typing import List, Dict


class Solution:
    WILDCARD = '.'

    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        if end_word not in word_list:
            return []

        word_tree = self.get_words_tree(begin_word, end_word, word_list)
        return self.get_ladders(begin_word, end_word, word_tree)

    @staticmethod
    def get_words_tree(begin_word: str, end_word: str, word_list: List[str]) -> Dict[str, List[str]]:
        adjacency_list = defaultdict(list)

        for word in word_list:
            for i in range(len(word)):
                pattern = word[:i] + Solution.WILDCARD + word[i + 1:]
                adjacency_list[pattern].append(word)

        visited_tree = {begin_word: []}
        found = False
        queue = deque([begin_word])

        while queue and not found:
            n = len(queue)

            visited_this_level = {}

            for i in range(n):
                word = queue.popleft()

                for j in range(len(word)):
                    pattern = word[:j] + Solution.WILDCARD + word[j + 1:]

                    for next_word in adjacency_list[pattern]:
                        if next_word == end_word:
                            found = True
                        if next_word not in visited_tree:
                            if next_word not in visited_this_level:
                                visited_this_level[next_word] = [word]
                                queue.append(next_word)
                            else:
                                visited_this_level[next_word].append(word)

            visited_tree.update(visited_this_level)

        return visited_tree

    @staticmethod
    def get_ladders(begin_word: str, end_word: str, word_tree: Dict[str, List[str]]) -> List[List[str]]:
        def dfs(node: str) -> List[List[str]]:
            if node == begin_word:
                return [[begin_word]]

            if node not in word_tree:
                return []

            ladders = []
            for parent in word_tree[node]:
                ladders += dfs(parent)

            for ldr in ladders:
                ldr.append(node)

            return ladders

        return dfs(end_word)
