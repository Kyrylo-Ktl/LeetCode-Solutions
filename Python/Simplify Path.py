class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    SEP = '/'
    CURRENT_DIR = '.'
    PARENT_DIR = '..'

    def simplifyPath(self, path: str) -> str:
        simplified = []

        for directory in path.split(self.SEP):
            if not directory or directory == self.CURRENT_DIR:
                continue

            if directory == self.PARENT_DIR:
                if simplified:
                    simplified.pop()
            else:
                simplified.append(directory)

        return self.SEP + self.SEP.join(simplified)
