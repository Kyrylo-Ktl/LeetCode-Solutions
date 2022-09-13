class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def lengthOfLongestSubstring(self, string: str) -> int:
        last_index = {}
        start_ind = max_length = 0

        for ind, ch in enumerate(string):
            if ch in last_index and start_ind <= last_index[ch]:
                start_ind = last_index[ch] + 1

            last_index[ch] = ind
            max_length = max(max_length, ind - start_ind + 1)

        return max_length
