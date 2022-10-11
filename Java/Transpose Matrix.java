public class Solution {

    /**
     * Time:   O(n*m)
     * Memory: O(1)
     */
    public int[][] transpose(int[][] A) {
        int n = A.length, m = A[0].length;
        int[][] transposed = new int[m][n];

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                transposed[j][i] = A[i][j];

        return transposed;
    }
}
