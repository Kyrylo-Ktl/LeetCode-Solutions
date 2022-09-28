public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int longestNiceSubarray(int[] nums) {
        int longest = 0, used_bits = 0, j = 0;

        for (int i = 0; i < nums.length; ++i) {
            while ((used_bits & nums[i]) != 0)
                used_bits ^= nums[j++];

            used_bits |= nums[i];
            longest = Math.max(longest, i - j + 1);
        }

        return longest;
    }
}
