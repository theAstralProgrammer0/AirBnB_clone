#!/usr/bin/python3
"""This is the module that contains the structure of the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This is the class that contains the attributes and methods of the
        Place class
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """This method instantiates a new Place object which is an instance
           of BaseModel
        """
        super().__init__(**kwargs)
