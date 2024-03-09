#!/usr/bin/python3
"""This is the module that contains the structure of the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class that contains the attributes and methods of the
       User class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """This method instantiates a new User object which is an instance
           of BaseModel
        """
        super().__init__(**kwargs)
