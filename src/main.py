import logging
import os
from typing import Generator, Iterable

import config
from markdown_table import MarkdownTable
from problem import Problem
from readme_template import MARKDOWN_TEMPLATE
from src.parser import LeetCodeProblemParser

logger = logging.getLogger(__name__)


class SolutionsCollector:
    TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Difficulty', 'Note']

    @staticmethod
    def collect_solutions() -> Generator:
        for language, props in config.LANGUAGES.items():
            directory = props['directory']
            extension = props['extension']

            for file in os.listdir(directory):
                if file.endswith(extension):
                    yield file.removesuffix(extension)
                else:
                    logger.error('TODO LOGGING')

    @staticmethod
    def collect_problems(titles: Iterable) -> Generator:
        with open(config.GRAPHQL_QUERY_PATH, 'rt') as query_file:
            parser = LeetCodeProblemParser(query_file.read())

        for title in titles:
            problem = parser.get_problem(config.to_slug(title))
            if problem is not None:
                logger.info(problem.title)
                yield problem
            else:
                logger.error('TODO LOGGING 2')


class MarkdownFormatter:
    @staticmethod
    def _format_problem(problem: Problem) -> dict:
        problem_solutions = ', '.join(
            '[{}]({})'.format(
                solution.language,
                solution.url_path,
            )
            for solution in problem.solutions
        )
        return {
            '№': problem.id,
            'Title': f'[{problem.title}](https://leetcode.com/problems/{problem.slug}/)',
            'Solutions': problem_solutions,
            'Difficulty': problem.difficulty,
        }

    @classmethod
    def format(cls):
        with open(config.README, 'wt') as readme:
            readme.write(cls.format_markdown())

    @classmethod
    def format_markdown(cls) -> str:
        solutions = SolutionsCollector.collect_solutions()
        problems = SolutionsCollector.collect_problems(solutions)

        return MARKDOWN_TEMPLATE.format(
            all_solutions=MarkdownTable.format(map(cls._format_problem, problems)),
        )
