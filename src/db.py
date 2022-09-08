from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DatabaseSession:
    def __init__(self):
        self._engine = create_engine('sqlite:///test.db')
        self.session = sessionmaker(bind=self._engine)

    def create_all(self):
        Base.metadata.create_all(self._engine)


db = DatabaseSession()
