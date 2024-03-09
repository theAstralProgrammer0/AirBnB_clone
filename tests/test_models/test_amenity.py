#!/usr/bin/python3
"""This module contains all unittests for the ``Amenity`` class
"""
from models import storage
from models.amenity import Amenity
import datetime
import unittest
import os
import io
import sys


class Amenity_attributes_test(unittest.TestCase):
    """This class tests the attributes of a Amenity object instance.
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
        a = Amenity()
        self.assertEqual(a.name, '')
        a.name = "abdu"
        self.assertEqual(a.name, 'abdu')
        a.name = 123486
        self.assertEqual(a.name, 123486)

    def test_id_attr(self):
        a = Amenity()
        self.assertIsInstance(a.id, str)

    def test_created_at_attr(self):
        a = Amenity()
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        a = Amenity()
        self.assertIsInstance(a.updated_at, datetime.datetime)


class Amenity_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a Amenity
    object/instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_init_no_args(self):
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_int_arg(self):
        a = Amenity(12)
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_float_arg(self):
        a = Amenity(23.4)
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_str_arg(self):
        a = Amenity("Hello")
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_None_arg(self):
        a = Amenity(None)
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_zero_arg(self):
        a = Amenity(0)
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_list_arg(self):
        a = Amenity([1, 2.5, "Hello"])
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_dict_arg(self):
        kwargs = {"name": "abdu", "age": 28}
        a = Amenity(kwargs)
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')

    def test_init_list_arg(self):
        a = Amenity(*[1, 2.5, "Hello"])
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(48), "{{\"{}\":".format(key))

    def test_init_keyworded_args(self):
        kwargs = {"name": "abdu", "age": 28}
        a = Amenity(**kwargs)
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, "abdu")
        self.assertEqual(a.age, 28)

    def test_init_nonkeyworded_args(self):
        args = [1, 2.5, "HI"]
        a = Amenity(*args)
        self.assertIsInstance(a, Amenity)

    def test_init_unique_id_obj(self):
        a = Amenity()
        b = Amenity()
        self.assertNotEqual(a.id, b.id)

    def test_init_different_created_date(self):
        a = Amenity()
        b = Amenity()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_init_different_updated_date(self):
        a = Amenity()
        b = Amenity()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_init_keyworded_classattr(self):
        a = Amenity(**{"__class__": "BaseModel"})
        self.assertEqual(a.__class__.__name__, "Amenity")

    def test_init_keyworded_created_at(self):
        with self.assertRaises(ValueError):
            a = Amenity(**{"created_at": "500"})

    def test_init_keyworded_updated_at(self):
        with self.assertRaises(ValueError):
            a = Amenity(**{"updated_at": "500"})


class Amenity_str_test(unittest.TestCase):
    """This class tests the str method of a Amenity
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
        a = Amenity()
        self.assertEqual(a.__str__(),
                         "[Amenity] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = Amenity()
        self.assertEqual(str(a),
                         "[Amenity] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = Amenity()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[Amenity] ({}) {}\n".format(a.id, a.__dict__))


class Amenity_save_test(unittest.TestCase):
    """This class tests the save method of a Amenity
    class instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_onearg(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.save(1)

    def test_noargs(self):
        a = Amenity()
        firstdate = a.updated_at
        a.save()
        seconddate = a.updated_at
        self.assertNotEqual(firstdate, seconddate)
        a.name = "abdu"
        a.age = 28
        a.save()
        objdict = storage.all()
        key = "Amenity.{}".format(a.id)
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


class Amenity_to_dict_test(unittest.TestCase):
    """This class tests the to_dict method of a Amenity
    class instance
    """
    def test_no_arg(self):
        a = Amenity()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            dictionary = a.to_dict(1)

    def test_newattr_arg(self):
        a = Amenity()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = Amenity()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "Amenity")

    def test_created_at_attr(self):
        a = Amenity()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = Amenity()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
