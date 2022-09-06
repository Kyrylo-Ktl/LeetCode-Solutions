import os

import config
from markdown_table import MarkdownTable
from problem import Problem
from readme_template import TEMPLATE
from src.parser import LeetCodeProblemParser


class MarkdownFormatter:
    TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Tags', 'Difficulty']

    def __init__(self, output: str):
        self._output = output

    @staticmethod
    def _format_problem_fields(problem: Problem) -> dict:
        for solution in problem.solutions:
            print(str(solution.path))
        problem_solutions = ', '.join(
            '[{}]({})'.format(solution.language, solution.path.as_posix().replace(' ', '%20'))
            for solution in problem.solutions
        )
        return {
            '№': problem.id,
            'Title': f'[{problem.title}](https://leetcode.com/problems/{problem.slug}/)',
            'Solutions': problem_solutions,
            'Tags': ', '.join(tag.name for tag in problem.tags),
            'Difficulty': problem.difficulty,
        }

    def main(self):
        with open(self._output, 'wt') as readme:
            readme.write(self.format())

    def format(self) -> str:
        problems = map(self._format_problem_fields, self.collect_problems())
        table = MarkdownTable(self.TABLE_HEADERS, order_by='№')

        return TEMPLATE.format(all_solutions=table(problems))

    def collect_problems(self) -> list[Problem]:
        with open(config.GRAPHQL_QUERY_PATH, 'rt') as query_file:
            parser = LeetCodeProblemParser(query_file.read())

        for language, props in config.LANGUAGES.items():
            directory = props['directory']
            extension = props['extension']

            for file in os.listdir(directory):
                if file.endswith(extension):
                    problem_title = file.removesuffix(extension)
                    problem_slug = config.to_slug(problem_title)

                    problem = parser.get_problem(problem_slug)
                    if problem is not None:
                        print(problem.title)
                        yield problem


if __name__ == '__main__':
    MarkdownFormatter(output=config.BASE_DIR / 'README.md').main()
