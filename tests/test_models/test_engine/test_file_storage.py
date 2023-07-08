import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.user = User()
        self.base_model = BaseModel()

    def tearDown(self):
        self.storage = None
        self.user = None
        self.base_model = None
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        self.storage.new(self.user)
        key = "User.{}".format(self.user.id)
        self.assertEqual(self.storage.all()[key], self.user)

    def test_save(self):
        self.storage.new(self.user)
        self.storage.new(self.base_model)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.storage.save()
            expected_output = "{}\n".format(json.dumps({
                "User.{}".format(self.user.id): self.user.to_dict(),
                "BaseModel.{}".format(self.base_model.id): self.base_model.to_dict()
            }))
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_reload(self):
        self.storage.new(self.user)
        self.storage.save()
        self.storage.reload()
        key = "User.{}".format(self.user.id)
        self.assertEqual(type(self.storage.all()[key]), User)
        self.assertEqual(self.storage.all()[key].id, self.user.id)

if __name__ == '__main__':
    unittest.main()
