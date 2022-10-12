import java.util.Arrays;

public class Solution {

    /**
     * Time:   O(n*log(n))
     * Memory: O(1)
     */
    public int largestPerimeter(int[] A) {
        Arrays.sort(A);

        for (int i = A.length - 3; i >= 0; --i)
            if (A[i] + A[i + 1] > A[i + 2])
                return A[i] + A[i + 1] + A[i + 2];

        return 0;
    }
}
