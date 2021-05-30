from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base


class DatabaseAdaptor:
    def __init__(self, database: str):
        engine = create_engine(f'sqlite:///{database}', echo=True)
        Session = orm.sessionmaker(bind=engine)
        self.session = Session()
        self.Base = declarative_base()

    def get_session(self):
        return self.session

    def get_base(self):
        return self.Base

