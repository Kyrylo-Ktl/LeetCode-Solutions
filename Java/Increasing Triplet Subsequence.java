public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean increasingTriplet(int[] nums) {
        int firstMin = Integer.MAX_VALUE, secondMin = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num <= firstMin) {
                firstMin = num;
            } else if (num <= secondMin) {
                secondMin = num;
            } else {
                return true;
            }
        }

        return false;
    }
}
