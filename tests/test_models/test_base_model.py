#!/usr/bin/python3
'''
Test cases for the BaseModel Class
'''
from models import base_model
from datetime import datetime
from uuid import uuid4
import unittest

my_model = base_model.BaseModel()
my_model2 = base_model.BaseModel()
my_model.save()


class TestBaseModel(unittest.TestCase):
    '''Test the outputs of BaseModel class'''

    def test_documentation(self):
        '''Test that the module and class is well documentated'''
        self.assertIsNotNone(base_model.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__doc__)

    def test_datatype(self):
        '''Test that the instance attributes are the correct type'''
        self.assertTrue(isinstance(my_model.id, str))
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))

    def test_init(self):
        '''Test the functionality of **kwargs'''
        date1 = datetime.now()
        kwargs = {"id": str(uuid4()),
                  "created_at": date1.isoformat(),
                  "__class__": "BaseModel",
                  "my_number": 32,
                  "extra": "extra",
                  "updated_at": datetime(2024, 12, 13, 12, 59, 52, 123456).
                  isoformat()
                  }
        my_model3 = base_model.BaseModel(**kwargs)
        self.assertEqual(my_model3.to_dict(), kwargs)

    def test_str(self):
        '''Test __str__ method'''
        hstring = str(my_model)
        outp = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                     my_model.id, my_model.__dict__)
        self.assertIn(outp, hstring)

    def test_save(self):
        '''Test save method'''
        my_model.save()
        # self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        '''Test keys to value in to_dict method'''
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_dict, dict))
        self.assertIn("created_at", my_dict)
        self.assertEqual(my_dict["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertIs(my_dict["name"], my_model.name)
        self.assertTrue(isinstance(my_dict["my_number"], int))


if __name__ == "__main__":
    unittest.main()
