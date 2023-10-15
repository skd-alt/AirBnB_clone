#!/usr/bin/python3
"""Review class inheriting from Base"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review objects is created"""
    place_id = ""
    user_id = ""
    text = ""
