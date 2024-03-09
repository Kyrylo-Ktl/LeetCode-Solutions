
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
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](Python/Two%20Sum.py), [Java](Java/Two%20Sum.java) | $O(n)$ | $O(n)$ | - | 99.78% | 88.62% |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | [Python](Python/Regular%20Expression%20Matching.py) | $O(n*m)$ | $O(n*m)$ | DP | - | - |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](Python/Container%20With%20Most%20Water.py), [Java](Java/Container%20With%20Most%20Water.java) | $O(n)$ | $O(1)$ | Two Pointers | 98.13% | 91.81% |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](Python/Integer%20to%20Roman.py) | $O(1)$ | $O(1)$ | - | - | - |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](Python/Roman%20to%20Integer.py) | $O(1)$ | $O(1)$ | - | - | - |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [Python](Python/Longest%20Common%20Prefix.py) | $O(n)$ | $O(1)$ | - | - | - |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](Python/3Sum.py) | $O(n^{2})$ | $O(1)$ | Two Pointers | - | - |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | [Python](Python/Generate%20Parentheses.py), [Java](Java/Generate%20Parentheses.java) | $O(2^{n})$ | $O(n)$ | Backtracking | - | - |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Python](Python/Remove%20Duplicates%20from%20Sorted%20Array.py), [Java](Java/Remove%20Duplicates%20from%20Sorted%20Array.java) | $O(n)$ | $O(1)$ | - | 100.00% | 85.81% |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](Python/Valid%20Sudoku.py), [Java](Java/Valid%20Sudoku.java) | $O(n^{2})$ | $O(n^{2})$ | - | 100.00% | 97.10% |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](Python/Trapping%20Rain%20Water.py) | $O(n)$ | $O(n)$ | - | - | - |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python](Python/Group%20Anagrams.py) | $O(n * m * \log_{2} m)$ | $O(n * m)$ | - | - | - |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | [Python](Python/Pow(x,%20n).py) | $O(\log_{2} n)$ | $O(\log_{2} n)$ | BinPow | - | - |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](Python/Maximum%20Subarray.py), [Java](Java/Maximum%20Subarray.java) | $O(n)$ | $O(1)$ | Kadane's | 100.00% | 93.17% |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | [Python](Python/Climbing%20Stairs.py) | $O(n)$ | $O(n)$ | DP | - | - |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | [Python](Python/Simplify%20Path.py) | $O(n)$ | $O(n)$ | - | - | - |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | [Python](Python/Edit%20Distance.py), [Java](Java/Edit%20Distance.java) | $O(n*m)$ | $O(n*m)$ | DP | 92.85% | 91.32% |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | [Python](Python/Search%20a%202D%20Matrix.py), [Java](Java/Search%20a%202D%20Matrix.java) | $O(\log_{2} (n*m))$ | $O(1)$ | Binary Search | - | - |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | [Python](Python/Merge%20Sorted%20Array.py), [Java](Java/Merge%20Sorted%20Array.java) | $O(n + m)$ | $O(1)$ | - | 100.00% | 83.33% |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | [Python](Python/Decode%20Ways.py) | $O(n)$ | $O(n)$ | DP | - | - |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](Python/Validate%20Binary%20Search%20Tree.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | [Python](Python/Symmetric%20Tree.py) | $O(n)$ | $O(n)$ | DFS, BFS | - | - |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](Python/Maximum%20Depth%20of%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | [Python](Python/Convert%20Sorted%20List%20to%20Binary%20Search%20Tree.py) | $O(n*\log_{2} n)$ | $O(\log_{2} n)$ | DFS | - | - |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | [Python](Python/Path%20Sum.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | [Python](Python/Flatten%20Binary%20Tree%20to%20Linked%20List.py) | $O(n)$ | $O(1)$ | - | - | - |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | [Python](Python/Word%20Ladder.py) | - | - | - | - | - |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Python](Python/Sum%20Root%20to%20Leaf%20Numbers.py) | $O(n)$ | $O(h)$ | DFS | 97.50% | 95.89% |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | [Python](Python/Single%20Number.py), [Java](Java/Single%20Number.java) | $O(n)$ | $O(1)$ | - | 100.00% | 93.84% |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [Python](Python/Reverse%20Words%20in%20a%20String.py) | $O(n)$ | $O(n)$ | - | - | - |
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | [Python](Python/Min%20Stack.py) | $O(1)$ | $O(n)$ | - | - | - |
| 168 | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) | [Python](Python/Excel%20Sheet%20Column%20Title.py) | $O(\log_{26} n)$ | $O(1)$ | - | - | - |
| 172 | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | [Python](Python/Factorial%20Trailing%20Zeroes.py) | $O(\log_{5} n)$ | $O(\log_{5} n)$ | Math | - | - |
| 181 | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | [SQL](SQL/Employees%20Earning%20More%20Than%20Their%20Managers.sql) | SQL | SQL | - | - | - |
| 185 | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | [SQL](SQL/Department%20Top%20Three%20Salaries.sql) | SQL | SQL | - | - | - |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | [Python](Python/Reverse%20Bits.py), [Java](Java/Reverse%20Bits.java) | $O(1)$ | $O(1)$ | - | - | - |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | [Python](Python/Number%20of%201%20Bits.py) | $O(\log_{10} n)$ | $O(1)$ | - | - | - |
| 192 | [Word Frequency](https://leetcode.com/problems/word-frequency/) | [Shell](Shell/Word%20Frequency.sh) | SHELL | SHELL | - | - | - |
| 193 | [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/) | [Shell](Shell/Valid%20Phone%20Numbers.sh) | SHELL | SHELL | - | - | - |
| 194 | [Transpose File](https://leetcode.com/problems/transpose-file/) | [Shell](Shell/Transpose%20File.sh) | SHELL | SHELL | - | - | - |
| 195 | [Tenth Line](https://leetcode.com/problems/tenth-line/) | [Shell](Shell/Tenth%20Line.sh) | SHELL | SHELL | - | - | - |
| 196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) | [SQL](SQL/Delete%20Duplicate%20Emails.sql) | SQL | SQL | - | - | - |
| 197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) | [SQL](SQL/Rising%20Temperature.sql) | SQL | SQL | - | - | - |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | [Python](Python/House%20Robber.py) | $O(n)$ | $O(n)$ | DP | - | - |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](Python/Number%20of%20Islands.py), [Java](Java/Number%20of%20Islands.java) | $O(n*m)$ | $O(n*m)$ | DFS | - | - |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](Python/Reverse%20Linked%20List.py) | $O(n)$ | $O(1)$ | - | - | - |
| 223 | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) | [Python](Python/Rectangle%20Area.py) | $O(1)$ | $O(1)$ | Math | - | - |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | [Python](Python/Palindrome%20Linked%20List.py) | $O(n)$ | $O(1)$ | - | - | - |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Python](Python/Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.py) | $O(n)$ | $O(n)$ | - | - | - |
| 237 | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [Python](Python/Delete%20Node%20in%20a%20Linked%20List.py), [Java](Java/Delete%20Node%20in%20a%20Linked%20List.java) | $O(1)$ | $O(1)$ | - | - | - |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](Python/Valid%20Anagram.py) | $O(max(n,m))$ | $O(n+m)$ | - | - | - |
| 258 | [Add Digits](https://leetcode.com/problems/add-digits/) | [Python](Python/Add%20Digits.py) | $O(1)$ | $O(1)$ | - | - | - |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Python](Python/Serialize%20and%20Deserialize%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Preorder | - | - |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | [Python](Python/Longest%20Increasing%20Subsequence.py) | $O(n*\log_{2} n)$ | $O(n)$ | - | - | - |
| 307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | [Python](Python/Range%20Sum%20Query%20-%20Mutable.py) | $O(n * \log_{2} n) + O(\log_{2} n)$ | $O(n) + O(1)$ | - | - | - |
| 326 | [Power of Three](https://leetcode.com/problems/power-of-three/) | [Python](Python/Power%20of%20Three.py) | $O(1)$ | $O(1)$ | - | - | - |
| 329 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [Python](Python/Longest%20Increasing%20Path%20in%20a%20Matrix.py) | $O(n * m)$ | $O(n * m)$ | - | - | - |
| 342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | [Python](Python/Power%20of%20Four.py) | $O(1)$ | $O(1)$ | - | - | - |
| 374 | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | [Python](Python/Guess%20Number%20Higher%20or%20Lower.py) | $O(\log_{2} n)$ | $O(1)$ | - | 75.79% | 66.34% |
| 377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | [Python](Python/Combination%20Sum%20IV.py) | $O(2^{n})$ | $O(n)$ | - | - | - |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [Python](Python/First%20Unique%20Character%20in%20a%20String.py) | $O(n)$ | $O(1)$ | - | - | - |
| 390 | [Elimination Game](https://leetcode.com/problems/elimination-game/) | [Python](Python/Elimination%20Game.py), [Java](Java/Elimination%20Game.java) | $O(\log_{2} n)$ | $O(\log_{2} n)$ | - | - | - |
| 393 | [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) | [Python](Python/UTF-8%20Validation.py) | $O(n)$ | $O(1)$ | - | - | - |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Python](Python/Pacific%20Atlantic%20Water%20Flow.py) | $O(n * m)$ | $O(n * m)$ | DFS | - | - |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Python](Python/Longest%20Repeating%20Character%20Replacement.py) | $O(n)$ | $O(1)$ | - | - | - |
| 429 | [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [Python](Python/N-ary%20Tree%20Level%20Order%20Traversal.py) | $O(n)$ | $O(n)$ | - | - | - |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [Python](Python/Minimum%20Number%20of%20Arrows%20to%20Burst%20Balloons.py) | $O(n * \log_{2} n)$ | $O(1)$ | Greedy | - | - |
| 463 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | [Python](Python/Island%20Perimeter.py), [Java](Java/Island%20Perimeter.java) | $O(n*m)$ | $O(1)$ | - | 94.28% | 94.13% |
| 468 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | [Python](Python/Validate%20IP%20Address.py) | $O(1)$ | $O(1)$ | RegEx | - | - |
| 491 | [Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/) | [Python](Python/Non-decreasing%20Subsequences.py) | $O(n^{2})$ | $O(n^{2})$ | - | - | - |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | [Python](Python/Target%20Sum.py) | $O(n*t)$ | $O(n*t)$ | - | - | - |
| 497 | [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | [Python](Python/Random%20Point%20in%20Non-overlapping%20Rectangles.py) | $O(n) + O(\log_{2} n)$ | $O(n) + O(1)$ | - | - | - |
| 508 | [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/) | [Python](Python/Most%20Frequent%20Subtree%20Sum.py) | $O(n)$ | $O(n)$ | - | - | - |
| 511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | [SQL](SQL/Game%20Play%20Analysis%20I.sql) | SQL | SQL | - | - | - |
| 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | [Python](Python/Continuous%20Subarray%20Sum.py), [Java](Java/Continuous%20Subarray%20Sum.java) | $O(n)$ | $O(n)$ | - | 95.90% | 91.04% |
| 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](Python/Diameter%20of%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | - | - | - |
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | [Python](Python/Number%20of%20Provinces.py) | $O(n^{2})$ | $O(n)$ | DSU | - | - |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python](Python/Subarray%20Sum%20Equals%20K.py) | $O(n)$ | $O(n)$ | - | - | - |
| 565 | [Array Nesting](https://leetcode.com/problems/array-nesting/) | [Python](Python/Array%20Nesting.py) | $O(n)$ | $O(n)$ | - | - | - |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | [SQL](SQL/Find%20Customer%20Referee.sql) | SQL | SQL | - | - | - |
| 592 | [Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction/) | [Python](Python/Fraction%20Addition%20and%20Subtraction.py) | $O(n)$ | $O(n)$ | - | - | - |
| 598 | [Range Addition II](https://leetcode.com/problems/range-addition-ii/) | [Python](Python/Range%20Addition%20II.py), [Java](Java/Range%20Addition%20II.java) | $O(n)$ | $O(1)$ | - | - | - |
| 606 | [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/) | [Python](Python/Construct%20String%20from%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | - | - | - |
| 607 | [Sales Person](https://leetcode.com/problems/sales-person/) | [SQL](SQL/Sales%20Person.sql) | SQL | SQL | - | - | - |
| 608 | [Tree Node](https://leetcode.com/problems/tree-node/) | [SQL](SQL/Tree%20Node.sql) | SQL | SQL | - | - | - |
| 609 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | [Python](Python/Find%20Duplicate%20File%20in%20System.py) | $O(n*k)$ | $O(n*k)$ | - | - | - |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) | [SQL](SQL/Not%20Boring%20Movies.sql) | SQL | SQL | - | - | - |
| 623 | [Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/) | [Python](Python/Add%20One%20Row%20to%20Tree.py) | $O(n)$ | $O(n)$ | - | - | - |
| 627 | [Swap Salary](https://leetcode.com/problems/swap-salary/) | [SQL](SQL/Swap%20Salary.sql) | SQL | SQL | - | - | - |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [Python](Python/Maximum%20Average%20Subarray%20I.py) | $O(n)$ | $O(1)$ | Sliding Window | - | - |
| 680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [Python](Python/Valid%20Palindrome%20II.py) | $O(n)$ | $O(1)$ | - | - | - |
| 692 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | [Python](Python/Top%20K%20Frequent%20Words.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 700 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | [Python](Python/Search%20in%20a%20Binary%20Search%20Tree.py) | $O(n)$ | $O(1)$ | - | - | - |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | [Python](Python/Binary%20Search.py) | $O(\log_{2} n)$ | $O(1)$ | - | - | - |
| 718 | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | [Python](Python/Maximum%20Length%20of%20Repeated%20Subarray.py) | $O(n*m)$ | $O(n*m)$ | DP | - | - |
| 747 | [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) | [Python](Python/Largest%20Number%20At%20Least%20Twice%20of%20Others.py) | $O(n)$ | $O(1)$ | - | - | - |
| 748 | [Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/) | [Python](Python/Shortest%20Completing%20Word.py) | $O(n^{2})$ | $O(n^{2})$ | - | - | - |
| 777 | [Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/) | [Python](Python/Swap%20Adjacent%20in%20LR%20String.py), [Java](Java/Swap%20Adjacent%20in%20LR%20String.java) | $O(n)$ | $O(1)$ | Two Pointers | 100.00% | 98.78% |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | [Python](Python/Find%20Eventual%20Safe%20States.py) | $O(V+E)$ | $O(V)$ | - | - | - |
| 804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | [Python](Python/Unique%20Morse%20Code%20Words.py) | $O(n)$ | $O(n)$ | - | - | - |
| 814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | [Python](Python/Binary%20Tree%20Pruning.py) | $O(n)$ | $O(n)$ | - | - | - |
| 836 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) | [Python](Python/Rectangle%20Overlap.py) | $O(1)$ | $O(1)$ | Math | - | - |
| 838 | [Push Dominoes](https://leetcode.com/problems/push-dominoes/) | [Python](Python/Push%20Dominoes.py) | $O(n)$ | $O(n)$ | - | - | - |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | [Python](Python/Backspace%20String%20Compare.py) | $O(min(n,m))$ | $O(1)$ | - | - | - |
| 847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | [Python](Python/Shortest%20Path%20Visiting%20All%20Nodes.py) | $O(n^{2}*2^{n})$ | $O(n*2^{n})$ | BFS | - | - |
| 860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) | [Python](Python/Lemonade%20Change.py), [Java](Java/Lemonade%20Change.java) | $O(n)$ | $O(1)$ | - | - | - |
| 867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | [Python](Python/Transpose%20Matrix.py), [Java](Java/Transpose%20Matrix.java) | $O(n*m)$ | $O(1)$ | - | - | - |
| 869 | [Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/) | [Python](Python/Reordered%20Power%20of%202.py) | $O({\log_{2} n}^{2})$ | $O(\log_{2} n)$ | - | - | - |
| 871 | [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | [Python](Python/Minimum%20Number%20of%20Refueling%20Stops.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 872 | [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | [Python](Python/Leaf-Similar%20Trees.py) | $O(H)$ | $O(H)$ | - | 91.29% | 87.58% |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | [Python](Python/Koko%20Eating%20Bananas.py) | $O(n * \log_{2} M)$ | $O(1)$ | Binary Search | 98.57% | 62.98% |
| 890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | [Python](Python/Find%20and%20Replace%20Pattern.py) | $O(n*k)$ | $O(k)$ | - | - | - |
| 896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) | [Python](Python/Monotonic%20Array.py) | $O(n)$ | $O(1)$ | - | 98.61% | 94.23% |
| 925 | [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/) | [Python](Python/Long%20Pressed%20Name.py), [Java](Java/Long%20Pressed%20Name.java) | $O(max(n,m))$ | $O(1)$ | - | - | - |
| 936 | [Stamping The Sequence](https://leetcode.com/problems/stamping-the-sequence/) | [Python](Python/Stamping%20The%20Sequence.py) | $O(m*(m-n))$ | $O(m*(m-n))$ | - | - | - |
| 944 | [Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/) | [Python](Python/Delete%20Columns%20to%20Make%20Sorted.py) | $O(m * n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 954 | [Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/) | [Python](Python/Array%20of%20Doubled%20Pairs.py) | - | - | - | - | - |
| 959 | [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | [Python](Python/Regions%20Cut%20By%20Slashes.py) | $O(n*m)$ | $O(n*m)$ | DFS | - | - |
| 967 | [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | [Python](Python/Numbers%20With%20Same%20Consecutive%20Differences.py) | $O(2^{n})$ | $O(2^{n})$ | DFS | - | - |
| 980 | [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) | [Python](Python/Unique%20Paths%20III.py) | - | - | - | - | - |
| 982 | [Triples with Bitwise AND Equal To Zero](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/) | [Python](Python/Triples%20with%20Bitwise%20AND%20Equal%20To%20Zero.py) | $O(n^{3})$ | $O(n^{2})$ | - | - | - |
| 990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Python](Python/Satisfiability%20of%20Equality%20Equations.py) | $O(n)$ | $O(n)$ | - | - | - |
| 998 | [Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/) | [Python](Python/Maximum%20Binary%20Tree%20II.py) | $O(n)$ | $O(n)$ | - | - | - |
| 1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) | [Python](Python/Minimum%20Domino%20Rotations%20For%20Equal%20Row.py) | $O(n)$ | $O(1)$ | - | - | - |
| 1010 | [Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | [Python](Python/Pairs%20of%20Songs%20With%20Total%20Durations%20Divisible%20by%2060.py), [Java](Java/Pairs%20of%20Songs%20With%20Total%20Durations%20Divisible%20by%2060.java) | $O(n)$ | $O(1)$ | - | 96.43% | 85.53% |
| 1026 | [Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) | [Python](Python/Maximum%20Difference%20Between%20Node%20and%20Ancestor.py) | $O(n)$ | $O(n)$ | - | - | - |
| 1030 | [Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/) | [Python](Python/Matrix%20Cells%20in%20Distance%20Order.py) | - | - | - | - | - |
| 1039 | [Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | [Python](Python/Minimum%20Score%20Triangulation%20of%20Polygon.py) | $O(n^{2})$ | $O(n^{2})$ | DP | - | - |
| 1047 | [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | [Python](Python/Remove%20All%20Adjacent%20Duplicates%20In%20String.py) | $O(n)$ | $O(n)$ | Stack | - | - |
| 1084 | [Sales Analysis III](https://leetcode.com/problems/sales-analysis-iii/) | [SQL](SQL/Sales%20Analysis%20III.sql) | SQL | SQL | - | - | - |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [Python](Python/Shortest%20Path%20in%20Binary%20Matrix.py) | $O(n^{2})$ | $O(n^{2})$ | BFS | - | - |
| 1104 | [Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/) | [Python](Python/Path%20In%20Zigzag%20Labelled%20Binary%20Tree.py) | $O(\log_{2} n)$ | $O(1)$ | - | 67.53% | 73.43% |
| 1137 | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | [Python](Python/N-th%20Tribonacci%20Number.py) | $O(n)$ | $O(1)$ | - | - | - |
| 1141 | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | [SQL](SQL/User%20Activity%20for%20the%20Past%2030%20Days%20I.sql) | SQL | SQL | - | - | - |
| 1155 | [Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) | [Python](Python/Number%20of%20Dice%20Rolls%20With%20Target%20Sum.py) | $O(n*k)$ | $O(n*k)$ | DP | - | - |
| 1162 | [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) | [Python](Python/As%20Far%20from%20Land%20as%20Possible.py) | $O(n*m)$ | $O(n*m)$ | - | - | - |
| 1237 | [Find Positive Integer Solution for a Given Equation](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/) | [Python](Python/Find%20Positive%20Integer%20Solution%20for%20a%20Given%20Equation.py) | $O(N + M)$ | $O(1)$ | - | 100.00% | 33.63% |
| 1239 | [Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) | [Python](Python/Maximum%20Length%20of%20a%20Concatenated%20String%20with%20Unique%20Characters.py) | $O(n^{2})$ | $O(n^{2})$ | DP | 94.14% | 8.30% |
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | [Python](Python/Number%20of%20Closed%20Islands.py) | $O(n*m)$ | $O(n*m)$ | DFS | - | - |
| 1260 | [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/) | [Python](Python/Shift%202D%20Grid.py) | $O(n^{2})$ | $O(n^{2})$ | - | - | - |
| 1323 | [Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/) | [Python](Python/Maximum%2069%20Number.py) | $O(n)$ | $O(n)$ | - | - | - |
| 1328 | [Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/) | [Python](Python/Break%20a%20Palindrome.py) | $O(n)$ | $O(n)$ | - | - | - |
| 1331 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | [Python](Python/Rank%20Transform%20of%20an%20Array.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 1332 | [Remove Palindromic Subsequences](https://leetcode.com/problems/remove-palindromic-subsequences/) | [Python](Python/Remove%20Palindromic%20Subsequences.py), [Java](Java/Remove%20Palindromic%20Subsequences.java) | $O(n)$ | $O(1)$ | - | - | - |
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | [Python](Python/Reduce%20Array%20Size%20to%20The%20Half.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 1345 | [Jump Game IV](https://leetcode.com/problems/jump-game-iv/) | [Python](Python/Jump%20Game%20IV.py) | - | - | - | - | - |
| 1376 | [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [Python](Python/Time%20Needed%20to%20Inform%20All%20Employees.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | [Python](Python/Design%20a%20Stack%20With%20Increment%20Operation.py) | - | - | - | - | - |
| 1383 | [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) | [Python](Python/Maximum%20Performance%20of%20a%20Team.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 1387 | [Sort Integers by The Power Value](https://leetcode.com/problems/sort-integers-by-the-power-value/) | [Python](Python/Sort%20Integers%20by%20The%20Power%20Value.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 1408 | [String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/) | [Python](Python/String%20Matching%20in%20an%20Array.py) | $O(n^{2}*k^{2})$ | $O(1)$ | - | - | - |
| 1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | [Python](Python/Maximum%20Points%20You%20Can%20Obtain%20from%20Cards.py) | $O(n)$ | $O(1)$ | Sliding Window | - | - |
| 1466 | [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [Python](Python/Reorder%20Routes%20to%20Make%20All%20Paths%20Lead%20to%20the%20City%20Zero.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | [Python](Python/Shuffle%20the%20Array.py), [Java](Java/Shuffle%20the%20Array.java) | $O(n)$ | $O(1)$ | - | - | - |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) | [Python](Python/Design%20Browser%20History.py) | - | - | - | - | - |
| 1484 | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) | [SQL](SQL/Group%20Sold%20Products%20By%20The%20Date.sql) | SQL | SQL | - | - | - |
| 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | [Python](Python/Longest%20Subarray%20of%201's%20After%20Deleting%20One%20Element.py), [Java](Java/Longest%20Subarray%20of%201's%20After%20Deleting%20One%20Element.java) | $O(n)$ | $O(1)$ | - | - | - |
| 1496 | [Path Crossing](https://leetcode.com/problems/path-crossing/) | [Python](Python/Path%20Crossing.py) | $O(n)$ | $O(n)$ | - | - | - |
| 1523 | [Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | [Python](Python/Count%20Odd%20Numbers%20in%20an%20Interval%20Range.py) | - | - | - | - | - |
| 1578 | [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) | [Python](Python/Minimum%20Time%20to%20Make%20Rope%20Colorful.py) | $O(n)$ | $O(1)$ | - | - | - |
| 1581 | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) | [SQL](SQL/Customer%20Who%20Visited%20but%20Did%20Not%20Make%20Any%20Transactions.sql) | SQL | SQL | - | - | - |
| 1657 | [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/) | [Python](Python/Determine%20if%20Two%20Strings%20Are%20Close.py) | $O(n)$ | $O(n)$ | Sorting | 89.60% | 94.00% |
| 1667 | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) | [SQL](SQL/Fix%20Names%20in%20a%20Table.sql) | SQL | SQL | - | - | - |
| 1669 | [Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/) | [Python](Python/Merge%20In%20Between%20Linked%20Lists.py) | $O(n + m)$ | $O(1)$ | - | - | - |
| 1680 | [Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/) | [Python](Python/Concatenation%20of%20Consecutive%20Binary%20Numbers.py) | $O(n*\log_{2} n)$ | $O(1)$ | - | - | - |
| 1693 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/) | [SQL](SQL/Daily%20Leads%20and%20Partners.sql) | SQL | SQL | - | - | - |
| 1752 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) | [Python](Python/Check%20if%20Array%20Is%20Sorted%20and%20Rotated.py) | $O(n)$ | $O(1)$ | - | - | - |
| 1757 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | [SQL](SQL/Recyclable%20and%20Low%20Fat%20Products.sql) | SQL | SQL | - | - | - |
| 1770 | [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) | [Python](Python/Maximum%20Score%20from%20Performing%20Multiplication%20Operations.py) | $O(m^{2})$ | $O(m)$ | DP | - | - |
| 1795 | [Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/) | [SQL](SQL/Rearrange%20Products%20Table.sql) | SQL | SQL | - | - | - |
| 1817 | [Finding the Users Active Minutes](https://leetcode.com/problems/finding-the-users-active-minutes/) | [Python](Python/Finding%20the%20Users%20Active%20Minutes.py) | $O(n)$ | $O(n + k)$ | Hashing | - | - |
| 1832 | [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) | [Python](Python/Check%20if%20the%20Sentence%20Is%20Pangram.py), [Java](Java/Check%20if%20the%20Sentence%20Is%20Pangram.java) | $O(n)$ | $O(1)$ | - | 92.75% | 95.79% |
| 1848 | [Minimum Distance to the Target Element](https://leetcode.com/problems/minimum-distance-to-the-target-element/) | [Python](Python/Minimum%20Distance%20to%20the%20Target%20Element.py) | $O(n)$ | $O(1)$ | - | - | - |
| 1869 | [Longer Contiguous Segments of Ones than Zeros](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/) | [Python](Python/Longer%20Contiguous%20Segments%20of%20Ones%20than%20Zeros.py) | - | - | - | - | - |
| 1873 | [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/) | [SQL](SQL/Calculate%20Special%20Bonus.sql) | SQL | SQL | - | - | - |
| 1890 | [The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020/) | [SQL](SQL/The%20Latest%20Login%20in%202020.sql) | SQL | SQL | - | - | - |
| 1945 | [Sum of Digits of String After Convert](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/) | [Python](Python/Sum%20of%20Digits%20of%20String%20After%20Convert.py) | $O(n)$ | $O(n)$ | - | - | - |
| 1979 | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | [Python](Python/Find%20Greatest%20Common%20Divisor%20of%20Array.py), [Java](Java/Find%20Greatest%20Common%20Divisor%20of%20Array.java) | $O(n)$ | $O(1)$ | GCD | - | - |
| 2007 | [Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) | [Python](Python/Find%20Original%20Array%20From%20Doubled%20Array.py), [Java](Java/Find%20Original%20Array%20From%20Doubled%20Array.java) | $O(n+k*\log_{2}k)$ | $O(k)$ | - | - | - |
| 2022 | [Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | [Python](Python/Convert%201D%20Array%20Into%202D%20Array.py), [Java](Java/Convert%201D%20Array%20Into%202D%20Array.java) | $O(n*m)$ | $O(1)$ | - | - | - |
| 2095 | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) | [Python](Python/Delete%20the%20Middle%20Node%20of%20a%20Linked%20List.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2131 | [Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/) | [Python](Python/Longest%20Palindrome%20by%20Concatenating%20Two%20Letter%20Words.py) | - | - | - | - | - |
| 2136 | [Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/) | [Python](Python/Earliest%20Possible%20Day%20of%20Full%20Bloom.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 2186 | [Minimum Number of Steps to Make Two Strings Anagram II](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/) | [Python](Python/Minimum%20Number%20of%20Steps%20to%20Make%20Two%20Strings%20Anagram%20II.py) | $O(n+m)$ | $O(n+m)$ | - | - | - |
| 2243 | [Calculate Digit Sum of a String](https://leetcode.com/problems/calculate-digit-sum-of-a-string/) | [Python](Python/Calculate%20Digit%20Sum%20of%20a%20String.py) | $O(\log_{k} n)$ | $O(\log_{k} n)$ | - | - | - |
| 2255 | [Count Prefixes of a Given String](https://leetcode.com/problems/count-prefixes-of-a-given-string/) | [Python](Python/Count%20Prefixes%20of%20a%20Given%20String.py) | $O(n*m)$ | $O(n*m)$ | - | - | - |
| 2264 | [Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string/) | [Python](Python/Largest%203-Same-Digit%20Number%20in%20String.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2269 | [Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | [Python](Python/Find%20the%20K-Beauty%20of%20a%20Number.py) | $O(\log_{10} n)$ | $O(1)$ | - | - | - |
| 2278 | [Percentage of Letter in String](https://leetcode.com/problems/percentage-of-letter-in-string/) | [Python](Python/Percentage%20of%20Letter%20in%20String.py), [Java](Java/Percentage%20of%20Letter%20in%20String.java) | $O(n)$ | $O(1)$ | - | - | - |
| 2315 | [Count Asterisks](https://leetcode.com/problems/count-asterisks/) | [Python](Python/Count%20Asterisks.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2331 | [Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree/) | [Python](Python/Evaluate%20Boolean%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2337 | [Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) | [Python](Python/Move%20Pieces%20to%20Obtain%20a%20String.py), [Java](Java/Move%20Pieces%20to%20Obtain%20a%20String.java) | $O(n)$ | $O(1)$ | Two Pointers | 86.68% | 99.25% |
| 2341 | [Maximum Number of Pairs in Array](https://leetcode.com/problems/maximum-number-of-pairs-in-array/) | [Python](Python/Maximum%20Number%20of%20Pairs%20in%20Array.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2347 | [Best Poker Hand](https://leetcode.com/problems/best-poker-hand/) | [Python](Python/Best%20Poker%20Hand.py) | $O(1)$ | $O(1)$ | - | - | - |
| 2352 | [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) | [Python](Python/Equal%20Row%20and%20Column%20Pairs.py) | $O(n^{3}) / O(n^{2})$ | $O(1) / O(n)$ | - | - | - |
| 2357 | [Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) | [Python](Python/Make%20Array%20Zero%20by%20Subtracting%20Equal%20Amounts.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2359 | [Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/) | [Python](Python/Find%20Closest%20Node%20to%20Given%20Two%20Nodes.py) | $O(n)$ | $O(n)$ | DFS | - | - |
| 2363 | [Merge Similar Items](https://leetcode.com/problems/merge-similar-items/) | [Python](Python/Merge%20Similar%20Items.py) | $O(n*\log_{2} n)$ | $O(n)$ | - | - | - |
| 2364 | [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/) | [Python](Python/Count%20Number%20of%20Bad%20Pairs.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2367 | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) | [Python](Python/Number%20of%20Arithmetic%20Triplets.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2374 | [Node With Highest Edge Score](https://leetcode.com/problems/node-with-highest-edge-score/) | [Python](Python/Node%20With%20Highest%20Edge%20Score.py) | $O(n)$ | $O(n)$ | - | - | - |
| 2384 | [Largest Palindromic Number](https://leetcode.com/problems/largest-palindromic-number/) | [Python](Python/Largest%20Palindromic%20Number.py) | $O(1)$ | $O(1)$ | - | - | - |
| 2390 | [Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/) | [Python](Python/Removing%20Stars%20From%20a%20String.py) | - | - | - | - | - |
| 2391 | [Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/) | [Python](Python/Minimum%20Amount%20of%20Time%20to%20Collect%20Garbage.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2399 | [Check Distances Between Same Letters](https://leetcode.com/problems/check-distances-between-same-letters/) | [Python](Python/Check%20Distances%20Between%20Same%20Letters.py) | $O(1)$ | $O(1)$ | - | - | - |
| 2404 | [Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/) | [Python](Python/Most%20Frequent%20Even%20Element.py), [Java](Java/Most%20Frequent%20Even%20Element.java) | $O(n)$ | $O(n)$ | - | - | - |
| 2413 | [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | [Python](Python/Smallest%20Even%20Multiple.py), [Java](Java/Smallest%20Even%20Multiple.java) | $O(1)$ | $O(1)$ | - | - | - |
| 2414 | [Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) | [Python](Python/Length%20of%20the%20Longest%20Alphabetical%20Continuous%20Substring.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2418 | [Sort the People](https://leetcode.com/problems/sort-the-people/) | [Python](Python/Sort%20the%20People.py) | $O(n * \log_{2} n)$ | $O(n)$ | - | - | - |
| 2419 | [Longest Subarray With Maximum Bitwise AND](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) | [Python](Python/Longest%20Subarray%20With%20Maximum%20Bitwise%20AND.py) | $O(n)$ | $O(1)$ | - | - | - |
| 2428 | [Maximum Sum of an Hourglass](https://leetcode.com/problems/maximum-sum-of-an-hourglass/) | [Python](Python/Maximum%20Sum%20of%20an%20Hourglass.py) | $O(n*m)$ | $O(n*m)$ | - | - | - |
| 2442 | [Count Number of Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) | [Python](Python/Count%20Number%20of%20Distinct%20Integers%20After%20Reverse%20Operations.py), [Java](Java/Count%20Number%20of%20Distinct%20Integers%20After%20Reverse%20Operations.java) | $O(n)$ | $O(n)$ | - | 99.69% | 96.65% |
| 2446 | [Determine if Two Events Have Conflict](https://leetcode.com/problems/determine-if-two-events-have-conflict/) | [Python](Python/Determine%20if%20Two%20Events%20Have%20Conflict.py) | $O(1)$ | $O(1)$ | - | 89.91% | 75.19% |
| 2448 | [Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/) | [Python](Python/Minimum%20Cost%20to%20Make%20Array%20Equal.py), [Java](Java/Minimum%20Cost%20to%20Make%20Array%20Equal.java) | $O(n * \log_{2} m)$ | $O(1)$ | Binary Search | 99.41% | 98.81% |
| 2455 | [Average Value of Even Numbers That Are Divisible by Three](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/) | [Python](Python/Average%20Value%20of%20Even%20Numbers%20That%20Are%20Divisible%20by%20Three.py) | $O(n)$ | $O(1)$ | - | 100.00% | 85.71% |
| 2485 | [Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer/) | [Python](Python/Find%20the%20Pivot%20Integer.py) | $O(√n)$ | $O(1)$ | Math | 99.78% | 97.40% |
| 2487 | [Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/) | [Python](Python/Remove%20Nodes%20From%20Linked%20List.py) | - | - | - | - | - |
| 2491 | [Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) | [Python](Python/Divide%20Players%20Into%20Teams%20of%20Equal%20Skill.py) | - | - | - | - | - |
| 2501 | [Longest Square Streak in an Array](https://leetcode.com/problems/longest-square-streak-in-an-array/) | [Python](Python/Longest%20Square%20Streak%20in%20an%20Array.py) | $O(n * √n)$ | $O(n)$ | - | - | - |
| 2506 | [Count Pairs Of Similar Strings](https://leetcode.com/problems/count-pairs-of-similar-strings/) | [Python](Python/Count%20Pairs%20Of%20Similar%20Strings.py) | $O(n*m)$ | $O(1)$ | - | - | - |
| 2522 | [Partition String Into Substrings With Values at Most K](https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/) | [Python](Python/Partition%20String%20Into%20Substrings%20With%20Values%20at%20Most%20K.py) | - | - | - | - | - |
| 2525 | [Categorize Box According to Criteria](https://leetcode.com/problems/categorize-box-according-to-criteria/) | [Python](Python/Categorize%20Box%20According%20to%20Criteria.py) | $O(1)$ | $O(1)$ | - | - | - |
| 2529 | [Maximum Count of Positive Integer and Negative Integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) | [Python](Python/Maximum%20Count%20of%20Positive%20Integer%20and%20Negative%20Integer.py) | $O(\log_{2} n)$ | $O(1)$ | - | - | - |
| 2549 | [Count Distinct Numbers on Board](https://leetcode.com/problems/count-distinct-numbers-on-board/) | [Python](Python/Count%20Distinct%20Numbers%20on%20Board.py) | - | - | - | - | - |
| 2574 | [Left and Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/) | [Python](Python/Left%20and%20Right%20Sum%20Differences.py) | - | - | - | - | - |

## Last update

Solution table for problems was generated automatically on 2024-03-09 06:08 +0000

