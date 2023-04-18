from datetime import time,datetime

from comment.models import db

class UserModel(db.Model):
    __tablename__='t_user'
    id=db.Column(db.BIGINT,primary_key=True,autoincrement=True)
    name=db.Column(db.String(11),doc='用户名称')
    phone=db.Column(db.String(64),doc='手机号码')
    password=db.Column(db.String(64),doc='用户密码')
    icon=db.Column(db.String(5000),doc='用户头像')
    note=db.Column(db.String(500),doc='备注')
    create_time=db.Column(db.DateTime,default=datetime.now(),doc='注册时间')
    update_time=db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now(),doc='注册时间')

