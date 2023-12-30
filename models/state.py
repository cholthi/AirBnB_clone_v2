#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import shlex

print( models.__dict__)
print("==================")
class State(BaseModel, Base):
    """ State class """
    def __init__(self, *args, **kwargs):
        """
        initializes state
        """
        super().__init__(*args, **kwargs)

    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        name = ""
        @property
        def cities(self):
            """
            getter instances of cities related to the state
            """
            var = models.storage.all()
            lista = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)
