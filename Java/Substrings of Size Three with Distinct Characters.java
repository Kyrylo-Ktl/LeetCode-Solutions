import java.util.HashMap;

class Solution {

    /**
     * Time:   O(n)
     * Memory: O(min(n,k))
     */
    public int countGoodSubstrings(String s) {
        HashMap<Character, Integer> window = new HashMap<>();

        for (int i = 0; i < Math.min(K, s.length()); ++i)
            window.put(s.charAt(i), window.getOrDefault(s.charAt(i), 0) + 1);

        int count = window.size() == K ? 1 : 0;

        for (int i = K; i < s.length(); ++i) {
            if (window.getOrDefault(s.charAt(i - K), 0) > 1)
                window.put(s.charAt(i - K), window.get(s.charAt(i - K)) - 1);
            else
                window.remove(s.charAt(i - K));

            window.put(s.charAt(i), window.getOrDefault(s.charAt(i), 0) + 1);
            count += window.size() == K ? 1 : 0;
        }

        return count;
    }

    private static final int K = 3;
}
