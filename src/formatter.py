import logging

import config
from markdown_table import MarkdownTable
from models import Problem
from readme_template import MARKDOWN_TEMPLATE
from src.collector import SolutionsCollector

logger = logging.getLogger(__name__)


class MarkdownFormatter:
    @classmethod
    def format(cls):
        with open(config.README_PATH, 'wt') as readme:
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
