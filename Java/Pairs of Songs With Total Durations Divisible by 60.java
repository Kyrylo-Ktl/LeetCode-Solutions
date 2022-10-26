import java.util.HashMap;
import java.util.Map;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int numPairsDivisibleBy60(int[] time) {
        Map<Integer, Integer> memo = new HashMap<>();
        int pairsCount = 0;

        for (int t : time) {
            pairsCount += memo.getOrDefault((60 - t % 60) % 60, 0);
            memo.put(t % 60, 1 + memo.getOrDefault(t % 60, 0));
        }

        return pairsCount;
    }
}


public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int numPairsDivisibleBy60(int[] time) {
        int[] leftovers = new int[60];
        int pairsCount = 0;

        for (int t : time) {
            pairsCount += leftovers[(60 - t % 60) % 60];
            leftovers[t % 60] += 1;
        }

        return pairsCount;
    }
}
