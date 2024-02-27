#!/usr/bin/env python3
"""
Storage //mysql
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.input_data import InputData
from models.base import BaseModel, Base
from configs.xtoxica_configs import *


class DBStorage():
    """
    db
    """
    __session = None
    __engine = None

    def __init__(self, *args, **kwargs):
        """
        init
        """
        db = db_db
        user = db_user
        host = db_host
        pwd = db_pwd

        url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(url)

    def reload(self):
        """
        reloading the db
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def save(self, obj):
        """
        saves an obj to db
        """
        self.__session.add(obj)
        self.__session.commit()
