#!/usr/bin/python3
"""
Base Model
"""

import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class BaseModel():
    """
    base
    """
    now = datetime.now()
    id = Column(String(40), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=now, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        init
        """
        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)
        self.id = str(uuid4())
        self.created_at = datetime.now()

    def save(self):
        """
        saving
        """
        from models.engine import Storage
        Storage.save(self)
