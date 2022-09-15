import java.util.Map;
import java.util.TreeMap;

class Solution {

    /**
     * Time: O(n*log(k))
     * Memory: (n)
     * where k - number of unique numbers
     */
    public int[] findOriginalArray(int[] changed) {
        int n = changed.length;
        if (n % 2 == 1)
            return new int[0];

        Map<Integer, Integer> count = new TreeMap<>();
        for (int a : changed)
            count.put(a, count.getOrDefault(a, 0) + 1);

        int[] res = new int[n / 2];
        int i = 0;
        for (int x : count.keySet()) {
            if (count.get(x) > count.getOrDefault(2 * x, 0))
                return new int[0];

            for (int j = 0; j < count.get(x); ++j) {
                res[i++] = x;
                count.put(2 * x, count.get(2 * x) - 1);
            }
        }

        return res;
    }
}
