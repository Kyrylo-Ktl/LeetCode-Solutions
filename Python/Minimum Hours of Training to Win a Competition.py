from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minNumberOfHours(self, energy: int, experience: int, energies: List[int], experiences: List[int]) -> int:
        hours = 0

        for eng, exp in zip(energies, experiences):
            # Adding the missing amount of energy
            extra_en = max(0, eng - energy + 1)
            energy += extra_en

            # Adding the missing amount of experience
            extra_ex = max(0, exp - experience + 1)
            experience += extra_ex

            energy -= eng
            experience += exp
            hours += extra_en + extra_ex

        return hours
