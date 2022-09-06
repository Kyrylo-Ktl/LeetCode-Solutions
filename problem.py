from enum import Enum
from typing import Generator

from pydantic import BaseModel, Field, FilePath, ValidationError

from config import LANGUAGES, get_solution_path


class LanguageEnum(str, Enum):
    python = 'Python'
    sql = 'SQL'


class Solution(BaseModel):
    path: FilePath
    language: LanguageEnum

    def format(self) -> str:
        return '[{}](./{})'.format(self.language, self.path.as_posix().replace(' ', '%20'))

    class Config:
        use_enum_values = True


class DifficultyEnum(str, Enum):
    easy = 'Easy'
    medium = 'Medium'
    hard = 'Hard'


class Tag(BaseModel):
    name: str


class Problem(BaseModel):
    id: int = Field(alias='questionFrontendId')
    title: str
    slug: str = Field(alias='titleSlug')
    tags: list[Tag] = Field(alias='topicTags')
    difficulty: DifficultyEnum
    is_premium: bool = Field(alias='isPaidOnly')

    @property
    def solutions(self) -> Generator:
        for language in LANGUAGES:
            try:
                yield Solution(language=language, path=get_solution_path(language, self.title))
            except ValidationError:
                pass

    class Config:
        use_enum_values = True
