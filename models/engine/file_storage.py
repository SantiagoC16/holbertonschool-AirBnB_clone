import unittest
import json
import builtins
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        try:
            builtins.open = self.original_open
            del self.original_open
        except AttributeError:
            pass

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.storage._FileStorage__objects = data
            self.storage.save()
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """ Test __objects, __file_path """
        self.assertEqual(type(self.file_storage._FileStorage__objects), dict)
        self.assertEqual(type(self.file_storage._FileStorage__file_path), str)

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, self.storage._FileStorage__objects)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save(self):
        mock_data = {}
        for key, obj in self.storage._FileStorage__objects.items():
            mock_data[key] = obj.to_dict()

        self.original_open = builtins.open
        builtins.open = lambda file, mode: mock_open(file, mode)

        with open(self.file_path, "w") as f:
            self.storage.save()
            json_data = json.load(f)

            self.assertEqual(json_data, mock_data)

    def test_reload(self):
        mock_data = {
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

        with open(self.file_path, "w") as f:
            json.dump(mock_data, f)

        self.storage.reload()
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