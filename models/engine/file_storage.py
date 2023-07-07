#!/usr/bin/python3
"""define FileStorage class"""
import json


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        from models.base_model import BaseModel

        json_dict = {}

        for k, obj in self.__objects.items():
            json_dict[k] = obj.to_dict()

            with open(self.__file_path, "w") as f:
                json.dump(json_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as f:

                for key, obj_dict in json.load(f).items():
                    obj_dict = BaseModel(**obj_dict)
                    self.__objects[key] = obj_dict

        except FileNotFoundError:
            pass
