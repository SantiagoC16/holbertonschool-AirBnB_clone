#!/usr/bin/python3
"""Base model AirBnB"""
import json
import uuid
import datetime


class BaseModel:
    def __init__(self):
        """def init"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = 

    def __str__(self):
        """str"""
        return "[{}] (<{}>) <{}>".format(BaseModel.__name__, self.id, self.__dict___)
    
    def save(self):
        """save"""

    def to_dict(self):
        """dict"""
