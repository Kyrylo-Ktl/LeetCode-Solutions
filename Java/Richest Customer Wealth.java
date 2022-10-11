import java.util.Arrays;

public class Solution {

    /**
     * Time:   O(n*m)
     * Memory: O(1)
     */
    public int maximumWealth(int[][] accounts) {
        return Arrays.stream(accounts).mapToInt(row -> Arrays.stream(row).sum()).max().getAsInt();
    }
}
