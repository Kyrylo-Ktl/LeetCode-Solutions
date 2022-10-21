class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int maxDistance(int[] colors) {
        int maxDist = 0, n = colors.length;

        for (int i = 0; i < n; ++i) {
            if (colors[i] != colors[0])
                maxDist = Math.max(maxDist, i);
            if (colors[i] != colors[n - 1])
                maxDist = Math.max(maxDist, n - i - 1);
        }

        return maxDist;
    }
}
