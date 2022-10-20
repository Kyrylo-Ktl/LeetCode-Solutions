public class Solution {

    /**
     * Time:   O(n*m)
     * Memory: O(n*m)
     */
    public int uniquePaths(int n, int m) {
        int[][] grid = new int[m][n];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || j == 0) {
                    grid[i][j] = 1;
                } else {
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j];
                }
            }
        }

        return grid[m - 1][n - 1];
    }
}


public class Solution {

    /**
     * Time:   O(min(n,m))
     * Memory: O(1)
     */
    public int uniquePaths(int n, int m) {
        long paths = 1;

        for (int i = m + n - 2, j = 1; i >= Math.max(m, n); --i, ++j)
            paths = (paths * i) / j;

        return (int) paths;
    }
}
