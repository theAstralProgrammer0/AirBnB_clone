#!/usr/bin/python3
"""This module contains all unittests for the ``Place`` class
"""
from models import storage
from models.place import Place
import datetime
import unittest
import os
import io
import sys


class Place_attributes_test(unittest.TestCase):
    """This class tests the attributes of a Place object instance.
    """
    def setUp(self):
        try:
            os.remove('file.json')
        except Exception:
            pass
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_city_id_attr(self):
        a = Place()
        self.assertEqual(a.city_id, '')
        a.city_id = "12328972474"
        self.assertEqual(a.city_id, '12328972474')
        a.city_id = 1
        self.assertEqual(a.city_id, 1)

    def test_user_id_attr(self):
        a = Place()
        self.assertEqual(a.user_id, '')
        a.user_id = "2345436754"
        self.assertEqual(a.user_id, '2345436754')
        a.user_id = 1
        self.assertEqual(a.user_id, 1)

    def test_name_attr(self):
        a = Place()
        self.assertEqual(a.name, '')
        a.name = "abdu"
        self.assertEqual(a.name, 'abdu')
        a.name = 123466
        self.assertEqual(a.name, 123466)

    def test_description_attr(self):
        a = Place()
        self.assertEqual(a.description, '')
        a.description = "New Cairo"
        self.assertEqual(a.description, 'New Cairo')
        a.description = 1
        self.assertEqual(a.description, 1)

    def test_number_rooms_attr(self):
        a = Place()
        self.assertEqual(a.number_rooms, 0)
        a.number_rooms = "5"
        self.assertEqual(a.number_rooms, '5')
        a.number_rooms = 3
        self.assertEqual(a.number_rooms, 3)

    def test_number_bathrooms_attr(self):
        a = Place()
        self.assertEqual(a.number_bathrooms, 0)
        a.number_bathrooms = "2"
        self.assertEqual(a.number_bathrooms, '2')
        a.number_bathrooms = 3
        self.assertEqual(a.number_bathrooms, 3)

    def test_max_guest_attr(self):
        a = Place()
        self.assertEqual(a.max_guest, 0)
        a.max_guest = "1"
        self.assertEqual(a.max_guest, '1')
        a.max_guest = 2
        self.assertEqual(a.max_guest, 2)

    def test_price_by_night_attr(self):
        a = Place()
        self.assertEqual(a.price_by_night, 0)
        a.price_by_night = "500$"
        self.assertEqual(a.price_by_night, '500$')
        a.price_by_night = 40
        self.assertEqual(a.price_by_night, 40)

    def test_latitude_attr(self):
        a = Place()
        self.assertEqual(a.latitude, 0.0)
        a.latitude = "400.50"
        self.assertEqual(a.latitude, '400.50')
        a.latitude = 320.43
        self.assertEqual(a.latitude, 320.43)

    def test_longitude_attr(self):
        a = Place()
        self.assertEqual(a.longitude, 0.0)
        a.longitude = "400.59"
        self.assertEqual(a.longitude, '400.59')
        a.longitude = 230.423
        self.assertEqual(a.longitude, 230.423)

    def test_amenity_ids_attr(self):
        a = Place()
        self.assertEqual(a.amenity_ids, [])
        a.amenity_ids = "[2, 3, 5]"
        self.assertEqual(a.amenity_ids, '[2, 3, 5]')
        a.amenity_ids = [1, 4, 5]
        self.assertEqual(a.amenity_ids, [1, 4, 5])

    def test_id_attr(self):
        a = Place()
        self.assertIsInstance(a.id, str)

    def test_created_at_attr(self):
        a = Place()
        self.assertIsInstance(a.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        a = Place()
        self.assertIsInstance(a.updated_at, datetime.datetime)


class Place_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a Place
    object/instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_init_no_args(self):
        a = Place()
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_int_arg(self):
        a = Place(12)
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_float_arg(self):
        a = Place(23.4)
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_str_arg(self):
        a = Place("Hello")
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_None_arg(self):
        a = Place(None)
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_zero_arg(self):
        a = Place(0)
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_list_arg(self):
        a = Place([1, 2.5, "Hello"])
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_dict_arg(self):
        kwargs = {"name": "abdu", "age": 28}
        a = Place(kwargs)
        self.assertIsInstance(a, Place)
        self.assertEqual(a.name, '')

    def test_init_list_arg(self):
        a = Place(*[1, 2.5, "Hello"])
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.id), 36)
        self.assertIsInstance(a.created_at, datetime.datetime)
        self.assertIsInstance(a.updated_at, datetime.datetime)
        objdict = storage.all()
        key = "Place.{}".format(a.id)
        self.assertIn(key, objdict)
        with open('file.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_init_keyworded_args(self):
        kwargs = {"name": "abdu", "age": 28}
        a = Place(**kwargs)
        self.assertIsInstance(a, Place)
        self.assertEqual(a.name, "abdu")
        self.assertEqual(a.age, 28)

    def test_init_nonkeyworded_args(self):
        args = [1, 2.5, "HI"]
        a = Place(*args)
        self.assertIsInstance(a, Place)

    def test_init_unique_id_obj(self):
        a = Place()
        b = Place()
        self.assertNotEqual(a.id, b.id)

    def test_init_different_created_date(self):
        a = Place()
        b = Place()
        self.assertNotEqual(a.created_at, b.created_at)

    def test_init_different_updated_date(self):
        a = Place()
        b = Place()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_init_keyworded_classattr(self):
        a = Place(**{"__class__": "BaseModel"})
        self.assertEqual(a.__class__.__name__, "Place")

    def test_init_keyworded_created_at(self):
        with self.assertRaises(ValueError):
            a = Place(**{"created_at": "500"})

    def test_init_keyworded_updated_at(self):
        with self.assertRaises(ValueError):
            a = Place(**{"updated_at": "500"})


class Place_str_test(unittest.TestCase):
    """This class tests the str method of a Place
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
        a = Place()
        self.assertEqual(a.__str__(),
                         "[Place] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = Place()
        self.assertEqual(str(a),
                         "[Place] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = Place()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[Place] ({}) {}\n".format(a.id, a.__dict__))


class Place_save_test(unittest.TestCase):
    """This class tests the save method of a Place
    class instance
    """
    def setUp(self):
        objdict = storage.all()
        objdict.clear()
        storage.save()

    def test_onearg(self):
        a = Place()
        with self.assertRaises(TypeError):
            a.save(1)

    def test_noargs(self):
        a = Place()
        firstdate = a.updated_at
        a.save()
        seconddate = a.updated_at
        self.assertNotEqual(firstdate, seconddate)
        a.name = "abdu"
        a.age = 28
        a.save()
        objdict = storage.all()
        key = "Place.{}".format(a.id)
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


class Place_to_dict_test(unittest.TestCase):
    """This class tests the to_dict method of a Place
    class instance
    """
    def test_no_arg(self):
        a = Place()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = Place()
        with self.assertRaises(TypeError):
            dictionary = a.to_dict(1)

    def test_newattr_arg(self):
        a = Place()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = Place()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "Place")

    def test_created_at_attr(self):
        a = Place()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = Place()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
