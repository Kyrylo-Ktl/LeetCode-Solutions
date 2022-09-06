import logging
import re
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

ABSOLUTE_PATH = Path(__file__).parent
RELATIVE_PATH = ABSOLUTE_PATH.relative_to(ABSOLUTE_PATH)

LANGUAGES = {
    'Python': {
        'extension': 'py',
        'directory': ABSOLUTE_PATH / 'Python',
    },
    'SQL': {
        'extension': 'sql',
        'directory': ABSOLUTE_PATH / 'SQL',
    }
}
GRAPHQL_QUERY_PATH = ABSOLUTE_PATH / 'src' / 'resources' / 'test.graphql'
README = ABSOLUTE_PATH / 'README.md'

TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Difficulty', 'Note']
ORDER_BY = '№'
NO_DATA = '-'


def get_solution_path(lang: str, title: str) -> str:
    return LANGUAGES[lang]['directory'] / '{}.{}'.format(title, LANGUAGES[lang]['extension'])


def to_slug(name: str) -> str:
    return '-'.join(re.sub(r'[^\w\- ]', '', name).lower().split())
