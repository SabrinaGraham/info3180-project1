import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3sec5etK*y')
    SQLALCHEMY_DATABASE_URI= 'postgresql://xisutnqkorlhac:00fc88b7f98f1d56a61a541de186bb0745536fbef8e8797ffb478f18b5a85e18@ec2-3-222-204-187.compute-1.amazonaws.com:5432/degi3g6juk8mqu'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://info3180:project1@localhost/property' or 'postgresql://xisutnqkorlhac:00fc88b7f98f1d56a61a541de186bb0745536fbef8e8797ffb478f18b5a85e18@ec2-3-222-204-187.compute-1.amazonaws.com:5432/degi3g6juk8mqu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', './uploads')
