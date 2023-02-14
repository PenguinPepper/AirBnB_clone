#!/usr/bin/python3
'''
Test Amenity Class
'''
import unittest
from models.base_model import BaseModel
from models import amenity


class TestAmenity(unittest.TestCase):
    '''Test the Amenity class'''

    def setUp(self):
        '''Set uo class'''
        self.amenity = amenity.Amenity()
        self.amenity.name = "Amen"
        self.amenity.save()

    def test_documentataion(self):
        '''Test docstrings'''
        self.assertIsNotNone(amenity.__doc__)
        self.assertIsNotNone(self.amenity.__doc__)

    def test_inheritance(self):
        '''Test inheritance from BaseModel class'''
        self.assertTrue(issubclass(amenity.Amenity, BaseModel))

    def test_name(self):
        '''Test that name is added'''
        self.assertTrue(isinstance(self.amenity.name, str))
        self.assertIs(self.amenity.name, "Amen")

    def test_methods_base_model(self):
        '''Test that BaseModel methods work'''
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)
        self.assertEqual('to_dict' in dir(self.amenity), True)
        my_dict = self.amenity.to_dict()
        dd = self.amenity.__class__(**my_dict)
        self.assertEqual(dd.id, self.amenity.id)


if __name__ == "__main__":
    unittest.main()
