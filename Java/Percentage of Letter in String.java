public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int percentageLetter(String s, char letter) {
        int count = 0;

        for (int i = 0; i < s.length(); ++i)
            if (s.charAt(i) == letter)
                count += 1;

        return count * 100 / s.length();
    }
}


public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public int percentageLetter(String s, char letter) {
        return (int) (s.chars().filter(ch -> ch == letter).count() * 100 / s.length());
    }
}
