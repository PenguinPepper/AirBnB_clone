#!/usr/bin/python3
'''
Test City class
'''
from models import city
from models.base_model import BaseModel
import unittest

class TestCity(unittest.TestCase):
    '''Test the class city'''

    def setUp(self):
        '''Setup class'''
        self.city = city.City()
        self.city.state_id = "34.Ga"
        self.city.name = "Johannesburg"
        self.city.save()

    def test_documentataion(self):
        '''Test documentation of state'''
        self.assertIsNotNone(city.__doc__)
        self.assertIsNotNone(self.city.__doc__)

    def test_inheritance(self):
        '''Test inheritance from BseModel class'''
        self.assertTrue(issubclass(city.City, BaseModel))

    def test_state_id(self):
        '''Test state id attribute'''
        self.assertIsInstance(self.city.state_id, str)
        self.assertIs("34.Ga", self.city.state_id)

    def test_name(self):
        '''Test name attribute'''
        self.assertIsInstance(self.city.name, str)
        self.assertIs("Johannesburg", self.city.name)

    def test_methods_base_model(self):
        '''Test that BaseModel methods work'''
        my_dict = self.city.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))

