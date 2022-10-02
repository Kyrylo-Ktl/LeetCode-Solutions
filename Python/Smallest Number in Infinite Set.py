from heapq import heapify, heappop, heappush


class SmallestInfiniteSet:
    """
    Memory:
        creation - O(n)
        'popSmallest' and 'addBack' - O(1)

    Time:
        creation - O(n*log(n))
        'popSmallest' and 'addBack' - O(log(n))
    """

    MAX_NUM = 1001

    def __init__(self):
        self.heap = list(range(1, self.MAX_NUM + 1))
        heapify(self.heap)
        self.nums = set(range(1, self.MAX_NUM + 1))

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heappop(self.heap)
            self.nums.remove(smallest)
            return smallest

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            heappush(self.heap, num)
            self.nums.add(num)


class SmallestInfiniteSet:
    """
    Memory:
        creation - O(1), increases with calls 'addBack'
        'popSmallest' and 'addBack' - O(1)

    Time:
        creation - O(1)
        'popSmallest' and 'addBack' - O(log(n))
    """

    def __init__(self):
        self.heap = []
        self.nums = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.heap:
            sm = heappop(self.heap)
            self.nums.remove(sm)
            return sm
        else:
            sm = self.smallest
            self.smallest += 1
            return sm

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.heap:
            heappush(self.heap, num)
            self.nums.add(num)
