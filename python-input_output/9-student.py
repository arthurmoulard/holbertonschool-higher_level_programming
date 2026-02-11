#!/usr/bin/python3
"""
This module defines a Student class used to represent a student
with basic personal information.
"""


class Student:
    """
    Represents a student with a first name, last name and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.
        """
        return self.__dict__
    