#!/usr/bin/python3
# models/city.py
"""Unittests for City()."""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for City"""

    def test_class_attr(self):
        u1 = City()
        self.assertIn("state_id", dir(u1))
        self.assertEqual(str, type(u1.state_id))
        self.assertIn("name", dir(u1))
        self.assertEqual(str, type(u1.name))
