#!/usr/bin/python3
# models/amenity.py
"""Unittests for Amenity()."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for User"""

    def test_class_attr(self):
        u1 = Amenity()
        self.assertIn("name", dir(u1))
        self.assertEqual(str, type(u1.name))
