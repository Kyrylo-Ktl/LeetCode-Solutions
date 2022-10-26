import java.util.HashMap;
import java.util.Map;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(0, 0);
        int s = 0;

        for (int i = 0; i < nums.length; ++i) {
            s = (s + nums[i]) % k;

            if (!memo.containsKey(s))
                memo.put(s, i + 1);
            else if (memo.get(s) < i)
                return true;
        }
        return false;
    }
}
