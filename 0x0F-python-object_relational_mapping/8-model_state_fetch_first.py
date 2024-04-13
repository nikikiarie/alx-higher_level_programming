#!/usr/bin/python3

from sys import argv
from sqlalchemy import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    eng = create_engine('mysql+mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    obj = session.query(State).first()
    if !obj:
        print("Nothing")
    else:
        print(obj.id, obj.name, sep=": ")

