#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """FileStorage class for serialization and deserialization."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(FileStorage.__file_path,
                  mode='w', encoding='utf-8') as f:
            new_dict = {k: v.to_dict() for k, v
                        in FileStorage.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8')
            as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name = v['__class__']
                    del v['__class__']
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass
