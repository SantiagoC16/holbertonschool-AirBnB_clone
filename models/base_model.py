#!/usr/bin/python3
"""Base model AirBnB"""
import json
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """defines all common attributes/methods for other classes"""

        if kwargs:
            for k, v in kwargs.items():
                str_create_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                str_update_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
                if k == "created_at":
                    self.created_at = v
                    v = str_create_at
                if k == "updated_at":
                    self.updated_at = v
                    v = str_update_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """print class name, id and dict"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
