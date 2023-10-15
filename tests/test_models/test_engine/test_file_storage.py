#!/usr/bin/python3
# models/engine/file_storage.py
"""Unittests for FileStorage()."""

import json
import os
from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage"""
    
    def test_class_attr(self):
        storage = FileStorage()
        self.assertIn("_FileStorage__file_path", dir(storage))
        self.assertIn("_FileStorage__objects", dir(storage))

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_new(self):
        """test new function"""
        storage = FileStorage()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        self.assertIn("BaseModel." + bm.id, storage.all().keys())
        self.assertIn(bm, storage.all().values())
        self.assertIn("User." + us.id, storage.all().keys())
        self.assertIn(us, storage.all().values())
        self.assertIn("State." + st.id, storage.all().keys())
        self.assertIn(st, storage.all().values())
        self.assertIn("Place." + pl.id, storage.all().keys())
        self.assertIn(pl, storage.all().values())
        self.assertIn("City." + cy.id, storage.all().keys())
        self.assertIn(cy, storage.all().values())
        self.assertIn("Amenity." + am.id, storage.all().keys())
        self.assertIn(am, storage.all().values())
        self.assertIn("Review." + rv.id, storage.all().keys())
        self.assertIn(rv, storage.all().values())

    def test_save(self):
        """test new function"""
        storage = FileStorage()
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        storage.new(bm)
        storage.new(us)
        storage.new(st)
        storage.new(pl)
        storage.new(cy)
        storage.new(am)
        storage.new(rv)
        storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_reload(self):
        b1 = BaseModel()
        storage = FileStorage()
        storage._FileStorage__objects = ""
        storage.reload()
        self.assertIn(b1, storage._FileStorage__objects)
