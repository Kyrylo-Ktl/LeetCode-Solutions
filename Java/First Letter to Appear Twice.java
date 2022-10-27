import java.util.HashSet;
import java.util.Set;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public char repeatedCharacter(String s) {
        Set<Character> seen = new HashSet<>();

        for (char c : s.toCharArray()) {
            if (seen.contains(c))
                return c;
            seen.add(c);
        }

        return '#';
    }
}


public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public char repeatedCharacter(String s) {
        boolean[] seen = new boolean[26];

        for (char c : s.toCharArray()) {
            if (seen[c - 'a'])
                return c;
            seen[c - 'a'] = true;
        }

        return '#';
    }
}
