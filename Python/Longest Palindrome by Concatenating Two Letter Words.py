from typing import List


class Solution:
    ALPHABET_SIZE = 26

    def longestPalindrome(self, words: List[str]) -> int:
        count = [[0 for _ in range(self.ALPHABET_SIZE)] for _ in range(self.ALPHABET_SIZE)]

        for word in words:
            count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1

        answer = 0
        central = False

        for i in range(self.ALPHABET_SIZE):
            if count[i][i] % 2 == 0:
                answer += count[i][i]
            else:
                answer += count[i][i] - 1
                central = True

            for j in range(i + 1, self.ALPHABET_SIZE):
                answer += 2 * min(count[i][j], count[j][i])

        return 2 * (answer + central)
