#!/usr/bin/python3
"""This is the module that contains the structure of the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is the class that contains the attributes and methods of the
       Amenity class
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """This method instantiates a new Amenity object which is an instance
           of BaseModel
        """
        super().__init__(**kwargs)
