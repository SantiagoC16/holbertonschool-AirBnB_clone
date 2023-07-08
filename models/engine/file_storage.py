#!/usr/bin/python3
"""define FileStorage class"""
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        self.file_storage = None

    def test_all(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertEqual(objects, {'BaseModel.' + obj.id: obj})

    def test_new(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        objects = self.file_storage.all()
        self.assertEqual(objects, {'BaseModel.' + obj.id: obj})

    def test_save(self):
        obj = BaseModel()
        self.file_storage.new(obj)

        with patch('models.engine.file_storage.open', mock_open()) as mock_file:
            self.file_storage.save()
            mock_file.assert_called_once_with("file.json", "w")
            mock_file().write.assert_called_once()

    def test_reload(self):
        obj = BaseModel()
        self.file_storage.new(obj)

        json_data = {
            'BaseModel.' + obj.id: obj.to_dict()
        }
        json_string = StringIO(json.dumps(json_data))

        with patch('models.engine.file_storage.open', mock_open(read_data=json_string.getvalue())):
            self.file_storage.reload()
            objects = self.file_storage.all()
            self.assertEqual(objects, {'BaseModel.' + obj.id: obj})


if __name__ == '__main__':
    unittest.main()
