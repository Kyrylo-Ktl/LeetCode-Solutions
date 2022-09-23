import logging
import os
from typing import Generator, Iterable

from infrastructure.config import IGNORE_FILE_PREFIX, LANGUAGES
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
                    solutions.add(file.removesuffix(extension).replace('|', '/'))
                else:
                    logger.warning(f'File with unknown extension for {language}: {file}')

        return solutions

    @classmethod
    def collect_problems(cls, titles: Iterable) -> Generator:
        for title in titles:
            problem_data = LeetCodeParser.get_problem_data(title)

            if problem_data is None:
                logger.error(f'Failed to retrieve "{title}" details')
            else:
                yield Problem.update_or_create(title, problem_data)
                logger.info(f'Successfully parsed details for: {title}')
