class Solution {

    /**
     * Time:   O(log(n))
     * Memory: O(log(n))
     */
    public int lastRemaining(int n) {
        return n == 1 ? 1 : 2 * (n / 2 + 1 - lastRemaining(n / 2));
    }
}
