from contextlib import contextmanager
from sqlalchemy.orm import Session

@contextmanager
def DBSession(eng):

    s = Session(eng)
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
    finally:
        s.close()


class Sessions:
    def __init__(self, eng):
        self.engine = eng

    def __enter__(self):
        self.s = Session(self.engine)
        return self.s

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s.close()
        self.s.expire_all()

