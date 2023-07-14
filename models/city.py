#!/usr/bin/python3
"""class City that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """subclass of BaseModel"""

    state_id = ''
    name = ''
