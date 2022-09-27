public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int removeDuplicates(int[] nums) {
        int pos = 0;

        for (int i = 0; i < nums.length; ++i)
            if (i == 0 || nums[i - 1] != nums[i]) {
                nums[pos] = nums[i];
                pos += 1;
            }

        return pos;
    }
}
