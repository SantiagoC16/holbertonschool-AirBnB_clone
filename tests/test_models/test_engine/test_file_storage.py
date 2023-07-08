import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        # Ensure all() returns the __objects dictionary
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, self.storage._FileStorage__objects)

    def test_new(self):
        # Ensure new() adds the object to the __objects dictionary
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_attributes(self):
        """ Test __objects, __file_path """
        self.assertEqual(type(self.file_storage._FileStorage__objects), dict)
        self.assertEqual(type(self.file_storage._FileStorage__file_path), str)

    def test_save(self):
        # Mock the open() function and check if json.dump() is called
        with patch('builtins.open', mock_open()) as mock_file:
            self.storage.save()
            mock_file.assert_called_once_with(self.file_path, "w")
            mock_file().write.assert_called_once()

            # Check if the correct JSON data is written
            json_data = json.loads(mock_file().write.call_args[0][0])
            objects = self.storage.all()
            for key, obj in objects.items():
                self.assertIn(key, json_data)
                self.assertEqual(json_data[key], obj.to_dict())

    def test_reload(self):
        # Prepare mock JSON data
        json_data = {
            "BaseModel.1234": {
                "id": "1234",
                "name": "Test",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00"
            },
            "User.5678": {
                "id": "5678",
                "email": "test@example.com",
                "password": "password",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00"
            }
        }

        # Mock the open() function and simulate reading the mock JSON data
        with patch('builtins.open', mock_open(read_data=json.dumps(json_data))):
            self.storage.reload()

            # Check if objects were correctly loaded
            objects = self.storage.all()
            self.assertEqual(len(objects), 2)

            base_model_key = "BaseModel.1234"
            self.assertIn(base_model_key, objects)
            base_model = objects[base_model_key]
            self.assertIsInstance(base_model, BaseModel)
            self.assertEqual(base_model.id, "1234")
            self.assertEqual(base_model.name, "Test")

            user_key = "User.5678"
            self.assertIn(user_key, objects)
            user = objects[user_key]
            self.assertIsInstance(user, User)
            self.assertEqual(user.id, "5678")
            self.assertEqual(user.email, "test@example.com")
            self.assertEqual(user.password, "password")


if __name__ == '__main__':
    unittest.main()