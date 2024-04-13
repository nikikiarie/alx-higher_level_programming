#!/usr/bin/python3
"""lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    if (len(argv) != 4):
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for i in st:
        print(f'{i.id}: {i.name}')
    session.close()
