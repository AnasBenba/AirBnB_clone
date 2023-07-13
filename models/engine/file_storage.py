#!/usr/bin/python3
"""class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances"""
import json


class FileStorage:
    """class FileStorage"""

    __file_path = 'data.json'
    __objects = {}

    def all(self):
        """
        Retrieve all objects stored in the FileStorage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the FileStorage.
        """
        key = f'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize objects from FileStorage and save them to a JSON file
        """
        obj = {}
        for key, value in FileStorage.__objects.items():
            if isinstance(value, dict):
                obj[key] = value
            else:
                obj[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """
        Deserialize objects from the JSON file
        and reload them into the FileStorage.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj = json.load(file)
            new_obj = {}
            for key, value in obj.items():
                class_name = value['__class__']
                cls = self.classes()[class_name]
                instance = cls(**value)
                new_obj[key] = instance
            obj = new_obj
            FileStorage.__objects = obj
        except FileNotFoundError:
            pass
