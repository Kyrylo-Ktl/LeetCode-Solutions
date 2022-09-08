from typing import Iterable

from infrastructure.config import NO_DATA, ORDER_BY, TABLE_HEADERS


class MarkdownTable:
    @classmethod
    def format(cls, content: Iterable[dict]) -> str:
        content = sorted(content, key=lambda x: x.get(ORDER_BY))
        head = cls._format_head()
        rows = cls._format_rows(content)
        return '\n'.join(map(lambda x: f'| {x} |', head + rows))

    @staticmethod
    def _format_head() -> list:
        return [
            ' | '.join(TABLE_HEADERS),
            ' | '.join([':----:'] * len(TABLE_HEADERS))
        ]

    @classmethod
    def _format_rows(cls, content: list) -> list:
        return [
            ' | '.join(cls._get_value(row, col) for col in TABLE_HEADERS)
            for row in content
        ]

    @staticmethod
    def _get_value(row: dict, key: str) -> str:
        value = row.get(key)
        return NO_DATA if value is None else str(value)
