#注册user蓝图
from flask import Blueprint
from flask_restful import Api

#注册蓝图
from SuperMarket.resources.user.tect import UserTect
from comment.utils.output import output_json

user_bp=Blueprint('users',__name__,url_prefix='/user')
#创建接口
user_api=Api(user_bp)
#修改返回参数形式
user_api.representation('application/json')(output_json)

user_api.add_resource(UserTect,'/tect',endpoint='user')