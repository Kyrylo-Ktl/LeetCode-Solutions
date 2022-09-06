from typing import Iterable


class MarkdownTable:
    NO_DATA = '-'

    def __init__(self, headers: list, order_by: str):
        self._headers = headers
        self._order_by = order_by

    def __call__(self, content: Iterable[dict]) -> str:
        content = sorted(content, key=lambda x: x.get(self._order_by))
        head = self._format_head()
        rows = self._format_rows(content)
        return '\n'.join(map(lambda x: f'| {x} |', head + rows))

    def _format_head(self) -> list:
        return [' | '.join(self._headers), ' | '.join([':----:'] * len(self._headers))]

    def _format_rows(self, content: list) -> list:
        return [' | '.join(str(row.get(col, self.NO_DATA)) for col in self._headers) for row in content]
