MARKDOWN_TEMPLATE = """
# [LeetCode](https://leetcode.com/problemset/all/)

The repository contains the best versions of my solutions to LeetCode problems

## Complexity chart

<p align="center">
    <img alt="complexity_chart" src="https://user-images.githubusercontent.com/93226646/191962988-602fb801-6d39-42f2-ac5b-32fd6452cddd.png">
</p>

## Number of operations for complexity

|    $f(n)$    |       $n = 10$       |     $n = 10^{{2}}$     |     $n = 10^{{3}}$      |      $n = 10^{{4}}$      |       $n = 10^{{5}}$        |       $n = 10^{{6}}$        |
|:------------:|:--------------------:|:----------------------:|:-----------------------:|:------------------------:|:---------------------------:|:---------------------------:|
|     $1$      |         $1$          |          $1$           |           $1$           |           $1$            |             $1$             |             $1$             |
|   $\log n$   |   $\approxeq 3.32$   |    $\approxeq 6.64$    |    $\approxeq 9.97$     |  $\approxeq 1.33 * 10$   |    $\approxeq 1.66 * 10$    |    $\approxeq 1.99 * 10$    |
|     $n$      |         $10$         |       $10^{{2}}$       |       $10^{{3}}$        |        $10^{{4}}$        |         $10^{{5}}$          |         $10^{{6}}$          |
| $n * \log n$ |     $3.32 * 10$      |   $6.64 * 10^{{2}}$    |    $9.97 * 10^{{3}}$    |    $1.33 * 10^{{5}}$     | $\approxeq 1.66 * 10^{{6}}$ | $\approxeq 1.99 * 10^{{7}}$ |
|  $n^{{2}}$   |      $10^{{2}}$      |       $10^{{4}}$       |       $10^{{6}}$        |        $10^{{8}}$        |         $10^{{10}}$         |         $10^{{12}}$         |
|  $2^{{n}}$   | $\approxeq 10^{{3}}$ | $\approxeq 10^{{30}}$  | $\approxeq 10^{{301}}$  | $\approxeq 10^{{3010}}$  |  $\approxeq 10^{{30102}}$   |  $\approxeq 10^{{301030}}$  |
|     $n!$     | $\approxeq 10^{{7}}$ | $\approxeq 10^{{156}}$ | $\approxeq 10^{{2568}}$ | $\approxeq 10^{{35660}}$ |  $\approxeq 10^{{456574}}$  | $\approxeq 10^{{5565709}}$  |

## Complexity notations

| Notation |     Name     |  Sign  |           Meaning           |
|:--------:|:------------:|:------:|:---------------------------:|
|   $o$    |   Little O   |  $<$   |          Less than          |
|   $O$    |    Big O     | $\leq$ |    Less than or equal to    |
| $\Theta$ |    Theta     |  $=$   |          Equal to           |
| $\Omega$ |  Big Omega   | $\geq$ |  Greater than or equal to   |
| $\omega$ | Little Omega |  $>$   |        Greater than         |

## Solutions

{all_solutions}

## Last update

Solution table for problems was generated automatically on {now}

## Author

- [Kyrylo-Ktl](https://leetcode.com/Kyrylo-Ktl/) on LeetCode

"""