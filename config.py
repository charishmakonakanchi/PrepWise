import os

class Config:

    SECRET_KEY = "prepwise-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:honey25@localhost/prepwise"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    