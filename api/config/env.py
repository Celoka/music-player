import os
from config import get_env


class Config(object):
    """Base Configuration Class"""
    DEBUG = False
    SECRET = get_env("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = get_env('DATABASE_URL')


class DevConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS= True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = get_env('DATABASE_TEST_URL')
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


app_env = {
    'development': DevConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'production': ProdConfig
}
