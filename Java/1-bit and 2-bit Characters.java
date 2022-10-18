public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0, n = bits.length - 1;

        while (i < n) {
            i += bits[i] == 1 ? 2 : 1;
        }

        return i == n;
    }
}
