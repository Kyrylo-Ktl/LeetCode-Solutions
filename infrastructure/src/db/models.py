import logging
import os
import re
from typing import Generator

from sqlalchemy import Boolean, Column, Integer, String, exc
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Session

from infrastructure.config import LANGUAGES, BASE_DIR
from infrastructure.src.db import Base, db

logger = logging.getLogger(__name__)


class BaseModel(Base):
    __abstract__ = True

    def save(self, session: Session):
        try:
            session.add(self)
            session.commit()
        except exc.DatabaseError as err:
            logger.critical('Rollback on save', err)
            session.rollback()


class Problem(BaseModel):
    __tablename__ = 'problems'

    id = Column(Integer, nullable=False)
    title = Column(String, unique=True, nullable=False, primary_key=True)
    time = Column(String, nullable=True)
    memory = Column(String, nullable=True)
    difficulty = Column(String, nullable=False)
    is_premium = Column(Boolean, default=False, nullable=False)
    notes = Column(String, nullable=True)

    @classmethod
    def update_or_create(cls, title: str, data: dict):
        with db.session() as session:
            instance = session.query(cls).filter(cls.title == title).first()

            if instance is None:
                instance = cls(**data)

            for field, value in data.items():
                instance.__setattr__(field, value)

            instance.save(session)
            session.refresh(instance)

            return instance

    @hybrid_property
    def slug(self):
        return self.to_slug(self.title)

    @staticmethod
    def to_slug(title: str) -> str:
        return '-'.join(re.sub(r'[^\w\- ]', '', title.replace(' - ', ' ')).lower().split())

    @property
    def solutions(self) -> Generator:
        for language in LANGUAGES:
            filename = self.title + LANGUAGES[language]['extension']
            path = LANGUAGES[language]['directory'] / filename
            if os.path.exists(path):
                yield language, path.relative_to(BASE_DIR).as_posix().replace(' ', '%20')


db.create_all()
