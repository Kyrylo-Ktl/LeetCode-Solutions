from pathlib import Path

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

LEETCODE_API_URL = 'https://leetcode.com/graphql'

GRAPHQL_QUERY_PATH = ABSOLUTE_PATH / 'src' / 'resources' / 'test.graphql'
with open(GRAPHQL_QUERY_PATH, 'rt') as query_file:
    GRAPHQL_QUERY = query_file.read()

README_PATH = ABSOLUTE_PATH / 'README.md'

TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Difficulty', 'Notes']
ORDER_BY = '№'
NO_DATA = '-'
