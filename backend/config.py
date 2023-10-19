import os

from dotenv import load_dotenv

load_dotenv()

BASEDIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRT_KEY = os.getenv("SECRT_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(BASEDIR, "dev.db")
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
