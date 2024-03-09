#!/usr/bin/python3
"""This module describes the unittests for base_model

"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the instantiation of the BaseModel class"""
    def setUp(self):
        """This method sets up all test methods"""
        pass

    def tearDown(self):
        """This method tears down the test methods"""

        self.resetStorage()
        pass

    def resetStorage(self):
        """This method resets the FileStorage after testing"""

        FileStorage.__objects = {}
        if os.path.isfile(FileStorage.__file_path):
            os.remove(FileStorage.__file_path)

    def test_instantiation(self):
        """This method tests the instantiation of BaseModel"""

        a = BaseModel()
        self.assertEqual(str(type(a)), "<class 'models.base_model.BaseModel'>")
        self.asserIsInstance(a, BaseModel)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_instantiation_no_args(self):
        """This method tests the instantiation of BaseMode with no args"""
