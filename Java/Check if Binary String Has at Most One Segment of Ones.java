public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean checkOnesSegment(String s) {
        return !s.contains("01");
    }
}
