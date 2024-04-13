#!/usr/bin/python3
"""Contains the class definition of a State"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Representation of the table states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = column(String(128), nullable=False)
