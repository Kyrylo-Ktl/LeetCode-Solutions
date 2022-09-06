from typing import Iterable

import config


class MarkdownTable:
    NO_DATA = '-'

    @classmethod
    def format(cls, content: Iterable[dict]) -> str:
        content = sorted(content, key=lambda x: x.get(config.ORDER_BY))
        head = cls._format_head()
        rows = cls._format_rows(content)
        return '\n'.join(map(lambda x: f'| {x} |', head + rows))

    @staticmethod
    def _format_head() -> list:
        return [' | '.join(config.TABLE_HEADERS), ' | '.join([':----:'] * len(config.TABLE_HEADERS))]

    @staticmethod
    def _format_rows(content: list) -> list:
        return [' | '.join(str(row.get(col, config.NO_DATA)) for col in config.TABLE_HEADERS) for row in content]
