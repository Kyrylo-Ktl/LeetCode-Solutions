public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0, right = height.length - 1;

        while (left < right) {
            maxArea = Math.max(Math.min(height[left], height[right]) * (right - left), maxArea);

            if (height[left] < height[right]) {
                ++left;
            } else {
                --right;
            }
        }

        return maxArea;
    }
}
