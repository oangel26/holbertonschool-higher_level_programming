#!/usr/bin/python3
"""
Module that contains the class definition of a Cite and an
instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")
