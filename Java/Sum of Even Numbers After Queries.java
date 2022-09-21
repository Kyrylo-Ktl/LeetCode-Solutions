class Solution {

    /**
     * Time:   O(n + m)
     * Memory: O(1)
     */
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int sum = 0;
        for (int num : nums)
            sum += (num % 2 == 0 ? num : 0);

        int[] ans = new int[queries.length];
        for (int i = 0; i < ans.length; ++i) {
            int value = queries[i][0];
            int index = queries[i][1];

            if (nums[index] % 2 == 0)
                sum -= nums[index];

            nums[index] += value;

            if (nums[index] % 2 == 0)
                sum += nums[index];

            ans[i] = sum;
        }

        return ans;
    }
}
