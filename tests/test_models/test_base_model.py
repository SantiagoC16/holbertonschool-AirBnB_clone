#!/usr/bin/python3
"""unitest for base model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dictionary(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_all_attributes(self):
        obj_dict = self.model.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_has_correct_values(self):
        obj_dict = self.model.to_dict()
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(obj_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str_representation(self):
        str_repr = str(self.model)
        self.assertIn(self.model.__class__.__name__, str_repr)
        self.assertIn(self.model.id, str_repr)
        self.assertIn(str(self.model.__dict__), str_repr)


if __name__ == '__main__':
    unittest.main()
