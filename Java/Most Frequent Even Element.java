import java.util.HashMap;

class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int mostFrequentEven(int[] nums) {
        HashMap<Integer, Integer> numFrequency = new HashMap<>();
        int mostFreq = -1, maxFreq = 0;

        for (var n : nums) {
            if (n % 2 != 0)
                continue;

            int freq = numFrequency.getOrDefault(n, 0) + 1;
            numFrequency.put(n, freq);

            if (freq > maxFreq || freq == maxFreq && mostFreq > n) {
                mostFreq = n;
                maxFreq = freq;
            }
        }

        return mostFreq;
    }
}
