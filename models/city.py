#!/usr/bin/env python3
"""This is the module that contains the structure of the City class
"""
from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """This is the class that contains the attributes and methods of the
       City class
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """This method instantiates a new City object which is an instance
           of BaseModel
        """
        super().__init__(**kwargs)
