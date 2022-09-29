
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

| № | Title | Solutions | Time | Memory | Difficulty | Notes |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](Python/Two%20Sum.py), [Java](Java/Two%20Sum.java) | $O(n)$ | $O(n)$ | Easy | - |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python](Python/Add%20Two%20Numbers.py) | $O(n+m)$ | $O(1)$ | Medium | - |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](Python/Longest%20Substring%20Without%20Repeating%20Characters.py), [Java](Java/Longest%20Substring%20Without%20Repeating%20Characters.java) | $O(n)$ | $O(1)$ | Medium | - |
| 6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python](Python/Zigzag%20Conversion.py) | $O(n)$ | $O(n)$ | Medium | - |
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](Python/String%20to%20Integer%20(atoi).py) | $O(n)$ | $O(n)$ | Medium | RegEx |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Python](Python/Palindrome%20Number.py) | $O(\log_{10} n)$ | $O(1)$ | Easy | - |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | [Python](Python/Regular%20Expression%20Matching.py) | $O(n*m)$ | $O(n*m)$ | Hard | DP |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Python](Python/Container%20With%20Most%20Water.py) | $O(n)$ | $O(1)$ | Medium | - |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Python](Python/Integer%20to%20Roman.py) | $O(1)$ | $O(1)$ | Medium | - |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python](Python/Roman%20to%20Integer.py) | $O(1)$ | $O(1)$ | Easy | - |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [Python](Python/Longest%20Common%20Prefix.py) | $O(n)$ | $O(1)$ | Easy | - |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](Python/3Sum.py) | $O(n^{2})$ | $O(1)$ | Medium | Two Pointers |
| 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Python](Python/Remove%20Nth%20Node%20From%20End%20of%20List.py), [Java](Java/Remove%20Nth%20Node%20From%20End%20of%20List.java) | $O(n)$ | $O(1)$ | Medium | - |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python](Python/Valid%20Parentheses.py) | $O(n)$ | $O(n)$ | Easy | Stack |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | [Python](Python/Generate%20Parentheses.py), [Java](Java/Generate%20Parentheses.java) | $O(2^{n})$ | $O(n)$ | Medium | - |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Python](Python/Remove%20Duplicates%20from%20Sorted%20Array.py), [Java](Java/Remove%20Duplicates%20from%20Sorted%20Array.java) | $O(n)$ | $O(1)$ | Easy | - |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | [Python](Python/Remove%20Element.py), [Java](Java/Remove%20Element.java) | $O(n)$ | $O(1)$ | Easy | - |
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | [Python](Python/Substring%20with%20Concatenation%20of%20All%20Words.py) | $O(n*k)$ | $O(m*k)$ | Hard | - |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | [Python](Python/Valid%20Sudoku.py) | $O(n^{2})$ | $O(n^{2})$ | Medium | - |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [Python](Python/Trapping%20Rain%20Water.py) | $O(n)$ | $O(n)$ | Hard | - |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | [Python](Python/Rotate%20Image.py) | $O(n^{2})$ | $O(1)$ | Medium | - |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python](Python/Group%20Anagrams.py) | $O(n * m * \log_{2} m)$ | $O(n * m)$ | Medium | - |
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | [Python](Python/Pow(x,%20n).py) | $O(\log_{2} n)$ | $O(\log_{2} n)$ | Medium | BinPow |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](Python/Maximum%20Subarray.py), [Java](Java/Maximum%20Subarray.java) | $O(n)$ | $O(1)$ | Medium | Kadane's |
| 61 | [Rotate List](https://leetcode.com/problems/rotate-list/) | [Python](Python/Rotate%20List.py) | $O(n)$ | $O(1)$ | Medium | - |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | [Python](Python/Unique%20Paths.py) | $O(n*m)$ | $O(n*m)$ | Medium | DP |
| 68 | [Text Justification](https://leetcode.com/problems/text-justification/) | [Python](Python/Text%20Justification.py) | $O(n)$ | $O(n)$ | Hard | - |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | [Python](Python/Simplify%20Path.py) | $O(n)$ | $O(n)$ | Medium | - |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | [Python](Python/Set%20Matrix%20Zeroes.py) | $O(n*m)$ | $O(n+m)$ | Medium | - |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | [Python](Python/Subsets.py) | $O(2^{n})$ | $O(n)$ | Medium | - |
| 80 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | [Python](Python/Remove%20Duplicates%20from%20Sorted%20Array%20II.py) | $O(n)$ | $O(1)$ | Medium | - |
| 86 | [Partition List](https://leetcode.com/problems/partition-list/) | [Python](Python/Partition%20List.py) | $O(n)$ | $O(1)$ | Medium | - |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | [Python](Python/Merge%20Sorted%20Array.py), [Java](Java/Merge%20Sorted%20Array.java) | $O(n+m)$ | $O(1)$ | Easy | - |
| 89 | [Gray Code](https://leetcode.com/problems/gray-code/) | [Python](Python/Gray%20Code.py) | $O(2^{n})$ | $O(1)$ | Medium | - |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [Python](Python/Binary%20Tree%20Inorder%20Traversal.py) | $O(n)$ | $O(n)$ | Easy | - |
| 95 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | [Python](Python/Unique%20Binary%20Search%20Trees%20II.py) | $O(n^{2})$ | $O(\log_{2} n)$ | Medium | - |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | [Python](Python/Unique%20Binary%20Search%20Trees.py) | $O(n)$ | $O(1)$ | Medium | - |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python](Python/Validate%20Binary%20Search%20Tree.py) | $O(n)$ | $O(n)$ | Medium | DFS |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python](Python/Maximum%20Depth%20of%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Easy | DFS |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | [Python](Python/Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree.py) | $O(n)$ | $O(\log_{2} n)$ | Easy | - |
| 109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | [Python](Python/Convert%20Sorted%20List%20to%20Binary%20Search%20Tree.py) | $O(n*\log_{2} n)$ | $O(\log_{2} n)$ | Medium | DFS |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Python](Python/Minimum%20Depth%20of%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Easy | - |
| 113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | [Python](Python/Path%20Sum%20II.py) | - | - | Medium | - |
| 114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | [Python](Python/Flatten%20Binary%20Tree%20to%20Linked%20List.py) | $O(n)$ | $O(1)$ | Medium | - |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Python](Python/Binary%20Tree%20Maximum%20Path%20Sum.py) | $O(n)$ | $O(n)$ | Hard | - |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](Python/Valid%20Palindrome.py), [Java](Java/Valid%20Palindrome.java) | $O(n)$ | $O(1)$ | Easy | - |
| 126 | [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) | [Python](Python/Word%20Ladder%20II.py) | - | - | Hard | - |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | [Python](Python/Word%20Ladder.py) | - | - | Hard | - |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | [Python](Python/Single%20Number.py) | $O(n)$ | $O(1)$ | Easy | - |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](Python/Linked%20List%20Cycle.py) | $O(n)$ | $O(1)$ | Easy | - |
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Python](Python/Evaluate%20Reverse%20Polish%20Notation.py) | $O(n)$ | $O(n)$ | Medium | - |
| 151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [Python](Python/Reverse%20Words%20in%20a%20String.py) | $O(n)$ | $O(n)$ | Medium | - |
| 165 | [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) | [Python](Python/Compare%20Version%20Numbers.py) | $O(max(n,m))$ | $O(n+m)$ | Medium | - |
| 168 | [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/) | [Python](Python/Excel%20Sheet%20Column%20Title.py) | $O(\log_{26} n)$ | $O(1)$ | Easy | - |
| 172 | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) | [Python](Python/Factorial%20Trailing%20Zeroes.py) | $O(\log_{5} n)$ | $O(\log_{5} n)$ | Medium | - |
| 175 | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | [SQL](SQL/Combine%20Two%20Tables.sql) | SQL | SQL | Easy | - |
| 176 | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | [SQL](SQL/Second%20Highest%20Salary.sql) | SQL | SQL | Medium | - |
| 177 | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | [SQL](SQL/Nth%20Highest%20Salary.sql) | SQL | SQL | Medium | - |
| 178 | [Rank Scores](https://leetcode.com/problems/rank-scores/) | [SQL](SQL/Rank%20Scores.sql) | SQL | SQL | Medium | - |
| 180 | [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) | [SQL](SQL/Consecutive%20Numbers.sql) | SQL | SQL | Medium | - |
| 181 | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | [SQL](SQL/Employees%20Earning%20More%20Than%20Their%20Managers.sql) | SQL | SQL | Easy | - |
| 182 | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | [SQL](SQL/Duplicate%20Emails.sql) | SQL | SQL | Easy | - |
| 183 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | [SQL](SQL/Customers%20Who%20Never%20Order.sql) | SQL | SQL | Easy | - |
| 184 | [Department Highest Salary](https://leetcode.com/problems/department-highest-salary/) | [SQL](SQL/Department%20Highest%20Salary.sql) | SQL | SQL | Medium | - |
| 185 | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | [SQL](SQL/Department%20Top%20Three%20Salaries.sql) | SQL | SQL | Hard | - |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | [Python](Python/Reverse%20Bits.py), [Java](Java/Reverse%20Bits.java) | $O(1)$ | $O(1)$ | Easy | - |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | [Python](Python/Number%20of%201%20Bits.py) | $O(\log_{10} n)$ | $O(1)$ | Easy | - |
| 192 | [Word Frequency](https://leetcode.com/problems/word-frequency/) | [Shell](Shell/Word%20Frequency.sh) | SHELL | SHELL | Medium | - |
| 193 | [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers/) | [Shell](Shell/Valid%20Phone%20Numbers.sh) | SHELL | SHELL | Easy | - |
| 194 | [Transpose File](https://leetcode.com/problems/transpose-file/) | [Shell](Shell/Transpose%20File.sh) | SHELL | SHELL | Medium | - |
| 195 | [Tenth Line](https://leetcode.com/problems/tenth-line/) | [Shell](Shell/Tenth%20Line.sh) | SHELL | SHELL | Easy | - |
| 196 | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) | [SQL](SQL/Delete%20Duplicate%20Emails.sql) | SQL | SQL | Easy | - |
| 197 | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) | [SQL](SQL/Rising%20Temperature.sql) | SQL | SQL | Easy | - |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python](Python/Number%20of%20Islands.py), [Java](Java/Number%20of%20Islands.java) | $O(n*m)$ | $O(n*m)$ | Medium | DFS |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python](Python/Reverse%20Linked%20List.py) | $O(n)$ | $O(1)$ | Easy | - |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | [Python](Python/Minimum%20Size%20Subarray%20Sum.py), [Java](Java/Minimum%20Size%20Subarray%20Sum.java) | $O(n)$ | $O(1)$ | Medium | - |
| 219 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | [Python](Python/Contains%20Duplicate%20II.py) | $O(n)$ | $O(n)$ | Easy | - |
| 222 | [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | [Python](Python/Count%20Complete%20Tree%20Nodes.py) | $O(\log_{2}^{2} n)$ | $O(\log_{2} n)$ | Medium | - |
| 223 | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) | [Python](Python/Rectangle%20Area.py) | $O(1)$ | $O(1)$ | Medium | Math |
| 234 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | [Python](Python/Palindrome%20Linked%20List.py) | $O(n)$ | $O(1)$ | Easy | - |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Python](Python/Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.py) | $O(n)$ | $O(n)$ | Medium | - |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](Python/Valid%20Anagram.py) | $O(max(n,m))$ | $O(n+m)$ | Easy | - |
| 279 | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | [Python](Python/Perfect%20Squares.py) | $O(n*\sqrt{n})$ | $O(n)$ | Medium | - |
| 290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | [Python](Python/Word%20Pattern.py) | $O(n)$ | $O(n)$ | Easy | - |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [Python](Python/Serialize%20and%20Deserialize%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Hard | Preorder |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | [Python](Python/Longest%20Increasing%20Subsequence.py) | $O(n*\log_{2} n)$ | $O(n)$ | Medium | - |
| 304 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | [Python](Python/Range%20Sum%20Query%202D%20-%20Immutable.py) | $O(n*m) + O(1)$ | $O(n*m) + O(1)$ | Medium | - |
| 326 | [Power of Three](https://leetcode.com/problems/power-of-three/) | [Python](Python/Power%20of%20Three.py) | $O(1)$ | $O(1)$ | Easy | - |
| 336 | [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | [Python](Python/Palindrome%20Pairs.py) | $O(n*k^{2})$ | $O(n)$ | Hard | - |
| 342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | [Python](Python/Power%20of%20Four.py) | $O(1)$ | $O(1)$ | Easy | - |
| 377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | [Python](Python/Combination%20Sum%20IV.py) | $O(2^{n})$ | $O(n)$ | Medium | - |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | [Python](Python/Ransom%20Note.py) | $O(n+m)$ | $O(n+m)$ | Easy | - |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [Python](Python/First%20Unique%20Character%20in%20a%20String.py) | $O(n)$ | $O(1)$ | Easy | - |
| 390 | [Elimination Game](https://leetcode.com/problems/elimination-game/) | [Python](Python/Elimination%20Game.py), [Java](Java/Elimination%20Game.java) | $O(\log_{2} n)$ | $O(\log_{2} n)$ | Medium | - |
| 393 | [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) | [Python](Python/UTF-8%20Validation.py) | $O(n)$ | $O(1)$ | Medium | - |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Python](Python/Pacific%20Atlantic%20Water%20Flow.py) | $O(n*m)$ | $O(n*m)$ | Medium | DFS |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Python](Python/Longest%20Repeating%20Character%20Replacement.py) | $O(n)$ | $O(1)$ | Medium | - |
| 429 | [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [Python](Python/N-ary%20Tree%20Level%20Order%20Traversal.py) | $O(n)$ | $O(n)$ | Medium | - |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | [Python](Python/String%20Compression.py) | $O(n)$ | $O(1)$ | Medium | - |
| 463 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | [Python](Python/Island%20Perimeter.py) | $O(n*m)$ | $O(1)$ | Easy | - |
| 468 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) | [Python](Python/Validate%20IP%20Address.py) | $O(1)$ | $O(1)$ | Medium | RegEx |
| 491 | [Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences/) | [Python](Python/Increasing%20Subsequences.py) | $O(n^{2})$ | $O(n^{2})$ | Medium | - |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | [Python](Python/Target%20Sum.py) | $O(n*t)$ | $O(n*t)$ | Medium | - |
| 497 | [Random Point in Non-overlapping Rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/) | [Python](Python/Random%20Point%20in%20Non-overlapping%20Rectangles.py) | $O(n) + O(\log_{2} n)$ | $O(n) + O(1)$ | Medium | - |
| 506 | [Relative Ranks](https://leetcode.com/problems/relative-ranks/) | [Python](Python/Relative%20Ranks.py) | $O(n * \log_{2} n)$ | $O(n)$ | Easy | - |
| 508 | [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/) | [Python](Python/Most%20Frequent%20Subtree%20Sum.py) | $O(n)$ | $O(n)$ | Medium | - |
| 511 | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) | [SQL](SQL/Game%20Play%20Analysis%20I.sql) | SQL | SQL | Easy | - |
| 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [Python](Python/Diameter%20of%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Easy | - |
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | [Python](Python/Number%20of%20Provinces.py) | $O(n^{2})$ | $O(n)$ | Medium | DSU |
| 551 | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/) | [Python](Python/Student%20Attendance%20Record%20I.py), [Java](Java/Student%20Attendance%20Record%20I.java) | $O(n)$ | $O(1)$ | Easy | - |
| 557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | [Python](Python/Reverse%20Words%20in%20a%20String%20III.py), [Java](Java/Reverse%20Words%20in%20a%20String%20III.java) | $O(n)$ | $O(n)$ | Easy | - |
| 584 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | [SQL](SQL/Find%20Customer%20Referee.sql) | SQL | SQL | Easy | - |
| 586 | [Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) | [SQL](SQL/Customer%20Placing%20the%20Largest%20Number%20of%20Orders.sql) | SQL | SQL | Easy | - |
| 592 | [Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction/) | [Python](Python/Fraction%20Addition%20and%20Subtraction.py) | $O(n)$ | $O(n)$ | Medium | - |
| 595 | [Big Countries](https://leetcode.com/problems/big-countries/) | [SQL](SQL/Big%20Countries.sql) | SQL | SQL | Easy | - |
| 596 | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) | [SQL](SQL/Classes%20More%20Than%205%20Students.sql) | SQL | SQL | Easy | - |
| 598 | [Range Addition II](https://leetcode.com/problems/range-addition-ii/) | [Python](Python/Range%20Addition%20II.py), [Java](Java/Range%20Addition%20II.java) | $O(n)$ | $O(1)$ | Easy | - |
| 606 | [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/) | [Python](Python/Construct%20String%20from%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Easy | - |
| 607 | [Sales Person](https://leetcode.com/problems/sales-person/) | [SQL](SQL/Sales%20Person.sql) | SQL | SQL | Easy | - |
| 608 | [Tree Node](https://leetcode.com/problems/tree-node/) | [SQL](SQL/Tree%20Node.sql) | SQL | SQL | Medium | - |
| 609 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | [Python](Python/Find%20Duplicate%20File%20in%20System.py) | $O(n*k)$ | $O(n*k)$ | Medium | - |
| 620 | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) | [SQL](SQL/Not%20Boring%20Movies.sql) | SQL | SQL | Easy | - |
| 622 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | [Python](Python/Design%20Circular%20Queue.py) | $O(k) / O(1)$ | $O(k) / O(1)$ | Medium | - |
| 627 | [Swap Salary](https://leetcode.com/problems/swap-salary/) | [SQL](SQL/Swap%20Salary.sql) | SQL | SQL | Easy | - |
| 637 | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | [Python](Python/Average%20of%20Levels%20in%20Binary%20Tree.py) | $O(n)$ | $O(\log_{2} n)$ | Easy | - |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [Python](Python/Maximum%20Average%20Subarray%20I.py) | $O(n)$ | $O(1)$ | Easy | - |
| 658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | [Python](Python/Find%20K%20Closest%20Elements.py) | $O(k + \log_{2} n)$ | $O(1)$ | Medium | - |
| 659 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | [Python](Python/Split%20Array%20into%20Consecutive%20Subsequences.py) | $O(n)$ | $O(n)$ | Medium | - |
| 680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | [Python](Python/Valid%20Palindrome%20II.py) | $O(n)$ | $O(1)$ | Easy | - |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [Python](Python/Max%20Area%20of%20Island.py) | $O(n*m)$ | $O(n*m)$ | Medium | - |
| 700 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | [Python](Python/Search%20in%20a%20Binary%20Search%20Tree.py) | $O(n)$ | $O(1)$ | Easy | - |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | [Python](Python/Binary%20Search.py) | $O(\log_{2} n)$ | $O(1)$ | Easy | - |
| 718 | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | [Python](Python/Maximum%20Length%20of%20Repeated%20Subarray.py) | $O(n*m)$ | $O(n*m)$ | Medium | DP |
| 733 | [Flood Fill](https://leetcode.com/problems/flood-fill/) | [Python](Python/Flood%20Fill.py) | $O(n*m)$ | $O(n*m)$ | Easy | - |
| 747 | [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) | [Python](Python/Largest%20Number%20At%20Least%20Twice%20of%20Others.py) | $O(n)$ | $O(1)$ | Easy | - |
| 748 | [Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/) | [Python](Python/Shortest%20Completing%20Word.py) | $O(n^{2})$ | $O(n^{2})$ | Easy | - |
| 766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | [Python](Python/Toeplitz%20Matrix.py) | $O(n*m)$ | $O(1)$ | Easy | - |
| 788 | [Rotated Digits](https://leetcode.com/problems/rotated-digits/) | [Python](Python/Rotated%20Digits.py) | $O(n * \log_{10} n)$ | $O(\log_{10} n)$ | Medium | - |
| 797 | [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | [Python](Python/All%20Paths%20From%20Source%20to%20Target.py) | $O(n)$ | $O(n)$ | Medium | - |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | [Python](Python/Find%20Eventual%20Safe%20States.py) | $O(V+E)$ | $O(V)$ | Medium | - |
| 804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | [Python](Python/Unique%20Morse%20Code%20Words.py) | $O(n)$ | $O(n)$ | Easy | - |
| 814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | [Python](Python/Binary%20Tree%20Pruning.py) | $O(n)$ | $O(n)$ | Medium | - |
| 823 | [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/) | [Python](Python/Binary%20Trees%20With%20Factors.py) | $O(n^{2})$ | $O(n)$ | Medium | - |
| 836 | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) | [Python](Python/Rectangle%20Overlap.py) | $O(1)$ | $O(1)$ | Easy | Math |
| 838 | [Push Dominoes](https://leetcode.com/problems/push-dominoes/) | [Python](Python/Push%20Dominoes.py) | $O(n)$ | $O(n)$ | Medium | - |
| 841 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | [Python](Python/Keys%20and%20Rooms.py) | $O(n)$ | $O(n)$ | Medium | - |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | [Python](Python/Backspace%20String%20Compare.py) | $O(min(n,m))$ | $O(1)$ | Easy | - |
| 847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | [Python](Python/Shortest%20Path%20Visiting%20All%20Nodes.py) | $O(n^{2}*2^{n})$ | $O(n*2^{n})$ | Hard | - |
| 869 | [Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/) | [Python](Python/Reordered%20Power%20of%202.py) | $O({\log_{2} n}^{2})$ | $O(\log_{2} n)$ | Medium | - |
| 871 | [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | [Python](Python/Minimum%20Number%20of%20Refueling%20Stops.py) | $O(n * \log_{2} n)$ | $O(n)$ | Hard | - |
| 877 | [Stone Game](https://leetcode.com/problems/stone-game/) | [Python](Python/Stone%20Game.py), [Java](Java/Stone%20Game.java) | $O(1)$ | $O(1)$ | Medium | - |
| 890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | [Python](Python/Find%20and%20Replace%20Pattern.py) | $O(n*k)$ | $O(k)$ | Medium | - |
| 895 | [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) | [Python](Python/Maximum%20Frequency%20Stack.py) | $O(n)$ | $O(n)+O(1)$ | Hard | - |
| 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | [Python](Python/Fruit%20Into%20Baskets.py) | $O(n)$ | $O(k)$ | Medium | - |
| 923 | [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/) | [Python](Python/3Sum%20With%20Multiplicity.py) | $O(k^{2})$ | $O(k)$ | Medium | - |
| 925 | [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/) | [Python](Python/Long%20Pressed%20Name.py), [Java](Java/Long%20Pressed%20Name.java) | $O(max(n,m))$ | $O(1)$ | Easy | - |
| 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | [Python](Python/Binary%20Subarrays%20With%20Sum.py) | $O(n)$ | $O(n)$ | Medium | - |
| 936 | [Stamping The Sequence](https://leetcode.com/problems/stamping-the-sequence/) | [Python](Python/Stamping%20The%20Sequence.py) | $O(m*(m-n))$ | $O(m*(m-n))$ | Hard | - |
| 938 | [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | [Python](Python/Range%20Sum%20of%20BST.py) | $O(n)$ | $O(n)$ | Easy | DFS |
| 946 | [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) | [Python](Python/Validate%20Stack%20Sequences.py) | $O(n)$ | $O(n)$ | Medium | - |
| 948 | [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/) | [Python](Python/Bag%20of%20Tokens.py) | $O(n * \log_{2} n)$ | $O(1)$ | Medium | Two-pointer |
| 967 | [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | [Python](Python/Numbers%20With%20Same%20Consecutive%20Differences.py) | $O(2^{n})$ | $O(2^{n})$ | Medium | DFS |
| 977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | [Python](Python/Squares%20of%20a%20Sorted%20Array.py) | $O(n)$ | $O(n)$ | Easy | - |
| 982 | [Triples with Bitwise AND Equal To Zero](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/) | [Python](Python/Triples%20with%20Bitwise%20AND%20Equal%20To%20Zero.py) | $O(n^{3})$ | $O(n^{2})$ | Hard | - |
| 985 | [Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) | [Python](Python/Sum%20of%20Even%20Numbers%20After%20Queries.py), [Java](Java/Sum%20of%20Even%20Numbers%20After%20Queries.java) | $O(n + m)$ | $O(1)$ | Medium | - |
| 986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | [Python](Python/Interval%20List%20Intersections.py) | $O(n+m)$ | $O(n+m)$ | Medium | - |
| 990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Python](Python/Satisfiability%20of%20Equality%20Equations.py) | $O(n)$ | $O(n)$ | Medium | - |
| 997 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | [Python](Python/Find%20the%20Town%20Judge.py) | $O(n)$ | $O(n)$ | Easy | - |
| 998 | [Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/) | [Python](Python/Maximum%20Binary%20Tree%20II.py) | $O(n)$ | $O(n)$ | Medium | - |
| 1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) | [Python](Python/Minimum%20Domino%20Rotations%20For%20Equal%20Row.py) | $O(n)$ | $O(1)$ | Medium | - |
| 1020 | [Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) | [Python](Python/Number%20of%20Enclaves.py) | $O(n*m)$ | $O(n*m)$ | Medium | DFS |
| 1048 | [Longest String Chain](https://leetcode.com/problems/longest-string-chain/) | [Python](Python/Longest%20String%20Chain.py) | $O(n*k^{2})$ | $O(n)$ | Medium | - |
| 1050 | [Actors and Directors Who Cooperated At Least Three Times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/) | [SQL](SQL/Actors%20and%20Directors%20Who%20Cooperated%20At%20Least%20Three%20Times.sql) | SQL | SQL | Easy | - |
| 1071 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | [Python](Python/Greatest%20Common%20Divisor%20of%20Strings.py) | $O(n+m)$ | $O(n+m)$ | Easy | - |
| 1084 | [Sales Analysis III](https://leetcode.com/problems/sales-analysis-iii/) | [SQL](SQL/Sales%20Analysis%20III.sql) | SQL | SQL | Easy | - |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [Python](Python/Shortest%20Path%20in%20Binary%20Matrix.py) | $O(n^{2})$ | $O(n^{2})$ | Medium | BFS |
| 1114 | [Print in Order](https://leetcode.com/problems/print-in-order/) | [Python](Python/Print%20in%20Order.py) | CONCURRENCY | CONCURRENCY | Easy | - |
| 1137 | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | [Python](Python/N-th%20Tribonacci%20Number.py) | $O(n)$ | $O(1)$ | Easy | - |
| 1141 | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) | [SQL](SQL/User%20Activity%20for%20the%20Past%2030%20Days%20I.sql) | SQL | SQL | Easy | - |
| 1148 | [Article Views I](https://leetcode.com/problems/article-views-i/) | [SQL](SQL/Article%20Views%20I.sql) | SQL | SQL | Easy | - |
| 1158 | [Market Analysis I](https://leetcode.com/problems/market-analysis-i/) | [SQL](SQL/Market%20Analysis%20I.sql) | SQL | SQL | Medium | - |
| 1162 | [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) | [Python](Python/As%20Far%20from%20Land%20as%20Possible.py) | $O(n*m)$ | $O(n*m)$ | Medium | - |
| 1179 | [Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) | [SQL](SQL/Reformat%20Department%20Table.sql) | SQL | SQL | Easy | - |
| 1184 | [Distance Between Bus Stops](https://leetcode.com/problems/distance-between-bus-stops/) | [Python](Python/Distance%20Between%20Bus%20Stops.py) | $O(n)$ | $O(1)$ | Easy | - |
| 1220 | [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) | [Python](Python/Count%20Vowels%20Permutation.py) | $O(n)$ | $O(1)$ | Hard | DP |
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | [Python](Python/Number%20of%20Closed%20Islands.py) | $O(n*m)$ | $O(n*m)$ | Medium | DFS |
| 1260 | [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/) | [Python](Python/Shift%202D%20Grid.py) | $O(n^{2})$ | $O(n^{2})$ | Easy | - |
| 1319 | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | [Python](Python/Number%20of%20Operations%20to%20Make%20Network%20Connected.py) | $O(n)$ | $O(n)$ | Medium | - |
| 1329 | [Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/) | [Python](Python/Sort%20the%20Matrix%20Diagonally.py) | - | - | Medium | - |
| 1331 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | [Python](Python/Rank%20Transform%20of%20an%20Array.py) | $O(n * \log_{2} n)$ | $O(n)$ | Easy | - |
| 1332 | [Remove Palindromic Subsequences](https://leetcode.com/problems/remove-palindromic-subsequences/) | [Python](Python/Remove%20Palindromic%20Subsequences.py), [Java](Java/Remove%20Palindromic%20Subsequences.java) | $O(n)$ | $O(1)$ | Easy | - |
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | [Python](Python/Reduce%20Array%20Size%20to%20The%20Half.py) | $O(n * \log_{2} n)$ | $O(n)$ | Medium | - |
| 1347 | [Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) | [Python](Python/Minimum%20Number%20of%20Steps%20to%20Make%20Two%20Strings%20Anagram.py) | $O(n)$ | $O(1)$ | Medium | - |
| 1383 | [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) | [Python](Python/Maximum%20Performance%20of%20a%20Team.py) | $O(n * \log_{2} n)$ | $O(n)$ | Hard | - |
| 1393 | [Capital Gain/Loss](https://leetcode.com/problems/capital-gainloss/) |  | SQL | SQL | Medium | - |
| 1407 | [Top Travellers](https://leetcode.com/problems/top-travellers/) | [SQL](SQL/Top%20Travellers.sql) | SQL | SQL | Easy | - |
| 1408 | [String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/) | [Python](Python/String%20Matching%20in%20an%20Array.py) | $O(n^{2}*k^{2})$ | $O(1)$ | Easy | - |
| 1414 | [Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) | [Python](Python/Find%20the%20Minimum%20Number%20of%20Fibonacci%20Numbers%20Whose%20Sum%20Is%20K.py) | $O(\log_{2} k)$ | $O(\log_{2} k)$ | Medium | - |
| 1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | [Python](Python/Maximum%20Points%20You%20Can%20Obtain%20from%20Cards.py) | $O(n)$ | $O(1)$ | Medium | - |
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Python](Python/Count%20Good%20Nodes%20in%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Medium | DFS |
| 1457 | [Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/) | [Python](Python/Pseudo-Palindromic%20Paths%20in%20a%20Binary%20Tree.py), [Java](Java/Pseudo-Palindromic%20Paths%20in%20a%20Binary%20Tree.java) | $O(n)$ | $O(n)$ | Medium | - |
| 1466 | [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | [Python](Python/Reorder%20Routes%20to%20Make%20All%20Paths%20Lead%20to%20the%20City%20Zero.py) | $O(n)$ | $O(n)$ | Medium | - |
| 1470 | [Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/) | [Python](Python/Shuffle%20the%20Array.py), [Java](Java/Shuffle%20the%20Array.java) | $O(n)$ | $O(1)$ | Easy | - |
| 1484 | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) | [SQL](SQL/Group%20Sold%20Products%20By%20The%20Date.sql) | SQL | SQL | Easy | - |
| 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | [Python](Python/Longest%20Subarray%20of%201's%20After%20Deleting%20One%20Element.py), [Java](Java/Longest%20Subarray%20of%201's%20After%20Deleting%20One%20Element.java) | $O(n)$ | $O(1)$ | Medium | - |
| 1527 | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/) | [SQL](SQL/Patients%20With%20a%20Condition.sql) | SQL | SQL | Easy | - |
| 1557 | [Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) | [Python](Python/Minimum%20Number%20of%20Vertices%20to%20Reach%20All%20Nodes.py) | $O(n)$ | $O(n)$ | Medium | - |
| 1581 | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) | [SQL](SQL/Customer%20Who%20Visited%20but%20Did%20Not%20Make%20Any%20Transactions.sql) | SQL | SQL | Easy | - |
| 1587 | [Bank Account Summary II](https://leetcode.com/problems/bank-account-summary-ii/) | [SQL](SQL/Bank%20Account%20Summary%20II.sql) | SQL | SQL | Easy | - |
| 1663 | [Smallest String With A Given Numeric Value](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/) | [Python](Python/Smallest%20String%20With%20A%20Given%20Numeric%20Value.py) | $O(n)$ | $O(n)$ | Medium | - |
| 1667 | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) | [SQL](SQL/Fix%20Names%20in%20a%20Table.sql) | SQL | SQL | Easy | - |
| 1680 | [Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/) | [Python](Python/Concatenation%20of%20Consecutive%20Binary%20Numbers.py) | $O(n*\log_{2} n)$ | $O(1)$ | Medium | - |
| 1693 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/) | [SQL](SQL/Daily%20Leads%20and%20Partners.sql) | SQL | SQL | Easy | - |
| 1729 | [Find Followers Count](https://leetcode.com/problems/find-followers-count/) | [SQL](SQL/Find%20Followers%20Count.sql) | SQL | SQL | Easy | - |
| 1741 | [Find Total Time Spent by Each Employee](https://leetcode.com/problems/find-total-time-spent-by-each-employee/) | [SQL](SQL/Find%20Total%20Time%20Spent%20by%20Each%20Employee.sql) | SQL | SQL | Easy | - |
| 1757 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | [SQL](SQL/Recyclable%20and%20Low%20Fat%20Products.sql) | SQL | SQL | Easy | - |
| 1770 | [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) | [Python](Python/Maximum%20Score%20from%20Performing%20Multiplication%20Operations.py) | $O(m^{2})$ | $O(m)$ | Hard | DP |
| 1795 | [Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/) | [SQL](SQL/Rearrange%20Products%20Table.sql) | SQL | SQL | Easy | - |
| 1817 | [Finding the Users Active Minutes](https://leetcode.com/problems/finding-the-users-active-minutes/) | [Python](Python/Finding%20the%20Users%20Active%20Minutes.py) | $O(n)$ | $O(n+k)$ | Medium | - |
| 1839 | [Longest Substring Of All Vowels in Order](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/) | [Python](Python/Longest%20Substring%20Of%20All%20Vowels%20in%20Order.py) | $O(n)$ | $O(1)$ | Medium | - |
| 1873 | [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/) | [SQL](SQL/Calculate%20Special%20Bonus.sql) | SQL | SQL | Easy | - |
| 1876 | [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | [Python](Python/Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.py), [Java](Java/Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.java) | $O(n)$ | $O(min(n,k))$ | Easy | - |
| 1890 | [The Latest Login in 2020](https://leetcode.com/problems/the-latest-login-in-2020/) | [SQL](SQL/The%20Latest%20Login%20in%202020.sql) | SQL | SQL | Easy | - |
| 1905 | [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) | [Python](Python/Count%20Sub%20Islands.py) | $O(n^{2})$ | $O(n^{2})$ | Medium | - |
| 1965 | [Employees With Missing Information](https://leetcode.com/problems/employees-with-missing-information/) | [SQL](SQL/Employees%20With%20Missing%20Information.sql) | SQL | SQL | Easy | - |
| 1979 | [Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | [Python](Python/Find%20Greatest%20Common%20Divisor%20of%20Array.py), [Java](Java/Find%20Greatest%20Common%20Divisor%20of%20Array.java) | $O(n)$ | $O(1)$ | Easy | - |
| 1984 | [Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | [Python](Python/Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.py) | $O(n*\log_{2} n)$ | $O(1)$ | Easy | - |
| 1996 | [The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/) | [Python](Python/The%20Number%20of%20Weak%20Characters%20in%20the%20Game.py) | $O(n * \log_{2} n)$ | $O(n)$ | Medium | - |
| 2007 | [Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) | [Python](Python/Find%20Original%20Array%20From%20Doubled%20Array.py), [Java](Java/Find%20Original%20Array%20From%20Doubled%20Array.java) | $O(n+k*\log_{2}k)$ | $O(k)$ | Medium | - |
| 2243 | [Calculate Digit Sum of a String](https://leetcode.com/problems/calculate-digit-sum-of-a-string/) | [Python](Python/Calculate%20Digit%20Sum%20of%20a%20String.py) | $O(\log_{k} n)$ | $O(\log_{k} n)$ | Easy | - |
| 2269 | [Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | [Python](Python/Find%20the%20K-Beauty%20of%20a%20Number.py) | $O(\log_{10} n)$ | $O(1)$ | Easy | - |
| 2294 | [Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/) | [Python](Python/Partition%20Array%20Such%20That%20Maximum%20Difference%20Is%20K.py), [Java](Java/Partition%20Array%20Such%20That%20Maximum%20Difference%20Is%20K.java) | $O(n * \log_{2} n)$ | $O(1)$ | Medium | - |
| 2309 | [Greatest English Letter in Upper and Lower Case](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/) | [Python](Python/Greatest%20English%20Letter%20in%20Upper%20and%20Lower%20Case.py) | $O(1)$ | $O(1)$ | Easy | - |
| 2315 | [Count Asterisks](https://leetcode.com/problems/count-asterisks/) | [Python](Python/Count%20Asterisks.py) | $O(n)$ | $O(1)$ | Easy | - |
| 2316 | [Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) | [Python](Python/Count%20Unreachable%20Pairs%20of%20Nodes%20in%20an%20Undirected%20Graph.py) | $O(n)$ | $O(n)$ | Medium | - |
| 2331 | [Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree/) | [Python](Python/Evaluate%20Boolean%20Binary%20Tree.py) | $O(n)$ | $O(n)$ | Easy | - |
| 2335 | [Minimum Amount of Time to Fill Cups](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/) | [Python](Python/Minimum%20Amount%20of%20Time%20to%20Fill%20Cups.py) | $O(1)$ | $O(1)$ | Easy | - |
| 2341 | [Maximum Number of Pairs in Array](https://leetcode.com/problems/maximum-number-of-pairs-in-array/) | [Python](Python/Maximum%20Number%20of%20Pairs%20in%20Array.py) | $O(n)$ | $O(n)$ | Easy | - |
| 2347 | [Best Poker Hand](https://leetcode.com/problems/best-poker-hand/) | [Python](Python/Best%20Poker%20Hand.py) | $O(1)$ | $O(1)$ | Easy | - |
| 2351 | [First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) | [Python](Python/First%20Letter%20to%20Appear%20Twice.py) | $O(n)$ | $O(1)$ | Easy | - |
| 2357 | [Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) | [Python](Python/Make%20Array%20Zero%20by%20Subtracting%20Equal%20Amounts.py) | $O(n)$ | $O(n)$ | Easy | - |
| 2359 | [Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/) | [Python](Python/Find%20Closest%20Node%20to%20Given%20Two%20Nodes.py) | $O(n)$ | $O(n)$ | Medium | DFS |
| 2363 | [Merge Similar Items](https://leetcode.com/problems/merge-similar-items/) | [Python](Python/Merge%20Similar%20Items.py) | $O(n*\log_{2} n)$ | $O(n)$ | Easy | - |
| 2364 | [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/) | [Python](Python/Count%20Number%20of%20Bad%20Pairs.py) | $O(n)$ | $O(n)$ | Medium | - |
| 2367 | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) | [Python](Python/Number%20of%20Arithmetic%20Triplets.py) | $O(n)$ | $O(n)$ | Easy | - |
| 2373 | [Largest Local Values in a Matrix](https://leetcode.com/problems/largest-local-values-in-a-matrix/) | [Python](Python/Largest%20Local%20Values%20in%20a%20Matrix.py) | $O(n^{2})$ | $O(1)$ | Easy | - |
| 2374 | [Node With Highest Edge Score](https://leetcode.com/problems/node-with-highest-edge-score/) | [Python](Python/Node%20With%20Highest%20Edge%20Score.py) | $O(n)$ | $O(n)$ | Medium | - |
| 2379 | [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) | [Python](Python/Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks.py) | $O(n)$ | $O(k)$ | Easy | - |
| 2380 | [Time Needed to Rearrange a Binary String](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/) | [Python](Python/Time%20Needed%20to%20Rearrange%20a%20Binary%20String.py) | $O(n)$ | $O(1)$ | Medium | - |
| 2384 | [Largest Palindromic Number](https://leetcode.com/problems/largest-palindromic-number/) | [Python](Python/Largest%20Palindromic%20Number.py) | $O(1)$ | $O(1)$ | Medium | - |
| 2389 | [Longest Subsequence With Limited Sum](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) | [Python](Python/Longest%20Subsequence%20With%20Limited%20Sum.py) | $O(n*\log_{2} n)$ | $O(n)$ | Easy | - |
| 2391 | [Minimum Amount of Time to Collect Garbage](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/) | [Python](Python/Minimum%20Amount%20of%20Time%20to%20Collect%20Garbage.py) | $O(n)$ | $O(1)$ | Medium | - |
| 2395 | [Find Subarrays With Equal Sum](https://leetcode.com/problems/find-subarrays-with-equal-sum/) | [Python](Python/Find%20Subarrays%20With%20Equal%20Sum.py) | $O(n)$ | $O(n)$ | Easy | - |
| 2396 | [Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/) | [Python](Python/Strictly%20Palindromic%20Number.py) | $O(1)$ | $O(1)$ | Medium | - |
| 2399 | [Check Distances Between Same Letters](https://leetcode.com/problems/check-distances-between-same-letters/) | [Python](Python/Check%20Distances%20Between%20Same%20Letters.py) | $O(1)$ | $O(1)$ | Easy | - |
| 2401 | [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/) | [Python](Python/Longest%20Nice%20Subarray.py), [Java](Java/Longest%20Nice%20Subarray.java) | $O(n)$ | $O(1)$ | Medium | - |
| 2404 | [Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/) | [Python](Python/Most%20Frequent%20Even%20Element.py), [Java](Java/Most%20Frequent%20Even%20Element.java) | $O(n)$ | $O(n)$ | Easy | - |
| 2405 | [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) | [Python](Python/Optimal%20Partition%20of%20String.py), [Java](Java/Optimal%20Partition%20of%20String.java) | $O(n)$ | $O(1)$ | Medium | - |
| 2406 | [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | [Python](Python/Divide%20Intervals%20Into%20Minimum%20Number%20of%20Groups.py) | $O(n)$ | $O(n)$ | Medium | - |
| 2409 | [Count Days Spent Together](https://leetcode.com/problems/count-days-spent-together/) | [Python](Python/Count%20Days%20Spent%20Together.py) | $O(1)$ | $O(1)$ | Easy | - |
| 2413 | [Smallest Even Multiple](https://leetcode.com/problems/smallest-even-multiple/) | [Python](Python/Smallest%20Even%20Multiple.py), [Java](Java/Smallest%20Even%20Multiple.java) | $O(1)$ | $O(1)$ | Easy | - |
| 2414 | [Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) | [Python](Python/Length%20of%20the%20Longest%20Alphabetical%20Continuous%20Substring.py) | $O(n)$ | $O(1)$ | Medium | - |
| 2418 | [Sort the People](https://leetcode.com/problems/sort-the-people/) | [Python](Python/Sort%20the%20People.py) | $O(n * \log_{2} n)$ | $O(n)$ | Easy | - |
| 2419 | [Longest Subarray With Maximum Bitwise AND](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) | [Python](Python/Longest%20Subarray%20With%20Maximum%20Bitwise%20AND.py) | $O(n)$ | $O(1)$ | Medium | - |

## Last update

Solution table for problems was generated automatically on 2022-09-29 10:50 +0000

