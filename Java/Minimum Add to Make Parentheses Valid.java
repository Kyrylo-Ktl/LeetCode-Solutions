public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int minAddToMakeValid(String s) {
        int add = 0, score = 0;

        for (int i = 0; i < s.length(); ++i) {
            score += s.charAt(i) == '(' ? 1 : -1;
            if (score == -1) {
                ++add;
                ++score;
            }
        }

        return add + score;
    }
}
