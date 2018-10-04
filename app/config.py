import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    """ Common configurations """

    TESTING = False
    DEBUG = False
    SECRET_KEY = "andela"


class TestingConfig(BaseConfig):

    """Configurations for Testing, with a separate test database."""

    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/test_db'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/fastfood'
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configurations
    """
    # DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/fastfood'
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
