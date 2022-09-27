from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        walker = runner = 0

        while runner < n:
            # Write the current character to a new position
            chars[walker] = chars[runner]

            count = 1
            # Count the number of repetitions of the current character
            while runner < n - 1 and chars[runner] == chars[runner + 1]:
                runner += 1
                count += 1

            # If the current character is repeated more than once
            if count > 1:
                for d in str(count):
                    walker += 1
                    chars[walker] = d

            runner += 1
            walker += 1

        return walker
