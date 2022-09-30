import logging
import os
from typing import Generator, Iterable

from infrastructure.config import IGNORE_FILE_PREFIX, LANGUAGES, UPDATE_TIMEDELTA
from infrastructure.src.db.models import Problem
from infrastructure.src.parser import LeetCodeParser

logger = logging.getLogger(__name__)


class SolutionsCollector:
    @staticmethod
    def collect_solutions() -> set:
        solutions = set()

        for language, props in LANGUAGES.items():
            directory = props['directory']
            extension = props['extension']

            if not os.path.exists(directory):
                continue

            for file in os.listdir(directory):
                if file.startswith(IGNORE_FILE_PREFIX):
                    continue
                if file.endswith(extension):
                    solutions.add(file.removesuffix(extension).replace('%', '/'))
                else:
                    logger.warning(f'File with unknown extension for {language}: {file}')

        return solutions

    @classmethod
    def collect_problems(cls, titles: Iterable) -> Generator:
        for title in titles:
            problem = Problem.get_by_title(title)

            if problem is not None and problem.time_from_last_update < UPDATE_TIMEDELTA:
                yield problem
                continue

            problem = cls.parse_from_leetcode(title)

            if problem is None:
                logger.error(f'Failed to retrieve "{title}" details')
            else:
                logger.info(f'Successfully parsed details for: {title}')
                yield problem

    @staticmethod
    def parse_from_leetcode(title: str) -> Problem:
        problem_data = LeetCodeParser.get_problem_data(title)
        if problem_data is not None:
            return Problem.create_or_update_by_title(title, problem_data)
