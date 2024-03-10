#!/usr/bin/python3
"""This module describes the unittests for base_model

"""
import unittest
import os
import datetime
import io
import sys
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

        with self.assertRaises(TypeError):
            BaseModel.__init__()

    def test_instantiation_None_arg(self):
        """This method tests the instantiation of BaseModel with many args"""

        with self.assertRaises(AttributeError):
            BaseModel.__init__(None)

    def test_instantiation_int_arg(self):
        """This method tests the instantiation of BaseMode with an int arg"""

        with self.assertRaises(AttributeError):
            BaseModel.__init__(1, 1, 2, 4, 5)

    def test_instantiation_bytes_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(b'Bytes', b'Python', b'Simple')

    def test_instantiation_str_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__("Invalid", "Strings", "Mental")

    def test_instantiation_empty_str_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__("")

    def test_instantiation_bool_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(True)

    def test_instantiation_zero_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(0, 0, 0, 0, 0, 0)

    def test_instantiation_float_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(11.1, 12.8, 54.34, 5.009, 32.9)

    def test_instantiation_neg_val_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(-10, -9, -6, -500)

    def test_instantiation_set_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__({1, 2}, {80, 4, 56, 6}, {89, -98})

    def test_instantiation_tupl_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__((1, 2), )

    def test_instantiation_list_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(['string', 3, 6.8])

    def test_instantiation_dict_arg(self):
        with self.assertRaises(AttributeError):
            now = datetime.datetime.now()
            BaseModel.__init__({'id': 'Holberton', 'created_at': now})

    def test_instantiation_inf_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(float('inf'))

    def test_instantiation_nan_arg(self):
        with self.assertRaises(AttributeError):
            BaseModel.__init__(float('nan'))

    def test_instantiation_kwargs_class_id_other(self):
        now = datetime.datetime.now()
        kwargs = {'__class__': BaseModel,
                  'id': "888800008888",
                  'created_at': str(now),
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_other(self):
        now = datetime.datetime.now()
        kwargs = {'created_at': str(now),
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_other_no_ca(self):
        now = datetime.datetime.now()
        kwargs = {'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_other_no_ca_ua(self):
        kwargs = {'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_other_no_ca_ua_fn(self):
        kwargs = {'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_other_no_ca_ua_fn_ln(self):
        kwargs = {'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_other_no_ca_ua_fn_ln_email(self):
        kwargs = {'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_other_no_ca_ua_fn_ln_email_a(self):
        kwargs = {'weight': 100.048}
        a = BaseModel(**kwargs)
        with self.assertRaises(AttributeError):
            print(a)

    def test_instantiation_kwargs_empty(self):
        kwargs = {}
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_None(self):
        kwargs = None
        with self.assertRaises(TypeError):
            BaseModel(**kwargs)

    def test_instantiation_kwargs_id_other(self):
        now = datetime.datetime.now()
        kwargs = {'id': "888800008888",
                  'created_at': str(now),
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca(self):
        now = datetime.datetime.now()
        kwargs = {'id': "888800008888",
                  'update_at': str(now + datetime.timedelta(days=1)),
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua(self):
        kwargs = {'id': "888800008888",
                  'first_name': 'Betty',
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn(self):
        kwargs = {'id': "888800008888",
                  'last_name': 'Holberton',
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn_ln(self):
        kwargs = {'id': "888800008888",
                  'email': 'hbtn@sch.com',
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn_ln_email(self):
        kwargs = {'id': "888800008888",
                  'age': 98,
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id_other_no_ca_ua_fn_ln_email_a(self):
        kwargs = {'id': "888800008888",
                  'weight': 100.048
                  }
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))

    def test_instantiation_kwargs_id(self):
        kwargs = {'id': "888800008888"}
        a = BaseModel(**kwargs)
        self.assertEqual("[{}] ({}) {}".format(a.__class__.__name__,
                                               a.id,
                                               a.__dict__), str(a))


class TestBaseModel_str(unittest.TestCase):
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
        a = BaseModel()
        self.assertEqual(a.__str__(),
                         "[BaseModel] ({}) {}".format(a.id, a.__dict__))

    def test_str_cast_func(self):
        a = BaseModel()
        self.assertEqual(str(a),
                         "[BaseModel] ({}) {}".format(a.id, a.__dict__))

    def test_print_function(self):
        a = BaseModel()
        print(a)
        self.assertEqual(self.output.getvalue(),
                         "[BaseModel] ({}) {}\n".format(a.id, a.__dict__))


class TestBaseModel_save(unittest.TestCase):
    def tearDown(self):
        try:
            FileStorage._FileStorage__objects = {}
            if os.path.isfile(FileStorage._FileStorage__file_path):
                os.remove(FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def setUp(self):
        objdict = FileStorage().all()
        objdict.clear()
        FileStorage().save()

    def test_save_BaseModel_normal(self):
        a = BaseModel()
        key = "{}.{}".format(a.__class__.__name__, a.id)
        a.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            self.assertEqual(f.read(50), "{{\"{}\":".format(key))


class TestBaseModel_to_dict(unittest.TestCase):
    """This class tests the to_dict method of a Place
    class instance
    """
    def test_no_arg(self):
        a = BaseModel()
        self.assertIsInstance(a.to_dict(), dict)

    def test_one_arg(self):
        a = BaseModel()
        with self.assertRaises(TypeError):
            a.to_dict(1)

    def test_newattr_arg(self):
        a = BaseModel()
        a.name = "abdu"
        dictionary = a.to_dict()
        self.assertEqual(dictionary['name'], "abdu")

    def test_class_attr(self):
        a = BaseModel()
        dictionary = a.to_dict()
        self.assertEqual(dictionary['__class__'], "BaseModel")

    def test_created_at_attr(self):
        a = BaseModel()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['created_at'], str)

    def test_updated_at_attr(self):
        a = BaseModel()
        dictionary = a.to_dict()
        self.assertIsInstance(dictionary['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
