#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""


from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    if (len(argv) != 4):
        exit(1)

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3], pool_pre_ping=True)
    Base.metadata.create_all(eng)

    Session = sessionmaker(bind=eng)
    session = Session()

    st = session.query(State).order_by(State.id)

    for i in st:
        print(f'{i.id}:{i.name}')
    session.close()




