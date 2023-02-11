#!/usr/bin/python3
"""Module contains a class called BaseModel

    Imports:
        datetime (module)
        uuid (module)
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes:

    Attributes:
        id (string): assign when an instance is created.
        created_at (datetime): assign with
            current datetime when an instance is created.
        updated_at (datetime): assign with the current
            datetime when an instance is created and
            it will be updated everytime object is changed.
        kwargs (dictionary): dictionary of attributes.
    """

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = self.set_time(value)
                setattr(self, key, value)
        else:
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
        res.update(self.__dict__)
        res["__class__"] = __class__.__name__
        res["updated_at"] = self.str_time(self.updated_at)
        res["id"] = self.id
        res["created_at"] = self.str_time(self.created_at)

        return res

    def str_time(self, val):

        val = val.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return val

    def set_time(self, val):

        if type(val) != datetime:
            val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
        return val
