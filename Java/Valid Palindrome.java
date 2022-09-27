public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;

        char head, tail;
        while (left < right) {
            head = s.charAt(left);
            tail = s.charAt(right);

            if (!Character.isLetterOrDigit(head))
                ++left;
            else if (!Character.isLetterOrDigit(tail))
                --right;
            else if (Character.toLowerCase(head) != Character.toLowerCase(tail))
                return false;
            else {
                ++left;
                --right;
            }
        }

        return true;
    }
}
