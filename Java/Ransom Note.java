class Solution {

    /**
     * Time:   O(n+m)
     * Memory: O(1)
     */
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] arr = new int[26];

        for (int i = 0; i < magazine.length(); ++i)
            arr[magazine.charAt(i) - 'a']++;

        for (int i = 0; i < ransomNote.length(); ++i)
            if (--arr[ransomNote.charAt(i) - 'a'] < 0)
                return false;

        return true;
    }
}


class Solution {

    /**
     * Time:   O(n+m)
     * Memory: O(1)
     */
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] arr = new int[26];

        for (char c : magazine.toCharArray())
            arr[c - 'a']++;

        for (char c : ransomNote.toCharArray())
            if (--arr[c - 'a'] < 0)
                return false;

        return true;
    }
}
