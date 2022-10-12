public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean kLengthApart(int[] nums, int k) {
        int count = k;

        for (int bit : nums) {
            if (bit == 1) {
                if (count < k)
                    return false;
                count = 0;
            } else {
                count += 1;
            }
        }

        return true;
    }
}
