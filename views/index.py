import os
from tornado.web import RequestHandler
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from config import BASE_DIR


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    # get请求方式
    def get(self, *args, **kwargs):
        # 响应信息
        # self.write('<p>hello world</p>')
        # self.write('<a href="' + self.reverse_url('link_url') + '">这是链接</a>')
        def f(x, y):
            return x + y

        params = {
            'num': 100,
            'dict_obj': {'context': 200},
            'function': f
        }
        self.render('index.html', **params)  # 渲染模版

    def post(self, *args, **kwargs):
        path = os.path.join(BASE_DIR, 'upfile', '1.jpg')
        file1 = self.request.files['file'][0]  # tornado.httputil.HTTPFile
        # filename = file1.get('filename')
        body = file1.get('body')
        # content_type = file1.get('content_type')
        with open(path, 'wb') as f:
            f.write(body)


class HomeHandler(RequestHandler):
    def initialize(self, *args, **kwargs):
        # 接收自定义参数
        self.word1 = kwargs.get('word1')
        self.word2 = kwargs.get('word2')

    def get(self, *args, **kwargs):
        self.write(f'<p>this is home page, and the params is {self.word1} and {self.word2}</p>')
        self.write('<p>line 2</p>')
        self.write('<p>line 3</p>')
        self.write('<p>line 4</p>')
        self.finish()


class LinkHandler(RequestHandler):
    def initialize(self, *args, **kwargs):
        self.content = kwargs.get('content')

    def get(self, *args, **kwargs):
        self.write(self.content)


class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        json_obj = {
            'name': 'Tom',
            'age': 18,
            'gender': 'male'
        }
        # self.request
        # print(self.request.arguments)   # 获取所有参数
        # print(self.request.cookies)     # 获取cookies
        # print(self.request.query_arguments)  # 获取url参数

        # 其它的一些方法
        self.set_header('name', 'Tom')  # 自定义响应头
        self.set_status(200)  # 设置状态码；reason为描述状态码的词组
        # self.redirect(self.reverse_url('link_url'))  # 重定向到url网址
        # self.send_error()  # 抛出http错误状态码，默认为500；抛出错误后，tornado会调用write_error()方法进行处理，然后finish

        # import json;self.write(json.dumps(json_obj))  # 手动将字典转化为json字符串
        self.write(json_obj)  # 直接返回字典（返回Content type是json）
        self.finish()

    def post(self, *args, **kwargs):
        print(self.request.body_arguments)  # 表单参数

    def set_default_headers(self):
        # 设置默认headers，在进入http响应处理方法之前被调用
        pass


class TestPHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(args)  # 正则匹配url得到的参数


# 数据库
class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        connect = self.application.db
        result = connect.fetch('select * from students where id=1')
        students = {
            'id': result[0],
            'name': result[1],
            'sex': result[2],
            'num': result[3],
        }
        self.write(students)


# 异步
import time


class AsyncHandler(RequestHandler):
    executor = ThreadPoolExecutor(10)

    @run_on_executor()
    def get(self, *args, **kwargs):
        # 耗时操作
        time.sleep(5)
        self._callback()

    def _callback(self):
        self.write('hello world')
