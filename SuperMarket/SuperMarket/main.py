#项目入口
from SuperMarket import create_app

app=create_app('develop')

if __name__ == '__main__':
    app.run()