import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.web import RequestHandler
from tornado.options import define, options, parse_config_file

define("port", type=int, default=8888, help="服务器端口")


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    # get请求方式
    def get(self, *args, **kwargs):
        # 响应信息
        self.write('hello world')


if __name__ == '__main__':
    parse_config_file('./config')
    app = tornado.web.Application([
        ('/', IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)  # 创建服务器
    http_server.bind(options.port)  # 服务器绑定到指定端口
    http_server.start(num_processes=1)  # 开启多进程，num_processes默认为1，None 或 <=0则根据cpu
    tornado.ioloop.IOLoop.current().start()  # 不断的循环询问epoll
