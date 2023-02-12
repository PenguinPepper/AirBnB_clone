#!/usr/bin/python3
"""
File Storage Model Doc
"""
import json
#from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):

        return self.__objects

    def new(self, obj):

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):

        with open(self.__file_path, "w") as f:
            export = {}
            for key, value in self.__objects.items():
                export[key] = value
				#export[key] = value.to_dict()
            json.dump(export, f)

    def reload(self):
        try:
            with open(self.__file_path) as f:
                chunk = json.load(f)
                #for key, value in chunk.items():
                #    class_ = key.split(".")[0]
                #    self.__objects[key] = eval(class_)(**value)
                self.__objects = chunk
        except FileNotFoundError:
            pass
