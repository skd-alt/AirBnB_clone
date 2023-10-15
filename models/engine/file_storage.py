#!/usr/bin/python3
"""File Storage Class to store created objects"""

import json
import os


class FileStorage:
    """Store and recreate objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key_obj = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """serializes to json file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dicn = {k: v.to_dict() for (k, v) in FileStorage.__objects.items()}
            json.dump(dicn, f)

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel,
                "User": User}

        return classes

    def reload(self):
        """deserializes the JSON file to __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dicn = json.load(f)
            FileStorage.__objects = {k: self.classes()[v["__class__"]](**v) for (k, v) in obj_dicn.items()}
