import java.util.HashMap;
import java.util.Map;

class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; ++i) {
            if (map.containsKey(nums[i]) && i - map.get(nums[i]) <= k)
                return true;
            map.put(nums[i], i);
        }

        return false;
    }
}
