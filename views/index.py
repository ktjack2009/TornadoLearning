import json
from tornado.web import RequestHandler


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    # get请求方式
    def get(self, *args, **kwargs):
        # 响应信息
        self.write('<p>hello world</p>')
        self.write('<a href="' + self.reverse_url('link_url') + '">这是链接</a>')


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
        self.write('line 5')


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
        self.write(json.dumps(json_obj))
        self.finish()
