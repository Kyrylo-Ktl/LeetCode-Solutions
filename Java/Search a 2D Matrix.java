public class Solution {

    /**
     * Time:   O(log(n*m))
     * Memory: O(1)
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length, m = matrix[0].length;
        int left = 0, right = n * m - 1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int num = matrix[mid / m][mid % m];

            if (num == target)
                return true;

            if (num < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
}
