from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        justified_lines = []
        width = 0
        line = []

        for word in words:
            if len(word) + width + len(line) <= max_width:
                width += len(word)
                line.append(word)
                continue

            if len(line) == 1:
                justified_lines.append(line.pop().ljust(max_width))
            else:
                justified_lines.append(self.format_line(line, width, max_width))

            line = [word]
            width = len(word)

        justified_lines.append(' '.join(line).ljust(max_width))
        return justified_lines

    @staticmethod
    def format_line(line: List[str], width: int, max_width: int) -> str:
        space, extra = divmod(max_width - width, len(line) - 1)

        for i in range(extra):
            line[i] += ' '

        return (' ' * space).join(line)
