# class BaseConfig(object):
#     SQLALCHEMY_DATABASE_URI = "mysql://b1dfe25bebd0d5:babacb3a@us-cdbr-east-05.cleardb.net/heroku_653f8e9ae84c59d"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_POOL_SIZE = 3
#     SQLALCHEMY_POOL_TIMEOUT = 60
#     SQLALCHEMY_MAX_OVERFLOW = 5
#     SECRET_KEY = "horrible_secret_key"
#     LOGIN_DISABLED = True


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/american"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_MAX_OVERFLOW = 5
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True
