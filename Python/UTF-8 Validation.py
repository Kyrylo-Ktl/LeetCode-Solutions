from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    BITS = [
        0b00000000,
        0b00000001,
        0b00000010,
        0b00000100,
        0b00001000,
        0b00010000,
        0b00100000,
        0b01000000,
        0b10000000,
    ]

    def validUtf8(self, data: List[int]) -> bool:
        trailing_bytes = 0

        for byte in data:
            if trailing_bytes < 0:
                return False
            elif trailing_bytes > 0:
                if not (byte & self.BITS[8]) or (byte & self.BITS[7]):
                    return False
                trailing_bytes -= 1
            else:
                if not (byte & self.BITS[8]):
                    continue
                elif not (byte & self.BITS[7]):
                    return False
                elif not (byte & self.BITS[6]):
                    trailing_bytes = 1
                elif not (byte & self.BITS[5]):
                    trailing_bytes = 2
                elif not (byte & self.BITS[4]):
                    trailing_bytes = 3
                else:
                    return False

        return not trailing_bytes
