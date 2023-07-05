#!/usr/bin/python3
"""define FileStorage class"""
import os
from models.base_model import BaseModel

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
        """ sets in __objects the obj with 
        key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
