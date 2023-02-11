#!/usr/bin/python3
"""
File Storage Model Doc
"""
import sys
sys.path.append('..')
from base_model import BaseModel
import json



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
        
        with open("database.json") as f:
            remodels = json.load(f)
            print(type(remodels))

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
            with open(self._ffile_path, "w") as f:
                pass
            print("exception! new file created")
            data = {}
        return data

my_model = FileStorage()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
