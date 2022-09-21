from typing import List


class Solution:
    """
    Time:   O(n + m)
    Memory: O(1)
    """

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if not num & 1)
        sums = []

        for val, i in queries:
            if val & 1 and nums[i] & 1:
                even_sum += nums[i] + val
            elif val & 1 and not nums[i] & 1:
                even_sum += -nums[i]
            elif not val & 1 and not nums[i] & 1:
                even_sum += val

            nums[i] += val
            sums.append(even_sum)

        return sums


class Solution:
    """
    Time:   O(n + m)
    Memory: O(1)
    """

    CHANGE = {
        ( True,  True): lambda val, diff: val + diff,
        ( True, False): lambda val, diff: 0,
        (False,  True): lambda val, diff: -val,
        (False, False): lambda val, diff: diff,
    }

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if not num & 1)
        sums = []

        for val, i in queries:
            even_sum += self.CHANGE[nums[i] & 1, val & 1](nums[i], val)
            sums.append(even_sum)
            nums[i] += val

        return sums


class Solution:
    """
    Time:   O(n + m)
    Memory: O(1)
    """

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if not num & 1)
        sums = []

        for val, i in queries:
            if not nums[i] & 1:
                even_sum -= nums[i]

            nums[i] += val

            if not nums[i] & 1:
                even_sum += nums[i]

            sums.append(even_sum)

        return sums
