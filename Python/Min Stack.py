from sys import maxsize


class MinStack:
    """
    Memory:
        creation - O(1), increases with calls 'push'
        'popSmallest' and 'addBack' - O(1)

    Time:
        creation, 'popSmallest' and 'addBack' - O(1)
    """

    def __init__(self):
        self.stack = [(maxsize, maxsize)]

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        _, minimum = self.stack[-1]
        return minimum
