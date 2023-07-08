#!/usr/bin/python3
"""unittest for class User"""
import unittest
from models.user import User
from models.base_model import BaseModel

class User(BaseModel):
    """class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
