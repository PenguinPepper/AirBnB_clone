#!/usr/bin/python3
import json
from models.engine import file_storage
import unittest
'''Test cases for FileStorage class
'''


class TestFileStorage(unittest.TestCase):
    '''Test the FileStorage class'''

    def test_documentation(self):
        '''Test that the module and class is well documentated'''
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(file_storage.FileStorage.__doc__)

    def test_method(self):
        '''Test true'''
        self.assertTrue(True)

    def test_instances(self):
        '''Test that instance is created of class FileStorage'''
        storage = file_storage.FileStorage()
        self.assertIs(storage.__class__.__name__, "FileStorage")

    def test_new(self):
        pass


if __name__ == "__main__":
    unittest.main()
