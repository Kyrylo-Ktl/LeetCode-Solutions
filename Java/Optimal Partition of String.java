import java.util.HashSet;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int partitionString(String s) {
        HashSet<Character> usedChars = new HashSet<>();
        int numOfPartitions = 0;

        for (int i = 0; i < s.length(); ++i) {
            if (usedChars.contains(s.charAt(i))) {
                usedChars.clear();
                numOfPartitions += 1;
            }
            usedChars.add(s.charAt(i));
        }

        return numOfPartitions + 1;
    }
}
