# default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x9d\xb9Z|=\x94\xd1^d%\x96\xa6\x1b\xe0\xd4\xf7%\xc0\xcag\xcch\x82\xe8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False