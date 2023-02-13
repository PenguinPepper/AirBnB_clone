#!/usr/bin/python3
from models.user import User
from models.base_model import BaseModel
import unittest
from datetime import datetime
'''Test User class
'''

class TestUser(unittest.TestCase):
    '''Methods to test User class'''


    def setUp(self):
        '''Setup class'''
        self.user = User()
        self.user.last_name = "Bar"
        self.user.first_name = "Betty"
        self.user.email = "airbnb@mail.com"
        self.user.password = "root"
        self.user.save()

    def test_inheritance(self):
        '''Test Inheritance from BaseModel'''
        self.assertTrue(issubclass(User, BaseModel))

    def test_first_name(self):
        '''Test first name'''
        self.assertTrue(isinstance(self.user.first_name, str))
        self.assertIs("Betty", self.user.first_name)

    def test_last_name(self):
        '''Test Last name'''
        self.assertTrue(isinstance(self.user.last_name, str))
        self.assertIs("Bar", self.user.last_name)

    def test_email(self):
        '''Test Email'''
        self.assertTrue(isinstance(self.user.email, str))
        self.assertIs("airbnb@mail.com", self.user.email)

    def test_password(self):
        '''Test password'''
        self.assertTrue(isinstance(self.user.password, str))
        self.assertIs("root", self.user.password)

    def test_inheritance_of_methods(self):
        '''Check that the methods of BaseModel apply to User'''
        clas_dict = self.user.to_dict()
        self.assertIn("id", clas_dict)
        self.assertTrue(isinstance(clas_dict["created_at"], str))
        self.assertTrue(isinstance(clas_dict["updated_at"], str))
        self.assertEqual(clas_dict["email"], self.user.email)
        self.assertEqual(clas_dict['__class__'], self.user.__class__.__name__)

    def test_inheritance_of_methods2(self):
        '''Check output of string method'''
        string = str(self.user)
        self.assertIn(self.user.id, string)
