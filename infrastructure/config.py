from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CODE_DIR = Path(__file__).parent

LANGUAGES = {
    'Python': {
        'extension': '.py',
        'directory': BASE_DIR / 'Python',
    },
    'SQL': {
        'extension': '.sql',
        'directory': BASE_DIR / 'SQL',
    }
}

PROBLEMS_DB_PATH = CODE_DIR / 'src' / 'resources' / 'problems.db'
PROBLEMS_DB_URL = f'sqlite:///{PROBLEMS_DB_PATH}'

LEETCODE_API_URL = 'https://leetcode.com/graphql'

GRAPHQL_QUERY_PATH = CODE_DIR / 'src' / 'resources' / 'test.graphql'
with open(GRAPHQL_QUERY_PATH, 'rt') as query_file:
    GRAPHQL_QUERY = query_file.read()

README_PATH = BASE_DIR / 'README.md'

TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Difficulty', 'Notes']
ORDER_BY = '№'
NO_DATA = '-'
