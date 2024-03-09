#!/usr/bin/python3
"""This module contains all unittests for the ``Review`` class
"""
from models import storage
from models.review import Review
import datetime
import unittest
import os
import io
import sys


class Review_attributes_test(unittest.TestCase):
    """This class tests the attributes of a Review object instance.
    """
    def setUp(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_place_id_attr(self):
        a = Review()
        self.assertEqual(a.place_id, '')
        a.place_id = "234892348-2348923"
        self.assertEqual(a.place_id, '234892348-2348923')
        a.place_id = 1
        self.assertEqual(a.place_id, 1)

    def test_user_id_attr(self):
        a = Review()
        self.assertEqual(a.user_id, '')
        a.user_id = "2342349853477"
        self.assertEqual(a.user_id, '2342349853477')
        a.user_id = 123476
        self.assertEqual(a.user_id, 123476)

    def test_text_attr(self):
        a = Review()
        self.assertEqual(a.text, '')
        a.text = "YO, THIS PLACE IS AWESOMEE!!"
        self.assertEqual(a.text, 'YO, THIS PLACE IS AWESOMEE!!')
        a.text = 123476
        self.assertEqual(a.text, 123476)

    def test_id_attr(self):
        a = Review()
        self.assertIsInstance(a.id, str)

    def test_created_at_attr(self):
        a = Review()
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        a = Review()
        self.assertIsInstance(a.updated_at, datetime.datetime)


class Review_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a Review
    object/instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_init_no_args(self):
        a = Review()
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_int_arg(self):
        a = Review(12)
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_float_arg(self):
        a = Review(23.4)
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_str_arg(self):
        a = Review("Hello")
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_None_arg(self):
        a = Review(None)
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_zero_arg(self):
        a = Review(0)
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_list_arg(self):
        a = Review([1, 2.5, "Hello"])
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_dict_arg(self):
        kwargs = {"name": "abdu", "age": 28}
        a = Review(kwargs)
        self.assertIsInstance(a, Review)
        with self.assertRaises(AttributeError):
            print(a.name)

    def test_init_list_arg(self):
        a = Review(*[1, 2.5, "Hello"])
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Review.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_init_keyworded_args(self):
        kwargs = {"name": "abdu", "age": 28}
        a = Review(**kwargs)
        self.assertIsInstance(a, Review)
        self.assertEqual(a.name, "abdu")
        self.assertEqual(a.age, 28)

    def test_init_nonkeyworded_args(self):
        args = [1, 2.5, "HI"]
        a = Review(*args)
        self.assertIsInstance(a, Review)

    def test_init_unique_id_obj(self):
        a = Review()
        b = Review()
        self.assertNotEqual(a.id, b.id)

    def test_init_different_created_date(self):
        a = Review()
        b = Review()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_init_different_updated_date(self):
        a = Review()
        b = Review()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_init_keyworded_classattr(self):
        a = Review(**{"__class__": "BaseModel"})
        self.assertEqual(a.__class__.__name__, "Review")

    def test_init_keyworded_created_at(self):
        with self.assertRaises(ValueError):
            a = Review(**{"created_at": "500"})

    def test_init_keyworded_updated_at(self):
        with self.assertRaises(ValueError):
            a = Review(**{"updated_at": "500"})


class Review_str_test(unittest.TestCase):
    """This class tests the str method of a Review
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
        a = Review()
        self.assertEqual(a.__str__(),
                         "[Review] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = Review()
        self.assertEqual(str(a),
                         "[Review] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = Review()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[Review] ({}) {}\n".format(a.id, a.__dict__))


class Review_save_test(unittest.TestCase):
    """This class tests the save method of a Review
    class instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_onearg(self):
        a = Review()
        with self.assertRaises(TypeError):
            a.save(1)

    def test_noargs(self):
        a = Review()
        firstdate = a.updated_at
        a.save()
        seconddate = a.updated_at
        self.assertNotEqual(firstdate, seconddate)
        a.name = "abdu"
        a.age = 28
        a.save()
        objdict = storage.all()
        key = "Review.{}".format(a.id)
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


class Review_to_dict_test(unittest.TestCase):
    """This class tests the to_dict method of a Review
    class instance
    """
    def test_no_arg(self):
        a = Review()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = Review()
        with self.assertRaises(TypeError):
            dictionary = a.to_dict(1)

    def test_newattr_arg(self):
        a = Review()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = Review()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "Review")

    def test_created_at_attr(self):
        a = Review()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = Review()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
