import java.util.HashSet;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> uniq = new HashSet<Integer>();

        for (int num : nums) {
            if (uniq.contains(num)) {
                return true;
            }
            uniq.add(num);
        }

        return false;
    }
}
