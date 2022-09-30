import logging
import os
import re
from datetime import timezone, datetime, timedelta
from typing import Generator

from sqlalchemy import Boolean, Column, DateTime, Integer, String, exc
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

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

    def update(self, session: Session, data: dict):
        for field, value in data.items():
            self.__setattr__(field, value)
        self.save(session)

    @classmethod
    def create(cls, session: Session, data: dict) -> 'Base':
        instance = cls(**data)
        instance.save(session)
        return instance


class Problem(BaseModel):
    __tablename__ = 'problems'

    id = Column(Integer, nullable=False)
    title = Column(String, unique=True, nullable=False, primary_key=True)
    time = Column(String, nullable=True)
    memory = Column(String, nullable=True)
    difficulty = Column(String, nullable=False)
    is_premium = Column(Boolean, default=False, nullable=False)
    notes = Column(String, nullable=True)
    last_update = Column(DateTime)

    @classmethod
    def create_or_update_by_title(cls, title: str, data: dict):
        with db.session() as session:
            instance = cls.get_by_title(title)

            if instance is None:
                instance = cls.create(session, data)

            instance.update(session, data)
            session.refresh(instance)
            print(instance.last_update)
            return instance

    @classmethod
    def get_by_title(cls, title: str) -> 'Problem':
        with db.session() as session:
            return session.query(cls).filter(cls.title == title).first()

    @property
    def time_from_last_update(self) -> timedelta:
        return datetime.now(timezone.utc) - self.last_update.replace(tzinfo=timezone.utc)

    @property
    def slug(self):
        return self.to_slug(self.title)

    @staticmethod
    def to_slug(title: str) -> str:
        return '-'.join(re.sub(r'[^\w\- ]', '', title.replace(' - ', ' ').replace('%', '/')).lower().split())

    @property
    def solutions(self) -> Generator:
        for language in LANGUAGES:
            filename = self.title.replace('/', '%') + LANGUAGES[language]['extension']
            path = LANGUAGES[language]['directory'] / filename

            if 'Gain' in self.title:
                print(self.title, os.path.exists(path))

            if os.path.exists(path):
                yield language, path.relative_to(BASE_DIR).as_posix().replace(' ', '%20')


db.create_all()
