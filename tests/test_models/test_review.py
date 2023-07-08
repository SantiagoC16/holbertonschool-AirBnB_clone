#!/usr/bin/python3
"""unitest for review model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestUser(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_exist(self):
        """test create exist"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_empty(self):
        """test create empty attibute"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
