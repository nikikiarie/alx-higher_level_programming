#!/usr/bin/python3
"""Task 11"""


class Student:
    """Student representation"""
    def __init__(self, first_name, last_name, age):
        """Initializes student"""
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self, attrs=None):
        """Returns dictionary rep of student"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dict_n = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                dict_n[key] = value
        return dict_n

    def reload_from_json(self, json):
        """replaces instance attributes with json args"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
