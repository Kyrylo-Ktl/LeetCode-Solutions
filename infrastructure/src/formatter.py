import logging

from infrastructure.src.collector import SolutionsCollector
from infrastructure.src.markdown_table import MarkdownTable
from infrastructure.src.db.models import Problem
from infrastructure.src.resources.template import create_readme

logger = logging.getLogger(__name__)


class MarkdownFormatter:
    @classmethod
    def format(cls) -> str:
        solutions = SolutionsCollector.collect_solutions()
        problems = SolutionsCollector.collect_problems(solutions)
        solutions_table = MarkdownTable.format(map(cls._format_problem, problems))
        return create_readme(solutions=solutions_table)

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
