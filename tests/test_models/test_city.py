#!/usr/bin/python3
"""This module contains all unittests for the ``City`` class
"""
from models import storage
from models.city import City
import datetime
import unittest
import os
import io
import sys


class City_attributes_test(unittest.TestCase):
    """This class tests the attributes of a City object instance.
    """
    def setUp(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_name_attr(self):
        a = City()
        self.assertEqual(a.name, '')
        a.name = "abdu"
        self.assertEqual(a.name, 'abdu')
        a.name = 123456
        self.assertEqual(a.name, 123456)

    def test_state_id_attr(self):
        a = City()
        self.assertEqual(a.state_id, '')
        a.state_id = "CAI3439"
        self.assertEqual(a.state_id, 'CAI3439')
        a.state_id = 123456
        self.assertEqual(a.state_id, 123456)

    def test_id_attr(self):
        a = City()
        self.assertIsInstance(a.id, str)

    def test_created_at_attr(self):
        a = City()
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        a = City()
        self.assertIsInstance(a.updated_at, datetime.datetime)


class City_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a City
    object/instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_init_no_args(self):
        a = City()
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_int_arg(self):
        a = City(12)
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_float_arg(self):
        a = City(23.4)
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_str_arg(self):
        a = City("Hello")
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_None_arg(self):
        a = City(None)
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_zero_arg(self):
        a = City(0)
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_list_arg(self):
        a = City([1, 2.5, "Hello"])
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_dict_arg(self):
        kwargs = {"name": "abdu", "age": 28}
        a = City(kwargs)
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')

    def test_init_list_arg(self):
        a = City(*[1, 2.5, "Hello"])
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_keyworded_args(self):
        kwargs = {"name": "abdu", "age": 28}
        a = City(**kwargs)
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, "abdu")
        self.assertEqual(a.age, 28)

    def test_init_nonkeyworded_args(self):
        args = [1, 2.5, "HI"]
        a = City(*args)
        self.assertIsInstance(a, City)

    def test_init_unique_id_obj(self):
        a = City()
        b = City()
        self.assertNotEqual(a.id, b.id)

    def test_init_different_created_date(self):
        a = City()
        b = City()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_init_different_updated_date(self):
        a = City()
        b = City()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_init_keyworded_classattr(self):
        a = City(**{"__class__": "BaseModel"})
        self.assertEqual(a.__class__.__name__, "City")

    def test_init_keyworded_created_at(self):
        with self.assertRaises(ValueError):
            a = City(**{"created_at": "500"})

    def test_init_keyworded_updated_at(self):
        with self.assertRaises(ValueError):
            a = City(**{"updated_at": "500"})


class City_str_test(unittest.TestCase):
    """This class tests the str method of a City
    class instance
    """
    def setUp(self):
        """redirecting stdout to output
        """
        self.output = io.StringIO()
        self.originalstdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """resetting stdout to its original
        value
        """
        sys.stdout = self.originalstdout

    def test_str_method(self):
        a = City()
        self.assertEqual(a.__str__(),
                         "[City] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = City()
        self.assertEqual(str(a),
                         "[City] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = City()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[City] ({}) {}\n".format(a.id, a.__dict__))


class City_save_test(unittest.TestCase):
    """This class tests the save method of a City
    class instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_onearg(self):
        a = City()
        with self.assertRaises(TypeError):
            a.save(1)

    def test_noargs(self):
        a = City()
        firstdate = a.updated_at
        a.save()
        seconddate = a.updated_at
        self.assertNotEqual(firstdate, seconddate)
        a.name = "abdu"
        a.age = 28
        a.save()
        objdict = storage.all()
        key = "City.{}".format(a.id)
        self.assertEqual(objdict[key].name, "abdu")
        self.assertEqual(objdict[key].age, 28)
        try:
            with open('file.json', 'r', encoding='utf-8') as f:
                jsonstr = f.read()
                nameinside = "name\": \"abdu" in jsonstr
                ageinside = "28" in jsonstr
                self.assertTrue(nameinside)
                self.assertTrue(ageinside)
        except Exception:
            pass


class City_to_dict_test(unittest.TestCase):
    """This class tests the to_dict method of a City
    class instance
    """
    def test_no_arg(self):
        a = City()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = City()
        with self.assertRaises(TypeError):
            dictionary = a.to_dict(1)

    def test_newattr_arg(self):
        a = City()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = City()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "City")

    def test_created_at_attr(self):
        a = City()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = City()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
