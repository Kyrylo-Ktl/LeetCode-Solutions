class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean checkRecord(String s) {
        return s.indexOf("A") == s.lastIndexOf("A") && !s.contains("LLL");
    }
}
