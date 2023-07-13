#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""
import uuid
import datetime
import os
from models import storage


class BaseModel():

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    setattr(self, key, str(value))
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        String representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the object into a dictionary representation.

        Returns:
            dict: Dictionary containing the object's attributes and values.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
