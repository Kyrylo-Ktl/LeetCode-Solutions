import logging
import os
from typing import Generator, Iterable

import config
from markdown_table import MarkdownTable
from models import Problem
from readme_template import MARKDOWN_TEMPLATE
from src.parser import LeetCodeProblemDataParser

logger = logging.getLogger(__name__)


class SolutionsCollector:
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

    @classmethod
    def collect_problems(cls, titles: Iterable) -> Generator:
        with open(config.GRAPHQL_QUERY_PATH, 'rt') as query_file:
            parser = LeetCodeProblemDataParser(query_file.read())

        for title in titles:
            problem_data = parser.get_problem_data(title)

            if problem_data is None:
                logger.error('TODO LOGGING 2')
                continue

            yield Problem.get_or_create(title, problem_data)


class MarkdownFormatter:
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

    @staticmethod
    def _format_problem(problem: Problem) -> dict:
        return {
            '№': problem.id,
            'Title': f'[{problem.title}](https://leetcode.com/problems/{problem.slug}/)',
            'Solutions': ', '.join(f'[{language}]({path})' for language, path in problem.solutions),
            'Time': problem.time,
            'Memory': problem.memory,
            'Difficulty': problem.difficulty,
            'Notes': problem.notes,
        }
