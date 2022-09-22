class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int minSubArrayLen(int target, int[] nums) {
        int minLen = Integer.MAX_VALUE;
        int window_sum = 0, start = 0;

        for (int end = 0; end < nums.length; ++end) {
            window_sum += nums[end];

            while (window_sum >= target) {
                minLen = Math.min(minLen, end - start + 1);
                window_sum -= nums[start++];
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
