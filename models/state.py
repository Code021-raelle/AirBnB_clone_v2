#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete")


    if os.getenv('HBNB_TYPR_STORAGE') != 'db':
        @property
        def cities(self):
            """Return the list of City objects linked to the current state."""
            from models import storage
            from models.city import City
            city_list = []
            for key, city in storage.all(City).items():
                if city.state_id == self.id:
                    city_list.append(city)
                return city_list
