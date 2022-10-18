public class Solution {

    /**
     * Time:   O(1)
     * Memory: O(1)
     */
    public String tictactoe(int[][] moves) {
        int cross_mask = 0, zero_mask = 0;

        for (int i = 0; i < moves.length; ++i) {
            if ((i & 1) != 0)
                zero_mask |= 1 << 3 * moves[i][0] + moves[i][1];
            else
                cross_mask |= 1 << 3 * moves[i][0] + moves[i][1];
        }

        for (int mask : WIN_MASKS) {
            if ((mask & cross_mask) == mask)
                return "A";
            if ((mask & zero_mask) == mask)
                return "B";
        }

        return moves.length == 9 ? "Draw" : "Pending";
    }

    private static final int[] WIN_MASKS = new int[]{7, 56, 73, 84, 146, 273, 292, 448};
}
