public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;

        for (int bill : bills) {
            if (bill == 5) {
                five += 1;
            } else if (bill == 10 && five > 0) {
                five -= 1;
                ten += 1;
            } else if (bill == 20 && ten > 0 && five > 0) {
                five -= 1;
                ten -= 1;
            } else if (bill == 20 && five >= 3) {
                five -= 3;
            } else {
                return false;
            }
        }

        return true;
    }
}
