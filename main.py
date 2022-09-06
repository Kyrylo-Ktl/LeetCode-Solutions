import os

from config import LANGUAGES, to_slug
from markdown_table import MarkdownTable
from parser import LeetCodeProblemParser
from problem import Problem
from readme_template import TEMPLATE


class MarkdownFormatter:
    TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Tags', 'Difficulty']

    def __init__(self, output: str):
        self._output = output

    @staticmethod
    def _format_problem_fields(problem: Problem) -> dict:
        return {
            '№': problem.id,
            'Title': f'[{problem.title}](https://leetcode.com/problems/{problem.slug}/)',
            'Solutions': ', '.join('[{}](./{})'.format(solution.language, solution.path.as_posix().replace(' ', '%20'))
                                   for solution in problem.solutions),
            'Tags': ', '.join(tag.name for tag in problem.tags),
            'Difficulty': problem.difficulty,
        }

    def main(self):
        with open(f'{self._output}.md', 'wt') as readme:
            readme.write(self.format())

    def format(self) -> str:
        problems = map(self._format_problem_fields, self.collect_problems())
        table = MarkdownTable(self.TABLE_HEADERS, order_by='№')

        return TEMPLATE.format(all_solutions=table(problems))

    def collect_problems(self) -> list[Problem]:
        with open('test.graphql', 'rt') as query_file:
            parser = LeetCodeProblemParser(query_file.read())

        for language, props in LANGUAGES.items():
            directory = props['directory']
            extension = props['extension']

            for file in os.listdir(directory):
                if file.endswith(extension):
                    problem_title = file.removesuffix(extension)
                    problem_slug = to_slug(problem_title)

                    problem = parser.get_problem(problem_slug)
                    if problem is not None:
                        print(problem.title)
                        yield problem


if __name__ == '__main__':
    MarkdownFormatter(output='README').main()
