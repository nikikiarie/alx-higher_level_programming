#!/usr/bin/python3
"""lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    n_state = State(name='Louisiana')
    session.add(n_state)
    st = session.query(State).filter_by(name='Louisiana').first()
    print(st.id)
    session.commit()
