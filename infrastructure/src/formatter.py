import logging
from datetime import datetime

from infrastructure.config import DATETIME_FORMAT, README_PATH
from infrastructure.src.collector import SolutionsCollector
from infrastructure.src.markdown_table import MarkdownTable
from infrastructure.src.db.models import Problem
from infrastructure.src.resources.template import MARKDOWN_TEMPLATE

logger = logging.getLogger(__name__)


class MarkdownFormatter:
    @classmethod
    def format(cls):
        with open(README_PATH, 'wt') as readme:
            readme.write(cls.format_markdown())

    @classmethod
    def format_markdown(cls) -> str:
        solutions = SolutionsCollector.collect_solutions()
        problems = SolutionsCollector.collect_problems(solutions)

        return MARKDOWN_TEMPLATE.format(
            all_solutions=MarkdownTable.format(map(cls._format_problem, problems)),
            now=datetime.now().strftime(DATETIME_FORMAT)
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
