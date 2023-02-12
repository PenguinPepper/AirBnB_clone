#!/usr/bin/python3
"""
File Storage Model Doc
"""
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):

        return self.__objects

    def new(self, obj):

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):

        with open(self.__file_path, "w") as f:
            export = {}
            for key, value in self.__objects.items():
                export[key] = value.to_dict()
            json.dump(export, f)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path) as f:
                chunk = json.load(f)
                for key, value in chunk.items():
                    class_ = key.split(".")[0]
                    self.__objects[key] = eval(class_)(**value)
        except FileNotFoundError:
            pass
