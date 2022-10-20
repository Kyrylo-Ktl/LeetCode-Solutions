public class Solution {

    /**
     * Time:   O(n^3)
     * Memory: O(1)
     */
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < SIZE * SIZE; ++i) {
            for (int j = 0; j < SIZE * SIZE; ++j) {
                if (board[i][j] == EMPTY)
                    continue;

                for (int k = 0; k < SIZE * SIZE; ++k) {
                    if (board[i][k] == board[i][j] && k != j)
                        return false;
                    if (board[k][j] == board[i][j] && k != i)
                        return false;
                }

                int row = i - i % SIZE;
                int col = j - j % SIZE;


                for (int r = row; r < row + SIZE; ++r)
                    for (int c = col; c < col + SIZE; ++c)
                        if (board[r][c] == board[i][j] && (r != i || c != j))
                            return false;
            }
        }

        return true;
    }

    private static final int SIZE = 3;
    private static final char EMPTY = '.';
}
