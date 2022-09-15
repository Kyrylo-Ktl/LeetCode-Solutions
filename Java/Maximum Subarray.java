class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public static int maxSubArray(int[] nums) {
        int maxSum = nums[0], subarrayStart = nums[0];

        for (int i = 1; i < nums.length; ++i) {
            subarrayStart = Math.max(subarrayStart + nums[i], nums[i]);
            maxSum = Math.max(maxSum, subarrayStart);
        }

        return maxSum;
    }
}
