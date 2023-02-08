#!/usr/bin/python3

"""
Class Module Doc: 
"""
from uuid import uuid4
from datetime import datetime, timezone


class BaseModel:


	def __init__(self):
		
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	def __str__(self):

		name = __class__.__name__
		attrs = self.__dict__

		return f"[{name}] ({self.id}) {attrs}"

	def save(self):

		self.updated_at = datetime.now()

	def to_dict(self):

		res = {}
		res["__class__"] = __class__.__name__
		res["updated_at"] = str(self.updated_at)
		res["id"] = self.id
		res["created_at"] = str(self.created_at)
		res.update(self.__dict__)

		return res

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print()
my_model.save()
print(my_model)
print()
my_model_json = my_model.to_dict()
print(my_model_json)
print()
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
