public class Solution {

    /**
     * Time:   O(log(n))
     * Memory: O(1)
     */
    public int minBitFlips(int start, int goal) {
        int diff = start ^ goal, flips = 0;

        for (int i = 0; i < 32; ++i)
            if ((diff & (1 << i)) != 0)
                flips += 1;

        return flips;
    }
}

public class Solution {

    /**
     * Time:   O(log(n))
     * Memory: O(1)
     */
    public int minBitFlips(int start, int goal) {
        return Integer.bitCount(start ^ goal);
    }
}
