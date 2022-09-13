import java.util.Arrays;

class Solution {
    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);
        int partitions = 0;
        int start = -100000;

        for (int num : nums) {
            if (num - start > k) {
                partitions += 1;
                start = num;
            }
        }

        return partitions;
    }
}
