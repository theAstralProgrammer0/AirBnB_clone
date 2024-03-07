#!/usr/bin/env python3
"""This is the module that contains the structure of the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class that contains the attributes and methods of the
       Review class
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """This method instantiates a new Review object which is an instance
           of BaseModel
        """
        super().__init__(**kwargs)
