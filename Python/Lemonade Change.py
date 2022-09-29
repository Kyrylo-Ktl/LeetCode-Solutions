from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five > 0:
                ten += 1
                five -= 1
            elif bill == 20 and ten > 0 and five > 0:
                five -= 1
                ten -= 1
            elif bill == 20 and five >= 3:
                five -= 3
            else:
                return False

        return True
