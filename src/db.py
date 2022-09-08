from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import PROBLEMS_DB_URL

Base = declarative_base()


class DatabaseSession:
    def __init__(self):
        self._engine = create_engine(url=PROBLEMS_DB_URL)
        self.session = sessionmaker(bind=self._engine)

    def create_all(self):
        Base.metadata.create_all(self._engine)


db = DatabaseSession()
