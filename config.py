import os
import re

LANGUAGES = {
    'Python': {
        'extension': 'py',
        'directory': 'Python',
    },
    'SQL': {
        'extension': 'sql',
        'directory': 'SQL',
    }
}


def get_solution_path(lang: str, title: str) -> str:
    file = '{}.{}'.format(title, LANGUAGES[lang]['extension'])
    return os.path.join(LANGUAGES[lang]['directory'], file)


def to_slug(name: str) -> str:
    return '-'.join(re.sub(r'[^\w\- ]', '', name).lower().split())
