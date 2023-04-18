#项目配置

class Config:
    # 配置数据库和SQLAlchemy
    HOSTNAME = '192.168.221.129'
    PORT = '3306'
    DATABASE = 'supermarket'
    USERNAME = 'root'
    PASSWORD = 'root'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                            password=PASSWORD,
                                                                                            host=HOSTNAME, port=PORT,
                                                                                db=DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不需要跟踪数据的修改

    # 日志的配置
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FILE_DIR = 'logs/'
    LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
    LOGGING_FILE_BACKUP = 100

# 开发环境下的配置信息
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True  # 打印sql


# 生产环境中的配置信息
class ProductConfig(Config):
    pass
