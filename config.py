class Config(object):
    pass

class ProConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bingxin0918@192.168.0.2:3306/test2'
    SQLALCHEMY_TRACK_MODIFICATIONS  = True


