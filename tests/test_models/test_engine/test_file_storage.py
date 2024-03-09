#!/usr/bin/python3
"""This module contains all unittests for the ``file_storage`` class
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City


class FileStorage_attributes_test(unittest.TestCase):
    """This class tests accessing the attributes of the
    FileStorage class
    """
    def test_file_path_attr(self):
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)

    def test_objects_attr(self):
        with self.assertRaises(AttributeError):
            print(FileStorage.__objects)


class FileStorage_instantiation_test(unittest.TestCase):
    """This class tests the instantiation of a FileStorage
    instance
    """
    def test_init_noargs(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_init_1args(self):
        with self.assertRaises(TypeError):
            sto = FileStorage(1)

    def test_init_more_than_one(self):
        with self.assertRaises(TypeError):
            sto = FileStorage(2, 3)


class FileStorage_all_test(unittest.TestCase):
    """This class tests the all method of the FileStorage class.
    """
    def test_noargs(self):
        sto = FileStorage()
        obj_dict = sto.all()
        self.assertEqual(type(obj_dict), dict)

    def test_1_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(1)

    def test_2_args(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(1, 3)

    def test_str_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all("Hello")

    def test_float_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(4.4)

    def test_list_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all([1, 2])

    def test_dict_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(dict(hi="bye", name="abdu"))

    def test_None_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(None)

    def test_zero_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(0)

    def test_negative_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(-5)

    def test_empty_str_rg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all("")

    def test_boolean_arg(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            obj_dict = sto.all(True)


class FileStorage_new_test(unittest.TestCase):
    """This class tests the new method of the FileStorage
    class
    """
    def test_noargs(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            sto.new()

    def test_BaseModel_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        obj = BaseModel()
        sto.new(obj)
        self.assertTrue(obj in obj_dict.values())

    def test_User_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        obj = User()
        sto.new(obj)
        self.assertTrue(obj in obj_dict.values())

    def test_Place_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        obj = Place()
        sto.new(obj)
        self.assertTrue(obj in obj_dict.values())

    def test_State_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        obj = State()
        sto.new(obj)
        self.assertTrue(obj in obj_dict.values())

    def test_City_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        obj = City()
        sto.new(obj)
        self.assertTrue(obj in obj_dict.values())

    def test_Review_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        obj = Review()
        sto.new(obj)
        self.assertTrue(obj in obj_dict.values())

    def test_FileStorage_obj(self):
        sto = FileStorage()
        obj = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new(obj)

    def test_no_args(self):
        sto = FileStorage()
        with self.assertRaises(TypeError):
            sto.new()

    def test_more_than_one_args(self):
        sto = FileStorage()
        a = User()
        b = BaseModel()
        with self.assertRaises(TypeError):
            sto.new(a, b)

    def test_int_obj(self):
        sto = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new(5)

    def test_float_obj(self):
        sto = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new(5.6)

    def test_str_obj(self):
        sto = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new("Hello")

    def test_list_obj(self):
        sto = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new([1, 2, 3])

    def test_dict_obj(self):
        sto = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new(dict(name="Abdu", second="secondval"))

    def test_none_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        with self.assertRaises(AttributeError):
            sto.new(None)

    def test_zero_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        with self.assertRaises(AttributeError):
            sto.new(0)

    def test_negative_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        with self.assertRaises(AttributeError):
            sto.new(-1)

    def test_bool_obj(self):
        sto = FileStorage()
        obj_dict = sto.all()
        with self.assertRaises(AttributeError):
            sto.new(True)

    def test_self_obj(self):
        sto = FileStorage()
        with self.assertRaises(AttributeError):
            sto.new(sto)


class FileStorage_save_test(unittest.TestCase):
    """This class tests the save method/serialization
        into a file of the FileStorage class
        """

    def setUp(self):
        objdict = FileStorage().all()
        objdict.clear()
        FileStorage().save()

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_save_BaseModel_obj(self):
        a = BaseModel()
        objdict = FileStorage().all()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        objdict[key] = a
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(f.read(50), "{{\"{}\":".format(key))

    def test_save_User_obj(self):
        a = User()
        objdict = FileStorage().all()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        objdict[key] = a
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_save_Place_obj(self):
        a = Place()
        objdict = FileStorage().all()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        objdict[key] = a
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_save_State_obj(self):
        a = State()
        objdict = FileStorage().all()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        objdict[key] = a
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(f.read(46), "{{\"{}\":".format(key))

    def test_save_City_obj(self):
        a = City()
        objdict = FileStorage().all()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        objdict[key] = a
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(f.read(45), "{{\"{}\":".format(key))

    def test_save_Review_obj(self):
        a = Review()
        objdict = FileStorage().all()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        objdict[key] = a
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(f.read(47), "{{\"{}\":".format(key))

    def test_save_multiple_obj(self):
        a = Review()
        b = User()
        objdict = FileStorage().all()
        for obj in [a, b]:
            objdict["{}.{}".format(obj.__class__.__name__, obj.id)]
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual(408, len(f.read()))

    def test_save_empty_objdict(self):
        objdict = FileStorage().all()
        objdict.clear()
        FileStorage().save()
        with open('file.json', 'r') as f:
            self.assertEqual('{}', f.read())

    def test_save_int_arg(self):
        objdict = FileStorage().all()
        with self.assertRaises(TypeError):
            FileStorage().save(1)


class FileStorage_reload_test(unittest.TestCase):
    """This class tests the reload method of the FileStorage
    class instance.
    """
    def test_reload_non_existent_file(self):
        objdict = FileStorage().all()
        objdict.clear()
        try:
            os.remove('file.json')
        except Exception:
            pass
        FileStorage().reload()
        self.assertEqual({}, objdict)

    def test_reload_empty_file(self):
        objdict = FileStorage().all()
        objdict.clear()
        try:
            with open('file.json', 'w') as f:
                f.write('')
        except Exception:
            pass
        with self.assertRaises(json.decoder.JSONDecodeError):
            FileStorage().reload()

    def test_reload_BaseModel_obj_in_file(self):
        objdict = FileStorage().all()
        objdict.clear()
        key = "BaseModel.83078107-d20d-4ec2-9a74-ec9c1fac7139"
        try:
            with open('file.json', 'w') as f:
                f.write('{{"{}": '.format(key))
                f.write('{"id": "83078107-d20d-4ec2-9a74-ec9c1fac7139", '
                        '"created_at": "2024-03-09T21:03:57.786441", '
                        '"updated_at": "2024-03-09T21:03:57.786445", '
                        '"__class__": "BaseModel"}}')
        except Exception:
            pass
        FileStorage().reload()
        self.assertEqual('BaseModel.83078107-d20d-4ec2-9a74-ec9c1fac7139',
                         "{}.{}".format(objdict[key].__class__.__name__,
                                        objdict[key].id))

    def test_reload_fake_obj(self):
        objdict = FileStorage().all()
        objdict.clear()
        key = "FakeObj.123456"
        try:
            with open('file.json', 'w') as f:
                f.write('{{"{}": '.format(key))
                f.write('{"id": "123456", '
                        '"created_at": "2024-03-09T21:03:57.786441", '
                        '"updated_at": "2024-03-09T21:03:57.786445", '
                        '"__class__": "BaseModel"}}')
        except Exception:
            pass
        FileStorage().reload()
        self.assertEqual(objdict[key].__class__.__name__, "BaseModel")

    def test_reload_int_in_Json(self):
        objdict = FileStorage().all()
        objdict.clear()
        a = 1
        try:
            with open('file.json', 'w', encoding='utf-8') as f:
                json.dump(a, f)
        except Exception:
            pass
        with self.assertRaises(AttributeError):
            FileStorage().reload()

    def test_reload_list_in_Json(self):
        objdict = FileStorage().all()
        objdict.clear()
        a = [1, 23, "abdu"]
        try:
            with open('file.json', 'w', encoding='utf-8') as f:
                json.dump(a, f)
        except Exception:
            pass
        with self.assertRaises(AttributeError):
            FileStorage().reload()

    def test_reload_String_in_Json(self):
        objdict = FileStorage().all()
        objdict.clear()
        a = "abdu"
        try:
            with open('file.json', 'w', encoding='utf-8') as f:
                json.dump(a, f)
        except Exception:
            pass
        with self.assertRaises(AttributeError):
            FileStorage().reload()

    def test_reload_dict_in_Json(self):
        objdict = FileStorage().all()
        objdict.clear()
        a = dict(name="abdu", age=28, __class__="BaseModel")
        print(a)
        try:
            with open('file.json', 'w', encoding='utf-8') as f:
                json.dump(a, f)
        except Exception:
            pass
        with self.assertRaises(TypeError):
            FileStorage().reload()


if __name__ == "__main__":
    unittest.main()
