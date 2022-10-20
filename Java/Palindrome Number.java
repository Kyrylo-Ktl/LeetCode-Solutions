public class Solution {

    /**
     * Time:   O(log10(n))
     * Memory: O(1)
     */
    public boolean isPalindrome(int n) {
        if (n < 0 || (n % 10 == 0 && n != 0))
            return false;

        int reverted = 0;
        while (n > reverted) {
            reverted = reverted * 10 + n % 10;
            n /= 10;
        }

        return n == reverted || n == reverted / 10;
    }
}
