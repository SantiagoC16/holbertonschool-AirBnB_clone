#!/usr/bin/python3
"""Base model AirBnB"""
import json
import os
import sys
import uuid


class Base:
    def __init__(self, id, created_at, updated_at):
        """def init"""

        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        """save"""

    def to_dict(self):
        """dict"""

    def __str__(self):
        """str"""
