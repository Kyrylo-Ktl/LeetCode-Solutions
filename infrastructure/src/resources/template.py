MARKDOWN_TEMPLATE = """
# [LeetCode](https://leetcode.com/problemset/all/)

The repository contains the best versions of my solutions to LeetCode problems

## Complexity chart

<p align="center">
    <img alt="complexity_chart" src="https://user-images.githubusercontent.com/93226646/191962988-602fb801-6d39-42f2-ac5b-32fd6452cddd.png">
</p>

## Number of operations for complexity

|    $f(n)$    |       $n = 10$       |       $n = 10^{{2}}$       |       $n = 10^{{3}}$       |       $n = 10^{{4}}$       |       $n = 10^{{5}}$       |       $n = 10^{{6}}$       |
|:------------:|:--------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|
|     $1$      |         $1$          |            $1$             |            $1$             |            $1$             |            $1$             |            $1$             |
|   $\log n$   |   $\\approx 3.32$    |      $\\approx 6.64$       |      $\\approx 9.97$       |    $\\approx 1.33 * 10$    |    $\\approx 1.66 * 10$    |    $\\approx 1.99 * 10$    |
|     $n$      |         $10$         |         $10^{{2}}$         |         $10^{{3}}$         |         $10^{{4}}$         |         $10^{{5}}$         |         $10^{{6}}$         |
| $n * \log n$ | $\\approx 3.32 * 10$ | $\\approx 6.64 * 10^{{2}}$ | $\\approx 9.97 * 10^{{3}}$ | $\\approx 1.33 * 10^{{5}}$ | $\\approx 1.66 * 10^{{6}}$ | $\\approx 1.99 * 10^{{7}}$ |
|  $n^{{2}}$   |      $10^{{2}}$      |         $10^{{4}}$         |         $10^{{6}}$         |         $10^{{8}}$         |        $10^{{10}}$         |        $10^{{12}}$         |
|  $2^{{n}}$   | $\\approx 10^{{3}}$  |    $\\approx 10^{{30}}$    |   $\\approx 10^{{301}}$    |   $\\approx 10^{{3010}}$   |  $\\approx 10^{{30102}}$   |  $\\approx 10^{{301030}}$  |
|     $n!$     | $\\approx 10^{{7}}$  |   $\\approx 10^{{156}}$    |   $\\approx 10^{{2568}}$   |  $\\approx 10^{{35660}}$   |  $\\approx 10^{{456574}}$  | $\\approx 10^{{5565709}}$  |

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