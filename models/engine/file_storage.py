#!/usr/bin/python3
"""class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class FileStorage"""

    def __init__(self):
        """
        Initialize the FileStorage instance.
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        Retrieve all objects stored in the FileStorage.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the FileStorage.
        """
        key = f'{type(obj).__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """
        Serialize objects from FileStorage and save them to a JSON file
        """
        obj = {}
        for key, value in self.__objects.items():
            obj[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj, file)

    def reload(self):
        """
        Deserialize objects from the JSON file
        and reload them into the FileStorage.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj = json.load(file)
        except FileNotFoundError:
            pass
