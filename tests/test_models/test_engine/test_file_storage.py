#!/usr/bin/python3
""" unittest from parent class fileStorage """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage """

    def setUp(self):
        """test setup"""
        self.path = "file.json"
        self.storage = FileStorage()
        

    def tearDown(self):
        """test teardown"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """ test all method """
        self.assertAlmostEqual(self.storage.all(), {})
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ test new method """
        obj = BaseModel()
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertAlmostEqual(len(self.storage.all()), 1)
        self.assertAlmostEqual(key in self.storage.all(), True)

    def test_save(self):
        """ test save method """
        obj = BaseModel()
        self.storage.save()
        self.assertAlmostEqual(os.path.exists(self.path), True)
        with open(self.path, mode="r") as file:
            text = json.load(file)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, text)

    def test_reload(self):
        """ test reload"""
        json_data = {
            "BaseModel.1234": {
                "id": "1234",
                "name": "Test",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00"
            }
        }
        with open(self.file_path, "w") as f:
            json.dump(json_data, f)
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        base_model_key = "BaseModel.1234"
        self.assertIn(base_model_key, objects)
        base_model = objects[base_model_key]
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.id, "1234")
        self.assertEqual(base_model.name, "Test")

if __name__ == "__main__":
    unittest.main()
