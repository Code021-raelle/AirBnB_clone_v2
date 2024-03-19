#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey(
            'places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey(
            'amenities.id'), primary_key=True, nullable=False)
        )


class Place(BaseModel, Base):
    """ Place class """
    __tablename__ = 'places'
    amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)

    # For FileStorage
    @property
    def amenities(self):
        return [amenity for amenity in models.storage.all(
            Amenity).values() if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
