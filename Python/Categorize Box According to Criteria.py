class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = length >= 10_000 or width >= 10_000 or height >= 10_000 or length * width * height >= 1_000_000_000
        is_heavy = mass >= 100

        return {
            (True, True): 'Both',
            (True, False): 'Bulky',
            (False, True): 'Heavy',
            (False, False): 'Neither',
        }[(is_bulky, is_heavy)]
