class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    OPPOSITE = {'(': ')', '[': ']', '{': '}'}

    def isValid(self, string: str) -> bool:
        stack = []

        for bracket in string:
            if bracket in self.OPPOSITE:
                stack.append(bracket)
            elif not stack or bracket != self.OPPOSITE[stack[-1]]:
                return False
            else:
                stack.pop()

        return not stack
