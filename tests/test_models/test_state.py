#!/usr/bin/python3
'''
Test State
'''
import unittest
from models.base_model import BaseModel
from models import state
from datetime import datetime


class TestState(unittest.TestCase):
    '''Test the State class'''

    def setUp(self):
        '''Set uo class'''
        self.state = state.State()
        self.state.name = "Gauteng"
        self.state.save()

    def test_documentataion(self):
        '''Test documentation of state'''
        self.assertIsNotNone(state.__doc__)
        self.assertIsNotNone(self.state.__doc__)

    def test_inheritance(self):
        '''Test inheritance from BseModel class'''
        self.assertTrue(issubclass(state.State, BaseModel))

    def test_name(self):
        '''Test that name is added'''
        self.assertTrue(isinstance(self.state.name, str))
        self.assertIs(self.state.name, "Gauteng")

    def test_methods_base_model(self):
        '''Test that BaseModel methods work'''
        self.assertNotEqual(self.state.created_at, self.state.updated_at)
        self.assertIn("id", self.state.__dict__)
        self.assertEqual('to_dict' in dir(self.state), True)
        self.assertIn("name", self.state.__dict__)


if __name__ == "__main__":
    unittest.main()
