#!/usr/bin/python3
"""
    Model state
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Representation of State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String(128))
