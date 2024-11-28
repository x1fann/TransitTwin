from flask import Flask
from flask_cors import CORS
from routes import routes

# 初始化Flask应用
app = Flask(__name__)
CORS(app)

# 注册路由蓝图
app.register_blueprint(routes)

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)
