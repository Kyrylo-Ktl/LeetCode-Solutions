from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CODE_DIR = Path(__file__).parent

RESOURCES_PATH = CODE_DIR / 'src' / 'resources'

LANGUAGES = {
    'Python': {
        'extension': '.py',
        'directory': BASE_DIR / 'Python',
    },
    'Java': {
        'extension': '.java',
        'directory': BASE_DIR / 'Java',
    },
    'SQL': {
        'extension': '.sql',
        'directory': BASE_DIR / 'SQL',
    },
    'Shell': {
        'extension': '.sh',
        'directory': BASE_DIR / 'Shell',
    }
}
IGNORE_FILE_PREFIX = '_'

PROBLEMS_DB_PATH = RESOURCES_PATH / 'problems.db'
PROBLEMS_DB_URL = f'sqlite:///{PROBLEMS_DB_PATH}'

AUTHOR = 'Kyrylo-Ktl'
LEETCODE_URL = 'https://leetcode.com/'
LEETCODE_PROFILE_URL = LEETCODE_URL + AUTHOR
LEETCODE_API_URL = LEETCODE_URL + 'graphql'

GRAPHQL_QUERY_PATH = RESOURCES_PATH / 'problem_details_query.graphql'
with open(GRAPHQL_QUERY_PATH, 'rt') as query_file:
    GRAPHQL_QUERY = query_file.read()

NUMBER_OF_OPERATIONS_TABLE_PATH = RESOURCES_PATH / 'number_of_operations_table.txt'
with open(NUMBER_OF_OPERATIONS_TABLE_PATH, 'rt') as file:
    NUMBER_OF_OPERATIONS_TABLE = file.read()

COMPLEXITY_NOTATIONS_TABLE_PATH = RESOURCES_PATH / 'complexity_notations_table.txt'
with open(COMPLEXITY_NOTATIONS_TABLE_PATH, 'rt') as file:
    COMPLEXITY_NOTATIONS_TABLE = file.read()

README_PATH = BASE_DIR / 'README.md'

TABLE_HEADERS = ['№', 'Title', 'Solutions', 'Time', 'Memory', 'Beats Time', 'Beats Memory', 'Notes']
ORDER_BY = '№'
NO_DATA = '-'

DATETIME_FORMAT = '%Y-%m-%d %H:%M %z'
UPDATE_TIMEDELTA = timedelta(days=7)
