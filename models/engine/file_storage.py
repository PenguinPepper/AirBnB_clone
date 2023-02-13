#!/usr/bin/python3
"""
File Storage Model Doc
"""
import json


class FileStorage:
    """
    Serializes instances to JSON and deserializes to instances:

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): stores all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initialize instance
        """
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """

        with open(self.__file_path, "w") as f:
            export = {}
            for key, value in self.__objects.items():
                export[key] = value.to_dict()
            json.dump(export, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__file_path) as f:
                chunk = json.load(f)
                for key, value in chunk.items():
                    class_ = key.split(".")[0]
                    print(">>>>", value.values())
                    if class_ == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    if class_ == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
