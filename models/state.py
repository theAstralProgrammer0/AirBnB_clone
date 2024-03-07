#!/usr/bin/env python3
"""This is the module that contains the structure of the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is the class that contains the attributes and methods of the
       State class
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """This method instantiates a new State object which is an instance
           of BaseModel
        """
        super().__init__(**kwargs)
