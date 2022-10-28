public class Solution {

    /**
     * Time:   O(n^3)
     * Memory: O(n^2)
     */
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] dist = new int[n][n];

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (i != j)
                    dist[i][j] = INF;

        for (int[] edge : edges) {
            dist[edge[0]][edge[1]] = edge[2];
            dist[edge[1]][edge[0]] = edge[2];
        }

        for (int k = 0; k < n; ++k)
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    dist[i][j] = Math.min(dist[i][k] + dist[k][j], dist[i][j]);

        int minCity = 0, minNeighbours = n;
        for (int i = 0; i < n; ++i) {
            int neighbours = 0;

            for (int j = 0; j < n; ++j)
                if (dist[i][j] <= distanceThreshold) neighbours += 1;

            if (neighbours <= minNeighbours) {
                minCity = i;
                minNeighbours = neighbours;
            }
        }

        return minCity;
    }

    public static final int INF = 1_000_000;
}
