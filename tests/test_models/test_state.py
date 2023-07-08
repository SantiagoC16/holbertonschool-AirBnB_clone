#!/usr/bin/python3
"""unitest for state model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestUser(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_exist(self):
        """test create exist"""
        self.assertTrue(hasattr(self.city, "name"))

    def test_empty(self):
        """test create empty attibute"""
        self.assertEqual(self.city.name, "")

if __name__ == '__main__':
    unittest.main()
