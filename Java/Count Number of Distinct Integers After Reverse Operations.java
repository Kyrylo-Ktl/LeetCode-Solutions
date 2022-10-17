import java.util.HashSet;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int countDistinctIntegers(int[] nums) {
        HashSet<Integer> uniq = new HashSet<>();

        for (int num : nums) {
            uniq.add(num);
            int reverse = 0;

            for (; num != 0; num /= 10)
                reverse = reverse * 10 + num % 10;

            uniq.add(reverse);
        }

        return uniq.size();
    }
}
