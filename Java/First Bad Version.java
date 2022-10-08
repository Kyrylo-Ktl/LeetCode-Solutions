public class Solution extends VersionControl {

    /**
     * Time:   O(log(n))
     * Memory: O(1)
     */
    public int firstBadVersion(int n) {
        int left = 0, right = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid))
                right = mid - 1;
            else
                left = mid + 1;
        }

        return left;
    }
}
