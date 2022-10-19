public class Solution {

    /**
     * Time:   O(n*m)
     * Memory: O(n*m)
     */
    public int minDistance(String first, String second) {
        int n = first.length(), m = second.length();
        int[][] dp = new int[n + 1][m + 1];

        for (int i = 0; i <= n; ++i)
            dp[i][0] = i;

        for (int j = 0; j <= m; ++j)
            dp[0][j] = j;

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (first.charAt(i - 1) == second.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
            }
        }

        return dp[n][m];
    }
}
