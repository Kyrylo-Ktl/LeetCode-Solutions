from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def floodFill(self, image: List[List[int]], row: int, col: int, new_color: int) -> List[List[int]]:
        if image[row][col] != new_color:
            self.populate_color(image, row, col, new_color, image[row][col])
        return image

    @classmethod
    def populate_color(cls, image: List[List[int]], row: int, col: int, new_color: int, old_color: int):
        if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == old_color:
            image[row][col] = new_color
            cls.populate_color(image, row - 1, col, new_color, old_color)
            cls.populate_color(image, row + 1, col, new_color, old_color)
            cls.populate_color(image, row, col - 1, new_color, old_color)
            cls.populate_color(image, row, col + 1, new_color, old_color)
