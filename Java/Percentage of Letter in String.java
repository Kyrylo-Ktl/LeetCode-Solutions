public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int percentageLetter(String s, char letter) {
        return (int) (s.chars().filter(ch -> ch == letter).count() * 100 / s.length());
    }
}
