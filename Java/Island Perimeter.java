public class Solution {

    /**
     * Time:   O(n*m)
     * Memory: O(1)
     */
    public int islandPerimeter(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int perimeter = 0;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] != LAND)
                    continue;

                if (i == 0 || grid[i - 1][j] == WATER)
                    perimeter += 1;
                if (i + 1 == n || grid[i + 1][j] == WATER)
                    perimeter += 1;
                if (j == 0 || grid[i][j - 1] == WATER)
                    perimeter += 1;
                if (j + 1 == m || grid[i][j + 1] == WATER)
                    perimeter += 1;
            }
        }
        return perimeter;
    }

    public static final int WATER = 0, LAND = 1;
}
