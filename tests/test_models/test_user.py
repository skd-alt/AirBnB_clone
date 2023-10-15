#!/usr/bin/python3
# models/user.py
"""Unittests for User()."""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for User"""

    def test_class_attr(self):
        u1 = User()
        self.assertIn("email", dir(u1))
        self.assertEqual(str, type(u1.email))
        self.assertIn("password", dir(u1))
        self.assertEqual(str, type(u1.password))
        self.assertIn("first_name", dir(u1))
        self.assertEqual(str, type(u1.first_name))
        self.assertIn("last_name", dir(u1))
        self.assertEqual(str, type(u1.last_name))
