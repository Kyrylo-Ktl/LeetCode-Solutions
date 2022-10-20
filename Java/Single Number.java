import java.util.Arrays;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int singleNumber(int[] nums) {
        int single = 0;

        for (int num : nums)
            single ^= num;

        return single;
    }
}

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int singleNumber(int[] nums) {
        return Arrays.stream(nums).reduce(0, (single, num) -> single ^ num);
    }
}
