#!/usr/bin/python3
"""This module contains all unittests for the ``User`` class
"""
from models import storage
from models.user import User
import datetime
import unittest
import os
import io
import sys


class User_attributes_test(unittest.TestCase):
    """This class tests the attributes of a User object instance.
    """
    def setUp(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_email_attr(self):
        a = User()
        self.assertEqual(a.email, '')
        a.email = "any@mail.com"
        self.assertEqual(a.email, 'any@mail.com')
        a.email = 1
        self.assertEqual(a.email, 1)

    def test_password_attr(self):
        a = User()
        self.assertEqual(a.password, '')
        a.password = "verystrongpass"
        self.assertEqual(a.password, 'verystrongpass')
        a.password = 123456
        self.assertEqual(a.password, 123456)

    def test_first_name_attr(self):
        a = User()
        self.assertEqual(a.first_name, '')
        a.first_name = "Abdelrahman"
        self.assertEqual(a.first_name, 'Abdelrahman')
        a.first_name = 123456
        self.assertEqual(a.first_name, 123456)

    def test_last_name_attr(self):
        a = User()
        self.assertEqual(a.last_name, '')
        a.last_name = "Metawei"
        self.assertEqual(a.last_name, 'Metawei')
        a.last_name = 123456
        self.assertEqual(a.last_name, 123456)

    def test_id_attr(self):
        a = User()
        self.assertIsInstance(a.id, str)

    def test_created_at_attr(self):
        a = User()
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        a = User()
        self.assertIsInstance(a.updated_at, datetime.datetime)


class User_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a User
    object/instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_init_no_args(self):
        a = User()
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_int_arg(self):
        a = User(12)
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_float_arg(self):
        a = User(23.4)
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_str_arg(self):
        a = User("Hello")
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_None_arg(self):
        a = User(None)
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_zero_arg(self):
        a = User(0)
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_list_arg(self):
        a = User([1, 2.5, "Hello"])
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_dict_arg(self):
        kwargs = {"name": "abdu", "age": 28}
        a = User(kwargs)
        self.assertIsInstance(a, User)
        with self.assertRaises(AttributeError):
            print(a.name)

    def test_init_list_arg(self):
        a = User(*[1, 2.5, "Hello"])
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, '')
        self.assertEqual(a.password, '')
        self.assertEqual(a.first_name, '')
        self.assertEqual(a.last_name, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "User.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_init_keyworded_args(self):
        kwargs = {"name": "abdu", "age": 28}
        a = User(**kwargs)
        self.assertIsInstance(a, User)
        self.assertEqual(a.name, "abdu")
        self.assertEqual(a.age, 28)

    def test_init_nonkeyworded_args(self):
        args = [1, 2.5, "HI"]
        a = User(*args)
        self.assertIsInstance(a, User)

    def test_init_unique_id_obj(self):
        a = User()
        b = User()
        self.assertNotEqual(a.id, b.id)

    def test_init_different_created_date(self):
        a = User()
        b = User()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_init_different_updated_date(self):
        a = User()
        b = User()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_init_keyworded_classattr(self):
        a = User(**{"__class__": "BaseModel"})
        self.assertEqual(a.__class__.__name__, "User")

    def test_init_keyworded_created_at(self):
        with self.assertRaises(ValueError):
            a = User(**{"created_at": "500"})

    def test_init_keyworded_updated_at(self):
        with self.assertRaises(ValueError):
            a = User(**{"updated_at": "500"})


class User_str_test(unittest.TestCase):
    """This class tests the str method of a User
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
        a = User()
        self.assertEqual(a.__str__(),
                         "[User] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = User()
        self.assertEqual(str(a),
                         "[User] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = User()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[User] ({}) {}\n".format(a.id, a.__dict__))


class User_save_test(unittest.TestCase):
    """This class tests the save method of a User
    class instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_onearg(self):
        a = User()
        with self.assertRaises(TypeError):
            a.save(1)

    def test_noargs(self):
        a = User()
        firstdate = a.updated_at
        a.save()
        seconddate = a.updated_at
        self.assertNotEqual(firstdate, seconddate)
        a.name = "abdu"
        a.age = 28
        a.save()
        objdict = storage.all()
        key = "User.{}".format(a.id)
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


class User_to_dict_test(unittest.TestCase):
    """This class tests the to_dict method of a User
    class instance
    """
    def test_no_arg(self):
        a = User()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = User()
        with self.assertRaises(TypeError):
            dictionary = a.to_dict(1)

    def test_newattr_arg(self):
        a = User()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = User()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "User")

    def test_created_at_attr(self):
        a = User()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = User()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
