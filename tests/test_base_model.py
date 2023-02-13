#!/usr/bin/python3
# doctest for the base_model class
from models import base_model
import unittest
import datetime
'''
Instance ID-Number
==================
Check that unique id is assigned
::
    >>> from models import base_model
    >>> my_model = base_model.BaseModel()
    >>> my_model2 = base_model.BaseModel()
    >>> my_model.id
    ...
    >>> my_model2.id
    ...

Check that the datatype is a str
::
    >>> type(my_model2.id)
    <class 'str'>
'''

my_model = base_model.BaseModel()


class TestBaseModel(unittest.TestCase):
    '''Test the outputs of BaseModel class
    '''

    def test_documentation(self):
        '''Test that the module and class is well documentated'''
        self.assertIsNotNone(base_model.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__doc__)

    def test_datatype(self):
        '''Test that the instance attributes are the correct type'''
        self.assertTrue(isinstance(my_model.id, str))
        self.assertTrue(isinstance(my_model.created_at, datetime.datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime.datetime))

    def test_save(self):
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        self.assertTrue(isinstance(my_model.to_dict(), dict))
        self.assertIn("created_at", my_model.to_dict())
        # self.assertIn(my_model.__dict__, my_model.to_dict())
        # check that datetime is now str
        # self.assertTrue(isinstance(my_model.to_dict(["created_at"], str)))
