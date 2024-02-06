#!/usr/bin/python3
"""Defines class student"""


class Student:
    """Student representation"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self):
        """Returns dictionary rep of student"""
        return self.__dict__
