from flask import Flask

# 创建一个 Flask 应用实例
app = Flask(__name__)

# 定义一个路由，告诉 Flask 当用户访问网站根目录 (/) 时该做什么
@app.route('/')
def hello_world():
    # 返回要在浏览器中显示的文本
    return 'Hello, World!'

# 这段代码确保只有在直接运行此脚本时，开发服务器才会启动
if __name__ == '__main__':
    app.run(debug=True)