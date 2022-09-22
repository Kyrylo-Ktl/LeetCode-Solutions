class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public String reverseWords(String s) {
        StringBuilder reversed = new StringBuilder();

        for (String word : s.split("\\s"))
            reversed.append(new StringBuilder(word).reverse()).append(" ");

        return reversed.toString().trim();
    }
}
