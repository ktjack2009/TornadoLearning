from tornado.web import RequestHandler


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    # get请求方式
    def get(self, *args, **kwargs):
        # 响应信息
        self.write('hello world')


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('this is home page')
