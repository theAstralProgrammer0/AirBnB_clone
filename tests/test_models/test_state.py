#!/usr/bin/python3
"""This module contains all unittests for the ``State`` class
"""
from models import storage
from models.state import State
import datetime
import unittest
import os
import io
import sys


class State_attributes_test(unittest.TestCase):
    """This class tests the attributes of a State object instance.
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
        a = State()
        self.assertEqual(a.name, '')
        a.name = "abdu"
        self.assertEqual(a.name, 'abdu')
        a.name = 123466
        self.assertEqual(a.name, 123466)

    def test_id_attr(self):
        a = State()
        self.assertIsInstance(a.id, str)

    def test_created_at_attr(self):
        a = State()
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        a = State()
        self.assertIsInstance(a.updated_at, datetime.datetime)


class State_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a State
    object/instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_init_no_args(self):
        a = State()
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_int_arg(self):
        a = State(12)
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_float_arg(self):
        a = State(23.4)
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_str_arg(self):
        a = State("Hello")
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_None_arg(self):
        a = State(None)
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_zero_arg(self):
        a = State(0)
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_list_arg(self):
        a = State([1, 2.5, "Hello"])
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_dict_arg(self):
        kwargs = {"name": "abdu", "age": 28}
        a = State(kwargs)
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')

    def test_init_list_arg(self):
        a = State(*[1, 2.5, "Hello"])
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "State.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_keyworded_args(self):
        kwargs = {"name": "abdu", "age": 28}
        a = State(**kwargs)
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, "abdu")
        self.assertEqual(a.age, 28)

    def test_init_nonkeyworded_args(self):
        args = [1, 2.5, "HI"]
        a = State(*args)
        self.assertIsInstance(a, State)

    def test_init_unique_id_obj(self):
        a = State()
        b = State()
        self.assertNotEqual(a.id, b.id)

    def test_init_different_created_date(self):
        a = State()
        b = State()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_init_different_updated_date(self):
        a = State()
        b = State()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_init_keyworded_classattr(self):
        a = State(**{"__class__": "BaseModel"})
        self.assertEqual(a.__class__.__name__, "State")

    def test_init_keyworded_created_at(self):
        with self.assertRaises(ValueError):
            a = State(**{"created_at": "500"})

    def test_init_keyworded_updated_at(self):
        with self.assertRaises(ValueError):
            a = State(**{"updated_at": "500"})


class State_str_test(unittest.TestCase):
    """This class tests the str method of a State
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
        a = State()
        self.assertEqual(a.__str__(),
                         "[State] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = State()
        self.assertEqual(str(a),
                         "[State] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = State()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[State] ({}) {}\n".format(a.id, a.__dict__))


class State_save_test(unittest.TestCase):
    """This class tests the save method of a State
    class instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_onearg(self):
        a = State()
        with self.assertRaises(TypeError):
            a.save(1)

    def test_noargs(self):
        a = State()
        firstdate = a.updated_at
        a.save()
        seconddate = a.updated_at
        self.assertNotEqual(firstdate, seconddate)
        a.name = "abdu"
        a.age = 28
        a.save()
        objdict = storage.all()
        key = "State.{}".format(a.id)
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


class State_to_dict_test(unittest.TestCase):
    """This class tests the to_dict method of a State
    class instance
    """
    def test_no_arg(self):
        a = State()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = State()
        with self.assertRaises(TypeError):
            dictionary = a.to_dict(1)

    def test_newattr_arg(self):
        a = State()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = State()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "State")

    def test_created_at_attr(self):
        a = State()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = State()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
