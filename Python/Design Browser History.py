class BrowserHistory:
    """
    Memory:
        creation - O(1)
        operations - O(1)

    Time:
        creation - O(1)
        visit - O(1)
        back, forward - O(k)
    """

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.forw = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        self.forw = 0
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)

    def back(self, steps: int) -> str:
        for i in range(min(steps, self.curr)):
            self.curr -= 1
            self.forw += 1
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        for i in range(min(steps, self.forw)):
            self.curr += 1
            self.forw -= 1
        return self.history[self.curr]
