class Solution {

    /**
     * Time:   O(n^2)
     * Memory: O(n^2)
     */
    public int numIslands(char[][] grid) {
        int n = grid.length, m = grid[0].length;

        int islands = 0;
        for (int row = 0; row < n; ++row)
            for (int col = 0; col < m; ++col)
                if (grid[row][col] == LAND) {
                    visitIsland(row, col, grid);
                    islands += 1;
                }

        return islands;
    }

    private static void visitIsland(int row, int col, char[][] grid) {
        int n = grid.length, m = grid[0].length;
        grid[row][col] = WATER;

        if (row > 0     && grid[row - 1][col] == LAND) visitIsland(row - 1, col, grid);
        if (row < n - 1 && grid[row + 1][col] == LAND) visitIsland(row + 1, col, grid);
        if (col > 0     && grid[row][col - 1] == LAND) visitIsland(row, col - 1, grid);
        if (col < m - 1 && grid[row][col + 1] == LAND) visitIsland(row, col + 1, grid);
    }

    public static final char WATER = '0';
    public static final char LAND = '1';
}
