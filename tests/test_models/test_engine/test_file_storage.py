#!/usr/bin/env python3
"""This module contains all unittests for the ``file_storage`` class
"""
import unittest
from models.engine.file_storage import FileStorage


class file_storage_all_test(unittest.TestCase):
    """This class tests the all method of the file_storage class.
    """
    def test_noargs(self):
        sto = FileStorage()
        obj_dict = sto.all()
        self.assertEqual(type(obj_dict), dict)

    def test_1arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(1)

    def test_2args(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(1, 3)

    def test_strarg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all("Hello")

    def test_floatarg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(4.4)

    def test_floatarg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(4.4)
