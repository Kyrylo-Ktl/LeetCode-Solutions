public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int removePalindromeSub(String s) {
        int n = s.length();

        for (int i = 0; i < n / 2; ++i)
            if (s.charAt(i) != s.charAt(n - 1 - i))
                return 2;

        return 1;
    }
}
