import os


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI_PASS = os.getenv("SQLALCHEMY_DATABASE_URI_PASS")
    SQLALCHEMY_DATABASE_URI_USER = os.getenv("SQLALCHEMY_DATABASE_URI_USER")
    SQLALCHEMY_DATABASE_URI_HOST = os.getenv("SQLALCHEMY_DATABASE_URI_HOST")
    SQLALCHEMY_DATABASE_URI_DB = os.getenv("SQLALCHEMY_DATABASE_URI_DB")
    SQLALCHEMY_DATABASE_URI = (f'mysql://{SQLALCHEMY_DATABASE_URI_PASS}'
                               f':{SQLALCHEMY_DATABASE_URI_USER}'
                               f'@{SQLALCHEMY_DATABASE_URI_HOST}'
                               f'/{SQLALCHEMY_DATABASE_URI_DB}')


def __check_config_var(var_name: str):
    if Config.SQLALCHEMY_DATABASE_URI_USER is None:
        raise ValueError(f"No env variable for {var_name}")


__check_config_var("SQLALCHEMY_DATABASE_URI_PASS")
__check_config_var("SQLALCHEMY_DATABASE_URI_USER")
__check_config_var("SQLALCHEMY_DATABASE_URI_HOST")
__check_config_var("SQLALCHEMY_DATABASE_URI_DB")
