public class Solution {

    /**
     * Time:   O(n*log(m))
     * Memory: O(1)
     * where m - range of values, i.e. maximum - minimum
     */
    public long minCost(int[] nums, int[] cost) {
        long left = Long.MAX_VALUE, right = Long.MIN_VALUE;

        for (int num : nums) {
            left = Math.min(left, num);
            right = Math.max(right, num);
        }

        long minCost = getCost(nums, cost, left);

        while (left < right) {
            long mid = (left + right) / 2;
            long a = getCost(nums, cost, mid), b = getCost(nums, cost, mid + 1);
            minCost = Math.min(a, b);

            if (a < b)
                right = mid;
            else
                left = mid + 1;
        }

        return minCost;
    }

    private static long getCost(int[] nums, int[] cost, long num) {
        long changeCost = 0;

        for (int i = 0; i < nums.length; ++i)
            changeCost += Math.abs(nums[i] - num) * cost[i];

        return changeCost;
    }
}
