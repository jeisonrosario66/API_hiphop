# -*- coding: utf-8 -*-
from decouple import config as GETENV


class DevelopmentConfig:
    """
    object | DevelopmentConfig: Contains configurations required for the project
    """

    DEBUG = True
    MYSQL_HOST = GETENV("HOST")
    MYSQL_USER = GETENV("USER")
    MYSQL_PASSWORD = GETENV("PASSWORD")
    MYSQL_DB = GETENV("DATABASE")


config = {"development": DevelopmentConfig}
