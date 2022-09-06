from collections import defaultdict
from heapq import heappop, heappush


class FreqStack:
    """
    Implementation of a frequency stack based on a stack of stacks

    Memory:
        creation - O(n)
        'push' and 'pop' - O(1)

    Time:
        creation - O(n)
        'push' and 'pop' - O(1)
    """

    def __init__(self):
        self.frequency = defaultdict(int)
        self.stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.max_freq = max(self.frequency[val], self.max_freq)
        self.stack[self.frequency[val]].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_freq].pop()
        self.frequency[val] -= 1

        if not self.stack[self.max_freq]:
            self.max_freq -= 1

        return val


class FreqStack:
    """
    Implementation of a frequency stack based on a heap

    Memory:
        creation - O(n)
        'push' and 'pop' - O(1)

    Time:
        creation - O(n)
        'push' and 'pop' - O(log(n))
    """

    def __init__(self):
        self.frequency = defaultdict(int)
        self.heap = []
        self.index = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.index += 1
        heappush(self.heap, (-self.frequency[val], -self.index, val))

    def pop(self) -> int:
        _, _, val = heappop(self.heap)
        self.frequency[val] -= 1
        return val
