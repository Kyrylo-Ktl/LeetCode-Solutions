class MyCircularQueue:
    """
    Memory:
        creation - O(k)
        operations - O(1)

    Time:
        creation - O(k)
        operations - O(1)
    """

    def __init__(self, k: int):
        self._queue = [0] * k
        self._size = k
        self._cnt = 0
        self._head = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._queue[(self._head + self._cnt) % self._size] = value
        self._cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._head = (self._head + 1) % self._size
        self._cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._queue[self._head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._queue[(self._head + self._cnt - 1) % self._size]

    def isEmpty(self) -> bool:
        return self._cnt == 0

    def isFull(self) -> bool:
        return self._cnt == self._size
