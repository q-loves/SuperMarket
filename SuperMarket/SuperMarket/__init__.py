from flask import Flask
from flask_migrate import Migrate

from SuperMarket.resources.user import user_bp
from comment.models import db
from settings import map_config


def create_app(config_type):

    #创建app
    app = Flask(__name__)
    #加载配置
    app.config.from_object(map_config.get(config_type))

    #加载日志处理工具

    #初始化sqlalchemy
    db.init_app(app)
    #初始化migrate,做数据迁移时使用
    migrate=Migrate(db=db)
    migrate.init_app(app)
    #加载蓝图
    app.register_blueprint(user_bp)

    return app