#!/usr/bin/python3
# models/place.py
"""Unittests for Place()."""

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for Place"""

    def test_class_attr(self):
        u1 = Place()
        self.assertIn("city_id", dir(u1))
        self.assertEqual(str, type(u1.city_id))
        self.assertIn("user_id", dir(u1))
        self.assertEqual(str, type(u1.user_id))
        self.assertIn("name", dir(u1))
        self.assertEqual(str, type(u1.name))
        self.assertIn("description", dir(u1))
        self.assertEqual(str, type(u1.description))
        self.assertIn("number_rooms", dir(u1))
        self.assertEqual(int, type(u1.number_rooms))
        self.assertIn("number_bathrooms", dir(u1))
        self.assertEqual(int, type(u1.number_bathrooms))
        self.assertIn("max_guest", dir(u1))
        self.assertEqual(int, type(u1.max_guest))
        self.assertIn("price_by_night", dir(u1))
        self.assertEqual(int, type(u1.price_by_night))
        self.assertIn("latitude", dir(u1))
        self.assertEqual(float, type(u1.latitude))
        self.assertIn("longitude", dir(u1))
        self.assertEqual(float, type(u1.longitude))
        self.assertIn("amenity_ids", dir(u1))
        self.assertEqual(list, type(u1.amenity_ids))
