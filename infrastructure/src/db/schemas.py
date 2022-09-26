from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field

from infrastructure.src.db.models import Problem


class DifficultyEnum(str, Enum):
    easy = 'Easy'
    medium = 'Medium'
    hard = 'Hard'


class ProblemSchema(BaseModel):
    id: int = Field(alias='questionFrontendId')
    title: str
    difficulty: DifficultyEnum
    is_premium: bool = Field(alias='isPaidOnly')
    last_update: datetime = datetime.now(timezone.utc)

    @property
    def slug(self) -> str:
        return Problem.to_slug(self.title)

    class Config:
        use_enum_values = True
