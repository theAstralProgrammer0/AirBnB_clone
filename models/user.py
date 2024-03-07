#!/usr/bin/env python3
"""This is the module that contains the structure of the user object attributes
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """This method instantiates a new User class that's a subclass of
           BaseModel making it an instance of the BaseModel
        """
        super().__init__(**kwargs)
