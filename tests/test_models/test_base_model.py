#!/usr/bin/python3
"""This module describes the unittests for base_model

"""
import unittest
import os
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel_instantiation(unittest.TestCase):
    """Defines all unittests for testing instantiation of BaseModel class"""

    def test_instantiation(self):
        """This method tests the normal instantiation of BaseModel"""

        a = BaseModel()
        self.assertEqual(str(type(a)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_instantiation_no_args(self):
        """This method tests the instantiation of BaseModel with no args"""

        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        err = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_None_arg(self):
        """This method tests the instantiation of BaseModel with many args"""

        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(None)
        err = "'NoneType' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_int_arg(self):
        """This method tests the instantiation of BaseMode with an int arg"""

        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(1, 1, 2, 4, 5)
        err = "'int' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_bytes_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(b'Bytes', b'Python', b'Simple')
        err = "'bytes' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_str_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__("Invalid", "Strings", "Mental")
        err = "'str' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_empty_str_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__("")
        err = "'str' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_bool_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(True)
        err = "'bool' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_zero_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(0, 0, 0, 0, 0, 0)
        err = "'int' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_float_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(11.1, 12.8, 54.34, 5.009, 32.9)
        err = "'float' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_neg_val_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(-10, -9, -6, -500)
        err = "'int' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_set_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__({1, 2}, {80, 4, 56, 6}, {89, -98})
        err = "'set' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_tupl_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__((1, 2), )
        err = "'tuple' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_list_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(['string', 3, 6.8])
        err = "'list' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_dict_arg(self):
        with self.assertRaises(AttributeError) as e:
            now = datetime.datetime.now()
            BaseModel.__init__({'id': 'Holberton', 'created_at': now})
        err = "'dict' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_inf_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(float('inf'))
        err = "'float' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_nan_arg(self):
        with self.assertRaises(AttributeError) as e:
            BaseModel.__init__(float('nan'))
        err = "'float' object has no attribute 'id'"
        self.assertEqual(str(e.exception), err)

    def test_instantiation_kwargs(self):

    def test_instantiation_kwargs(self):

    def test_instantiation_kwargs(self):

    def test_instantiation_kwargs(self):

    def test_instantiation_kwargs(self):

    def test_instantiation_kwargs(self):






class TestBaseModel_save_test(unittest.TestCase):
    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
