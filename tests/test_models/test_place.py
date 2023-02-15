#!/usr/bin/python3
'''Test Place class'''
import unittest
from models.base_model import BaseModel
from models import place


class TestPlace(unittest.TestCase):
    '''Test the State class'''

    def setUp(self):
        '''Set up class'''
        self.place = place.Place()
        self.place.city_id = "5F"
        self.place.user_id = "0bj78"
        self.place.description = "Nice place"
        self.place.number_of_rooms = 4
        self.place.number_of_bathrooms = 3
        self.place.max_guests = 5
        self.place.price_by_night = 30
        self.place.latitude = 90.0
        self.place.longitude = 90.0
        self.place.amenity_ids = ["amen"]
        self.place.save()

    def test_documentation(self):
        '''Test Documentation'''
        self.assertIsNotNone(place.__doc__)
        self.assertIsNotNone(self.place.__doc__)

    def test_city_id(self):
        '''Test attribute city_id exsits'''
        self.assertTrue(isinstance(self.place.city_id, str))
        self.assertIs(self.place.city_id, "5F")

    def test_user_id(self):
        '''Test attribute user_id exsits'''
        self.assertTrue(isinstance(self.place.user_id, str))
        self.assertIs(self.place.user_id, "0bj78")

    def test_description(self):
        '''Test attribute description'''
        self.assertTrue(isinstance(self.place.description, str))
        self.assertIs(self.place.description, "Nice place")

    def test_number_of_rooms(self):
        '''Test number of rooms attribute'''
        self.assertTrue(isinstance(self.place.number_of_rooms, int))
        self.assertIs(self.place.number_of_rooms, 4)

    def test_number_of_bathrooms(self):
        '''Test number of bathrooms attribute'''
        self.assertTrue(isinstance(self.place.number_of_bathrooms, int))
        self.assertEqual(self.place.number_of_bathrooms, 3)

    def test_max_guests(self):
        '''Test max guests attribute'''
        self.assertTrue(isinstance(self.place.max_guests, int))
        self.assertEqual(self.place.max_guests, 5)

    def test_price_by_night(self):
        '''Test price by night attribute'''
        self.assertTrue(isinstance(self.place.price_by_night, int))
        self.assertEqual(self.place.price_by_night, 30)

    def test_latitude(self):
        '''Test latitude attribute'''
        self.assertTrue(isinstance(self.place.latitude, float))
        self.assertEqual(self.place.latitude, 90.0)

    def test_longitude(self):
        '''Test longitude attribute'''
        self.assertTrue(isinstance(self.place.longitude, float))
        self.assertEqual(self.place.longitude, 90.0)

    def test_amenity_ids(self):
        '''Test amenity id list'''
        self.assertTrue(isinstance(self.place.amenity_ids, list))
        self.assertEqual(self.place.amenity_ids, ["amen"])

    def test_methods_base_model(self):
        '''Test the BaseModel methods'''
        self.assertEqual("to_dict" in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
