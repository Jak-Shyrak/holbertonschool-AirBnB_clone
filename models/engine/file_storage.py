#!/usr/bin/python3
"""
-
FileStorage class module
-
"""


import json


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionnary
        """
        return self.__objects

    def new(self, obj):
        """
        Sets obj in __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dict_to_save = {}
        for key, obj in self.__objects.items():
            dict_to_save[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict_to_save, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    inst_cls = eval(cls_name)(**value)
                    self.__objects[key] = inst_cls
        except FileNotFoundError:
            pass
