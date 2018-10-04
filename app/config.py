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
    # DATABASE_URL = 'postgres://hscqqcrrhcgcpn:30b46f80b9e83ac37a9fca1545fdda836058d1e73f52a7723fb51d77af4dc3a1@ec2-54-235-90-0.compute-1.amazonaws.com:5432/d3oceli53i6eg7'
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
