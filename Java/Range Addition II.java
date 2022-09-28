public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int maxCount(int rows, int cols, int[][] ops) {
        int minRow = rows;
        int minCol = cols;

        for (int[] op : ops) {
            minRow = Math.min(minRow, op[0]);
            minCol = Math.min(minCol, op[1]);
        }

        return minRow * minCol;
    }
}
