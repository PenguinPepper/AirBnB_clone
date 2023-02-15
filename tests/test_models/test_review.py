#!/usr/bin/python3
'''
Test Review class
'''
import unittest
from models.base_model import BaseModel
from models import review


class TestReview(unittest.TestCase):
    '''Test Review'''

    def setUp(self):
        '''Set up class'''
        self.review = review.Review()
        self.review.place_id = "12mk"
        self.review.user_id = "Bet35"
        self.review.text = "Had ants"
        self.review.save()

    def test_documentation(self):
        '''Test doc strings'''
        self.assertIsNotNone(review.__doc__)
        self.assertIsNotNone(review.Review.__doc__)

    def test_place_id(self):
        '''Test place id attribute'''
        self.assertTrue(isinstance(self.review.place_id, str))
        self.assertIs(self.review.place_id, "12mk")

    def test_user_id(self):
        '''Test place user id'''
        self.assertTrue(isinstance(self.review.user_id, str))
        self.assertIs(self.review.user_id, "Bet35")

    def test_test(self):
        '''Test place user id'''
        self.assertTrue(isinstance(self.review.text, str))
        self.assertIs(self.review.text, "Had ants")

    def test_methods_base_model(self):
        '''Test BaseModel methods'''
        self.assertEqual("to_dict" in dir(self.review), True)
        self.assertEqual("save" in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
