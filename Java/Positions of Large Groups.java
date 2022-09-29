import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public List<List<Integer>> largeGroupPositions(String s) {
        List<List<Integer>> positions = new ArrayList<>();
        int j = 0;

        for (int i = 0; i < s.length(); ++i) {
            if (i == s.length() - 1 || s.charAt(i) != s.charAt(i + 1)) {
                if (i - j + 1 >= MIN_GROUP_SIZE)
                    positions.add(Arrays.asList(j, i));
                j = i + 1;
            }
        }

        return positions;
    }

    static final public int MIN_GROUP_SIZE = 3;
}
