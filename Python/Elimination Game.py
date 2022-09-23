class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)

    Explanation:
    1. Initially we start elimination from left to right:
        f(1,2,3 ... n) = f(n | left)
    2. At each step, we eliminate odd numbers and start on the other side:
        f(n | left) = f(2,4,6 ... n | right)
        f(2,4,6 ... n | right) = 2*f(1,2,3 ... n/2 | right) = 2*f(n/2 | right)
    3. Let`s transform f(n | left) as follows:
        f(1,2,3 ... n | left) = ANS
        f(n+1-1,n+1-2,n+1-3 ... n+1-n | left) = n+1-ANS
        f(n,n-1,n-2 ... 1 | left) = f(n | right) = n+1-ANS
        f(n | right) = n+1-f(1,2,3 ... n | left)
    4. Based on the previous:
        f(n | left) = f(n/2 | right) = n/2+1-f(1,2,3 ... n/2 | left)
    5. As a result, we obtain the recursive relation:
        f(n) = 2*(n/2+1-f(n/2))
    """

    def lastRemaining(self, n: int) -> int:
        n = 1
        while 2*n != n - n&1:
            n = n + 1
        return n
