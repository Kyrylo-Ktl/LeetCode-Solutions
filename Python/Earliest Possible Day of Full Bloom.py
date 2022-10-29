from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def earliestFullBloom(self, plant_time: List[int], grow_time: List[int]) -> int:
        result = curr_plant_time = 0

        for i in sorted(range(len(plant_time)), key=lambda x: -grow_time[x]):
            curr_plant_time += plant_time[i]
            result = max(result, curr_plant_time + grow_time[i])

        return result
