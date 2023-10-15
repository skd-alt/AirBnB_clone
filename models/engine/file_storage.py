#!/usr/bin/python3
"""File Storage Class to store created objects"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Store and recreate objects"""
    __file_path = "./storage_file.json"
    __objects = {}

    def all(self):
        """Returns all objects."""
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key_obj = "{}.{}".format(type(obj).__name__, obj.id)
        __objects[key] = obj

    def save(self):
        """serializes to json file"""
        with open(__file_path, "w", encoding="utf-8") as f:
            dicn = {k: v.to_dict() for (k, v) in __objects.items()}
            json.dump(dicn, f)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if not os.path.isfile(__file_path):
            return

        with open(__file_path, "r", encoding="utf-8") as f:
            obj_dicn = json.load(f)
            __objects = {k: BaseModel(**v) for (k, v) in obj_dicn.items}
