#!/usr/bin/python3
"""
User Module Doc
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an instance of the User class"""
        super().__init__(*args, **kwargs)
