#!/usr/bin/python3
# models/state.py
"""Unittests for State()."""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test for State"""

    def test_class_attr(self):
        u1 = State()
        self.assertIn("name", dir(u1))
        self.assertEqual(str, type(u1.name))
