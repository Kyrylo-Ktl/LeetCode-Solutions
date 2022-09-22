class Solution {

    /**
     * Time:   O(1)
     * Memory: O(1)
     */
    public int smallestEvenMultiple(int n) {
        return n << (n & 1);
    }
}
