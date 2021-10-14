#!/usr/bin/python3
# 9-student.py
"""Defines a class student"""


class Student:
    """represent a student"""

    def __init__(self, first_name, last_name, age):
        """initialise a student
        
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_jason_file(self):
        """Get a dictionary representation of the student"""
        return self.__dict__
