import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.web import RequestHandler
from tornado.options import define, options

define("port", type=int, default=8888, help="服务器端口")


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    def get(self):
        "get请求方式"
        self.write('hello world')


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)  # 服务器绑定到指定端口
    http_server.start(num_processes=0)  # 开启多进程，num_processes默认为1，None 或 <=0则根据cpu
    tornado.ioloop.IOLoop.current().start()  # 不断的循环询问epoll
