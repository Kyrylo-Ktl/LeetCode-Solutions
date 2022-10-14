public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int[] findArray(int[] pref) {
        for (int i = pref.length - 1; i > 0; --i)
            pref[i] ^= pref[i - 1];
        return pref;
    }
}
