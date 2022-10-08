import java.util.HashSet;
import java.util.Set;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int distributeCandies(int[] candyType) {
        Set<Integer> uniqueCandiesSet = new HashSet<>();

        for (int candy : candyType)
            uniqueCandiesSet.add(candy);

        return Math.min(uniqueCandiesSet.size(), candyType.length / 2);
    }
}
