#!/usr/bin/python3
"""User calss is define inheriting from base"""
from models.base_model import BaseModel


class User(BaseModel):
    """User is created"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
