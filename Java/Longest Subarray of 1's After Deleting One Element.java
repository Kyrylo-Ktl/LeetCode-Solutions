class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int longestSubarray(int[] nums) {
        int longest = 0;
        int prev = 0, curr = 0;

        for (int bit : nums) {
            if (bit == 0) {
                prev = curr;
                curr = 0;
            } else {
                longest = Math.max(longest, prev + ++curr);
            }
        }

        return longest == nums.length ? longest - 1 : longest;
    }
}
