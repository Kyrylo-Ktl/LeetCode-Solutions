public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean canChange(String start, String target) {
        int n = start.length();
        int i = 0, j = 0;

        while (i < n || j < n) {
            while (i < n && start.charAt(i) == SKIP) ++i;
            while (j < n && target.charAt(j) == SKIP) ++j;

            if (i == n && j == n)
                return true;

            if (i == n || j == n)
                return false;

            if (start.charAt(i) != target.charAt(j)) return false;
            if (start.charAt(i) == LEFT && i < j) return false;
            if (start.charAt(i) == RIGHT && i > j) return false;

            ++i;
            ++j;
        }

        return true;
    }

    public static final char SKIP = '_';
    public static final char LEFT = 'L';
    public static final char RIGHT = 'R';
}
