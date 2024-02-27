#!/usr/bin/env python3
"""
input data
"""
from models.base import BaseModel, Base
from sqlalchemy import Column, String, JSON


class InputData(BaseModel, Base):
    """
    data
    """
    __tablename__ = "input_data"
    ip = Column(String(100), nullable=False)
    data = Column(String(3000), nullable=False)
    prediction = Column(JSON, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        init
        """
        new_kwargs = {}
        if kwargs:
            for key, val in kwargs.items():
                if key in ["ip", "IP", "Ip"]:
                    if len(val) > 100:
                        val = f"{val[:97]}..."
                if key in ["data", "Data", "DATA"]:
                    if len(val) > 3000:
                        val = f"{val[:29997]}..."
                new_kwargs[key] = val

        super().__init__(*args, **new_kwargs)
