#!/usr/bin/python3
"""
File Storage Model Doc
"""
import sys
import json
sys.path.append('..')
from models.base_model import BaseModel


class FileStorage(BaseModel):

    __file_path = "database.json"
    __objects = {}

    def all(self):

        return self.__objects

    def new(self, obj):

        self.__objects[obj.id] = obj.to_dict()

    def save(self):

        self.new(self)
        mods = self.load_json()
        print("++", mods)

        self.__objects.update(mods)
        print("obj", self.__objects)

        with open(self.__file_path, "w") as m:
            json.dump(self.__objects, m)
            #  print(">>>>", m.read())

    def reload(self):

        try:
            with open(self.__file_path) as f:
                chunk = f.read().strip()
                if chunk:
                    models = json.loads(chunk)
                else:
                    models = {}

                for value in models.values():
                    model = BaseModel(**my_model)
                    self.new(model)

            print("Suceful reload!", self.__objects, sep="\n")
        except Exception as e:
            print(e)
            print("No file found")

    def load_json(self):

        try:
            with open(self.__file_path, 'r') as f:
                c = f.read().strip()
                if c:
                    data = json.loads(c)
                    print("found")
                else:
                    data = {}
        except FileNotFoundError:
            with open(self.__file_path, "w") as f:
                pass
            print("exception! new file created")
            data = {}
            return data


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.reload()
# print(my_model)

