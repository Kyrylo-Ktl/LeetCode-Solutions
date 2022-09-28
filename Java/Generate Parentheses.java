import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Time:   O(2^n)
     * Memory: O(n)
     */
    public List<String> generateParenthesis(int n) {
        List<String> parenthesis = new ArrayList<>();
        generateParenthesis(n, n, "", parenthesis);
        return parenthesis;
    }

    private void generateParenthesis(int opened, int closed, String string, List<String> result) {
        if (opened == 0 && closed == 0)
            result.add(string);
        else if (closed >= opened) {
            if (opened > 0)
                generateParenthesis(opened - 1, closed, string + '(', result);
            if (closed > 0)
                generateParenthesis(opened, closed - 1, string + ')', result);
        }
    }
}
