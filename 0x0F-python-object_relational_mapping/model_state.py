#!/usr/bin/python3
"""
Module that contains the class definition of a State and an
instance Base = declarative_base():
"""
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):

    __tablename__ = 'states'

    id = Column(Integer, Sequence('states_id_sequence'), primary_key=True)
    name = Column(String(128), nullable=False)

