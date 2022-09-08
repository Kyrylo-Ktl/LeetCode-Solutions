import logging
import os
from typing import Generator, Iterable

from infrastructure import config
from infrastructure.src.db.models import Problem
from infrastructure.src.parser import LeetCodeParser

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
                    logger.warning(f'File with unknown extension for {language}: {file}')

    @classmethod
    def collect_problems(cls, titles: Iterable) -> Generator:
        for title in titles:
            problem_data = LeetCodeParser.get_problem_data(title)

            if problem_data is None:
                logger.error(f'Failed to retrieve "{title}" details')
            else:
                yield Problem.update_or_create(title, problem_data)
                logger.info(f'Successfully parsed details for: {title}')
