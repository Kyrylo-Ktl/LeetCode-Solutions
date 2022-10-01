class LUPrefix:
    """
    Memory: O(n)
    Time:   O(1) per upload call, because adding to the set takes O(1) time, and the prefix
                 can be increased no more than n times for all n calls to the upload function
    """

    def __init__(self, n: int):
        self._longest = 0
        self._nums = set()

    def upload(self, video: int) -> None:
        self._nums.add(video)
        # Since the prefix cannot decrease, it is enough for us to increase it
        # until we reach the number that has not yet been added
        while self._longest + 1 in self._nums:
            self._longest += 1

    def longest(self) -> int:
        return self._longest
