public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean checkIfPangram(String sentence) {
        int seen = 0;

        for (char ch : sentence.toCharArray())
            seen |= 1 << (ch - 'a');

        return seen == (1 << 26) - 1;
    }
}

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean checkIfPangram(String sentence) {
        return sentence.chars().reduce(0, (seen, ch) -> seen | 1 << (ch - 'a')) == (1 << 26) - 1;
    }
}

import java.util.stream.Collectors;

public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean checkIfPangram(String sentence) {
        return sentence.chars().boxed().collect(Collectors.toSet()).size() == 26;
    }
}
