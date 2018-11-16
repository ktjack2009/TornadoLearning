from tornado.web import RequestHandler


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    # get请求方式
    def get(self, *args, **kwargs):
        # 响应信息
        # self.write('<p>hello world</p>')
        # self.write('<a href="' + self.reverse_url('link_url') + '">这是链接</a>')
        self.render('index.html')  # 渲染模版


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
