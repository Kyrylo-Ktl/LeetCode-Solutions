class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        return self.digitSum(self.round(s, k), k)

    @classmethod
    def round(cls, s: str, k: int) -> str:
        return ''.join(map(cls.add_digits, cls.slice(s, k)))

    @staticmethod
    def add_digits(s: str) -> str:
        return str(sum(int(d) for d in s))

    @staticmethod
    def slice(s: str, k: int):
        for i in range(0, len(s), k):
            yield s[i:i + k]


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = self.digitSum(self.round(s, k), k)
        return s

    @classmethod
    def round(cls, s: str, k: int) -> str:
        return ''.join(map(cls.add_digits, cls.slice(s, k)))

    @staticmethod
    def add_digits(s: str) -> str:
        return str(sum(int(d) for d in s))

    @staticmethod
    def slice(s: str, k: int):
        for i in range(0, len(s), k):
            yield s[i:i + k]
