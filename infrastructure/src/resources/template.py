from datetime import datetime, timezone

from infrastructure.config import (
    NUMBER_OF_OPERATIONS_TABLE,
    COMPLEXITY_NOTATIONS_TABLE,
    DATETIME_FORMAT,
    README_PATH,
)

MARKDOWN_TEMPLATE = """
# [LeetCode](https://leetcode.com/problemset/all/)

The repository contains the best versions of my solutions to LeetCode problems

## Complexity chart

<p align="center">
    <img alt="complexity_chart" src="https://user-images.githubusercontent.com/93226646/191962988-602fb801-6d39-42f2-ac5b-32fd6452cddd.png">
</p>

## Number of operations for complexity

{number_of_operations_table}

## Complexity notations

{complexity_notations_table}

## Solutions

{all_solutions}

## Last update

Solution table for problems was generated automatically on {now}

## Author

- [Kyrylo-Ktl](https://leetcode.com/Kyrylo-Ktl/) on LeetCode

"""


def format_markdown(solutions: str) -> str:
    return MARKDOWN_TEMPLATE.format(
        number_of_operations_table=NUMBER_OF_OPERATIONS_TABLE,
        complexity_notations_table=COMPLEXITY_NOTATIONS_TABLE,
        all_solutions=solutions,
        now=datetime.now(timezone.utc).strftime(DATETIME_FORMAT),
    )


def create_readme(solutions: str):
    with open(README_PATH, 'wt') as readme:
        readme.write(format_markdown(solutions))
