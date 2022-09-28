public class Solution {

    /**
     * Time:   O(log(n))
     * Memory: O(log(n))
     */
    public int findGCD(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        return gcd(min, max);
    }

    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}


public class Solution {

    /**
     * Time:   O(log(n))
     * Memory: O(1)
     */
    public int findGCD(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        return gcd(min, max);
    }

    private static int gcd(int a, int b) {
        while (a != 0 && b != 0) {
            int t = a;
            a = b % a;
            b = t;
        }
        return a == 0 ? b : a;
    }
}
