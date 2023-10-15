#!/usr/bin/pythoni3
"""
    This Setups up the Base model class
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base Model class which all other classes will inherit"""

    def __init__(self):
        """initialises the attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ The string represent of base model class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public attri update_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of class"""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = type(self).__name__
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()
        return dict_rep
