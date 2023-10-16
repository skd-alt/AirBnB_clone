#!/usr/bin/python3
# models/review.py
"""Unittests for Review()."""

import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for Review"""

    def test_class_attr(self):
        u1 = Review()
        self.assertIn("place_id", dir(u1))
        self.assertEqual(str, type(u1.place_id))
        self.assertIn("user_id", dir(u1))
        self.assertEqual(str, type(u1.user_id))
        self.assertIn("text", dir(u1))
        self.assertEqual(str, type(u1.text))
