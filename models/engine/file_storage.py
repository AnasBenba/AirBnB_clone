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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Amenity": Amenity,
                "City": City,
                "Place": Place,
                "State": State,
                "Review": Review
                }
        return classes

    def check_class(self):
        """Returns a dictionary of valid classes and their attributes"""
        attr = {
            "BaseModel": {
                "id": "",
                "created_at": "",
                "updated_at": ""
            },
            "User": {
                "email": "",
                "password": "",
                "first_name": "",
                "last_name": ""
            },
            "Place": {
                "name": "",
                "city_id": "",
                "user_id": "",
                "description": "",
                "number_rooms": 0,
                "number_bathrooms": 0,
                "max_guest": 0,
                "price_by_night": 0,
                "latitude": 0.0,
                "longitude": 0.0,
                "amenity_ids": "",
            },
            "State": {
                "name": ""
            },
            "City": {
                "state_id": "",
                "name": ""
            },
            "Review": {
                "user_id": "",
                "place_id": "",
                "text": ""
            },
            "amenity": {
                "name": ""
            }
        }
        return attr

    def reload(self):
        """
        Deserialize objects from the JSON file
        and reload them 0o the FileStorage.
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
