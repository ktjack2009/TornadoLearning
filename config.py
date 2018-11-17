import os

BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    'port': 8000,
}

# mysql配置
db_options = {
    'default': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '',
        'dbName': 'my_db',
    }
}

# 配置
'''
debug=True
    > tornado会自动重启；可以通通过autoreload=True单独设置
    > 取消缓存编译的模版；可以通过compiled_template_cache=False单独设置
    > 取消缓存静态文件的hash值；可以通过static_hash_cache=False单独设置
    > 提供追踪信息；可以通过serve_traceback=True单独设置
'''
settings = {
    'debug': True,
    'static_path': os.path.join(BASE_DIR, 'static'),
    'template_path': os.path.join(BASE_DIR, 'templates'),
    # 'autoescape': None,   # 关闭转义
}
