class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int removeElement(int[] nums, int val) {
        int i = 0;

        for (int num : nums)
            if (num != val)
                nums[i++] = num;

        return i;
    }
}
