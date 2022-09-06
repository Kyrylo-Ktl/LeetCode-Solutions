import re
from pathlib import Path

ABS_PATH = Path(__file__).parent
BASE_DIR = ABS_PATH.relative_to(ABS_PATH)

LANGUAGES = {
    'Python': {
        'extension': 'py',
        'directory': BASE_DIR / 'Python',
    },
    'SQL': {
        'extension': 'sql',
        'directory': BASE_DIR / 'SQL',
    }
}
GRAPHQL_QUERY_PATH = 'src/test.graphql'


def get_solution_path(lang: str, title: str) -> str:
    return LANGUAGES[lang]['directory'] / '{}.{}'.format(title, LANGUAGES[lang]['extension'])


def to_slug(name: str) -> str:
    return '-'.join(re.sub(r'[^\w\- ]', '', name).lower().split())
