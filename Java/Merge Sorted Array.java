public class Solution {

    /**
     * Time:   O(n + m)
     * Memory: O(1)
     */
    public void merge(int[] first, int n, int[] second, int m) {
        int i = n - 1, j = m - 1;

        for (int curr = n + m - 1; curr >= 0; --curr)
            if (j < 0)
                first[curr] = first[i--];
            else if (i < 0)
                first[curr] = second[j--];
            else if (first[i] > second[j])
                first[curr] = first[i--];
            else
                first[curr] = second[j--];

    }
}
