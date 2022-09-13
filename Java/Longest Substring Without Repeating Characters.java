class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int lengthOfLongestSubstring(String s) {
        int[] nextIndex = new int[128];
        int longest = 0, left = 0;

        for (int right = 0; right < s.length(); right++) {
            left = Math.max(nextIndex[s.charAt(right)], left);
            longest = Math.max(longest, right - left + 1);
            nextIndex[s.charAt(right)] = right + 1;
        }

        return longest;
    }
}
