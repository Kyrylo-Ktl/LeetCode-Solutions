class CustomStack:
    def __init__(self, maxsize: int):
        self.stack = []
        self.maxsize = maxsize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxsize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return - 1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
