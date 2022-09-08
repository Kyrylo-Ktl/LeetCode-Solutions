import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

ABSOLUTE_PATH = Path(__file__).parent
RELATIVE_PATH = ABSOLUTE_PATH.relative_to(ABSOLUTE_PATH)

LANGUAGES = {
    'Python': {
        'extension': '.py',
        'directory': ABSOLUTE_PATH / 'Python',
    },
    'SQL': {
        'extension': '.sql',
        'directory': ABSOLUTE_PATH / 'SQL',
    }
}

PROBLEMS_DB_PATH = ABSOLUTE_PATH / 'src' / 'resources' / 'problems.db'
PROBLEMS_DB_URL = f'sqlite:///{PROBLEMS_DB_PATH}'
GRAPHQL_QUERY_PATH = ABSOLUTE_PATH / 'src' / 'resources' / 'test.graphql'
README = ABSOLUTE_PATH / 'README.md'

TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Difficulty', 'Notes']
ORDER_BY = '№'
NO_DATA = '-'


def get_solution_path(lang: str, title: str) -> Path:
    filename = title + LANGUAGES[lang]['extension']
    return LANGUAGES[lang]['directory'] / filename
