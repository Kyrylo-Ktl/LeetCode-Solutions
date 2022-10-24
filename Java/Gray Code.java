import java.util.ArrayList;
import java.util.List;

class Solution {

    /**
     * Time:   O(2^n)
     * Memory: O(2^n)
     */
    public List<Integer> grayCode(int n) {
        List<Integer> grayCode = new ArrayList<>();

        for (int i = 0; i < 1 << n; ++i)
            grayCode.add(i ^ (i >> 1));

        return grayCode;
    }
}

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {

    /**
     * Time:   O(2^n)
     * Memory: O(2^n)
     */
    public List<Integer> grayCode(int n) {
        return IntStream.range(0, 1 << n).map(i -> i ^ (i >> 1)).boxed().collect(Collectors.toList());
    }
}
