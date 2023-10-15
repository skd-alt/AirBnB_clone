#!/usr/bin/python3
# models/base_model.py
"""Unittests for BaseModel()."""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_id_is_str(self):
        """Test if id is string"""
        b1 = BaseModel()
        self.assertEqual(str, type(b1.id))

    def test_id_unique(self):
        """test if two ids are unique & Created date are also different"""
        b2 = BaseModel()
        b3 = BaseModel()
        self.assertNotEqual(b2.id, b3.id)
        self.assertLess(b2.created_at, b3.created_at)
        self.assertLess(b2.updated_at, b3.updated_at)

    def test_str_representation(self):
        """Print object gives str"""
        b4 = BaseModel()
        b4.id = "123"
        b4.created_at = "2023-10-19"
        b4.updated_at = "2023-10-19"
        self.assertEqual("[BaseModel] (123) {'id': '123', 'created_at': '2023-10-19', 'updated_at': '2023-10-19'}", b4.__str__())

    def test_save(self):
        b5 = BaseModel()
        date1 = b5.updated_at
        date2 = b5.created_at
        id5 = b5.id
        b5.save()
        self.assertLess(date1, b5.updated_at)
        self.assertEqual(date2, b5.created_at)
        self.assertEqual(id5, b5.id)
