from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    FIZZ = 3
    BUZZ = 5

    def fizzBuzz(self, n: int) -> List[str]:
        nums = [str(num) for num in range(1, n + 1)]

        for fizz in range(self.FIZZ - 1, n, self.FIZZ):
            nums[fizz] = 'Fizz'

        for buzz in range(self.BUZZ - 1, n, self.BUZZ):
            nums[buzz] = 'Buzz'

        for fizzbuzz in range(self.FIZZ * self.BUZZ - 1, n, self.FIZZ * self.BUZZ):
            nums[fizzbuzz] = 'FizzBuzz'

        return nums


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    FIZZ = 3
    BUZZ = 5

    def fizzBuzz(self, n: int) -> List[str]:
        nums = []

        for num in range(1, n + 1):
            if not num % (self.FIZZ * self.BUZZ):
                nums.append('FizzBuzz')
            elif not num % self.FIZZ:
                nums.append('Fizz')
            elif not num % self.BUZZ:
                nums.append('Buzz')
            else:
                nums.append(str(num))

        return nums
