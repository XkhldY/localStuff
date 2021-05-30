from sqlalchemy import Column, INTEGER, String, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from databaseAdaptor import DatabaseAdaptor

base = declarative_base()


class Book(base):
    __tablename__ = 'book'

    id = Column(INTEGER, primary_key=True)
    title = Column(String)
    author = Column(String)
    read = Column(BOOLEAN)

    def __repr__(self):
        return {'id': self.id, 'title':self.title,'author':self.author,'read':self.read}
