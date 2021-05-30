# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DBSession import DBSession
from DBSession import Sessions

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_engine():
    return create_engine('postgresql://localhost/postgres')
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')
    eng = get_engine()
    s = Session(eng)
    rs = eng.execute('select * from chi')
    print(rs.fetchall())
    s = Session(eng)
    rs = s.execute('select * from chi')
    print(rs.fetchall())
    with DBSession(eng) as session:
        rs = session.execute('select * from chi')
        # con = eng.connect()
        # rs = con.execute('select * from chi2')
    print(rs.fetchall())
    with Sessions(eng) as ss:
        ss.execute('select * from chi')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
