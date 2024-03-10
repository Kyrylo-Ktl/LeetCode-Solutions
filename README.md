
# [LeetCode](https://leetcode.com/)

The repository contains the best versions of my solutions to LeetCode problems

## Author

- [Kyrylo-Ktl](https://leetcode.com/Kyrylo-Ktl) on LeetCode

## Complexity chart

<p align="center">
    <img alt="complexity_chart" src="https://user-images.githubusercontent.com/93226646/191962988-602fb801-6d39-42f2-ac5b-32fd6452cddd.png">
</p>

## Number of operations for complexity

|    $f(n)$    |      $n = 10$       |       $n = 10^{2}$        |       $n = 10^{3}$        |      $n = 10^{4}$       |      $n = 10^{5}$       |      $n = 10^{6}$       |
|:------------:|:-------------------:|:-------------------------:|:-------------------------:|:-----------------------:|:-----------------------:|:-----------------------:|
|     $1$      |         $1$         |            $1$            |            $1$            |           $1$           |           $1$           |           $1$           |
|   $\log n$   |   $\approx 3.32$    |      $\approx 6.64$       |      $\approx 9.97$       |   $\approx 1.33 * 10$   |   $\approx 1.66 * 10$   |   $\approx 1.99 * 10$   |
|     $n$      |        $10$         |         $10^{2}$          |         $10^{3}$          |        $10^{4}$         |        $10^{5}$         |        $10^{6}$         |
| $n * \log n$ | $\approx 3.32 * 10$ |  $\approx 6.64 * 10^{2}$  |  $\approx 9.97 * 10^{3}$  | $\approx 1.33 * 10^{5}$ | $\approx 1.66 * 10^{6}$ | $\approx 1.99 * 10^{7}$ |
|   $n^{2}$    |      $10^{2}$       |         $10^{4}$          |         $10^{6}$          |        $10^{8}$         |        $10^{10}$        |        $10^{12}$        |
|   $2^{n}$    |  $\approx 10^{3}$   |     $\approx 10^{30}$     |    $\approx 10^{301}$     |   $\approx 10^{3010}$   |  $\approx 10^{30102}$   |  $\approx 10^{301030}$  |
|     $n!$     |  $\approx 10^{7}$   |    $\approx 10^{156}$     |    $\approx 10^{2568}$    |  $\approx 10^{35660}$   |  $\approx 10^{456574}$  | $\approx 10^{5565709}$  |

## Complexity notations

| Notation |     Name     |  Sign  |           Meaning           |
|:--------:|:------------:|:------:|:---------------------------:|
|   $o$    |   Little O   |  $<$   |          Less than          |
|   $O$    |    Big O     | $\leq$ |    Less than or equal to    |
| $\Theta$ |    Theta     |  $=$   |          Equal to           |
| $\Omega$ |  Big Omega   | $\geq$ |  Greater than or equal to   |
| $\omega$ | Little Omega |  $>$   |        Greater than         |

## Solutions

| № | Title | Solutions | Time | Memory | Notes | Beats Time | Beats Memory |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | [Python](Python/Path%20Sum.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Python](Python/Sum%20Root%20to%20Leaf%20Numbers.py) | $O(n)$ | $O(h)$ | DFS | 97.50% | 95.89% |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Python](Python/Serialize%20and%20Deserialize%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Preorder | - | - |
| 342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | [Python](Python/Power%20of%20Four.py) | $O(1)$ | $O(1)$ | - | - | - |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [Python](Python/Minimum%20Number%20of%20Arrows%20to%20Burst%20Balloons.py) | $O(n * \log_{2} n)$ | $O(1)$ | Greedy | - | - |
| 491 | [Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/) | [Python](Python/Non-decreasing%20Subsequences.py) | $O(n^{2})$ | $O(n^{2})$ | - | - | - |
| 511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | [SQL](SQL/Game%20Play%20Analysis%20I.sql) | SQL | SQL | - | - | - |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python](Python/Subarray%20Sum%20Equals%20K.py) | $O(n)$ | $O(n)$ | - | - | - |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | [SQL](SQL/Find%20Customer%20Referee.sql) | SQL | SQL | - | - | - |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [Python](Python/Maximum%20Average%20Subarray%20I.py) | $O(n)$ | $O(1)$ | Sliding Window | - | - |
| 718 | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | [Python](Python/Maximum%20Length%20of%20Repeated%20Subarray.py) | $O(n*m)$ | $O(n*m)$ | DP | - | - |
| 814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | [Python](Python/Binary%20Tree%20Pruning.py) | $O(n)$ | $O(n)$ | - | - | - |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [Python](Python/Koko%20Eating%20Bananas.py) | $O(n * \log_{2} M)$ | $O(1)$ | Binary Search | 98.57% | 62.98% |
| 944 | [Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/) | [Python](Python/Delete%20Columns%20to%20Make%20Sorted.py) | $O(m * n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | [Python](Python/Reduce%20Array%20Size%20to%20The%20Half.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 1848 | [Minimum Distance to the Target Element](https://leetcode.com/problems/minimum-distance-to-the-target-element/) | [Python](Python/Minimum%20Distance%20to%20the%20Target%20Element.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2367 | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) | [Python](Python/Number%20of%20Arithmetic%20Triplets.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2390 | [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/) | [Python](Python/Removing%20Stars%20From%20a%20String.py) | - | - | - | - | - |
| 2487 | [Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/) | [Python](Python/Remove%20Nodes%20From%20Linked%20List.py) | - | - | - | - | - |
| 2525 | [Categorize Box According to Criteria](https://leetcode.com/problems/categorize-box-according-to-criteria/) | [Python](Python/Categorize%20Box%20According%20to%20Criteria.py) | $O(1)$ | $O(1)$ | - | - | - |
| 2529 | [Maximum Count of Positive Integer and Negative Integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) | [Python](Python/Maximum%20Count%20of%20Positive%20Integer%20and%20Negative%20Integer.py) | $O(\log_{2} n)$ | $O(1)$ | - | - | - |
| 2549 | [Count Distinct Numbers on Board](https://leetcode.com/problems/count-distinct-numbers-on-board/) | [Python](Python/Count%20Distinct%20Numbers%20on%20Board.py) | - | - | - | - | - |

## Last update

Solution table for problems was generated automatically on 2024-03-10 18:02 +0000

