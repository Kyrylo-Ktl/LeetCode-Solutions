public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int countBinarySubstrings(String s) {
        int substrings = 0;
        int prev = 0, curr = 1;

        for (int i = 1; i < s.length(); ++i) {
            if (s.charAt(i - 1) != s.charAt(i)) {
                substrings += Math.min(prev, curr);
                prev = curr;
                curr = 1;
            } else {
                ++curr;
            }
        }

        return substrings + Math.min(prev, curr);
    }
}
