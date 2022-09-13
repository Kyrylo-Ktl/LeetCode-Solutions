import java.util.HashMap;

class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for (int i = 0; i < numbers.length; i++) {
            Integer diff = target - numbers[i];
            if (hash.containsKey(diff))
                return new int[]{hash.get(diff), i};
            hash.put(numbers[i], i);
        }

        return null;
    }
}
