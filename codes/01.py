import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.web import RequestHandler
from tornado.options import define, options

define("port", type=int, default=8000, help="服务器端口")

'''
tornado.ioloop：
    tornado的核心io循环模块，封装了Linux的epoll和BSD的kqueue，高性能的基石
tornado.httpserver：
    tornado的HTTP服务器实现
    
epoll:
    
Application：web应用框架的核心，是与服务器对接的接口，里面保存了路由信息表，其初始化第一个参数就是一个路由
    信息映射元祖的列表
RequestHandler:
    封装了对应一个请求的所有信息和方法，write（响应信息）就是写响应的一个方法；对应每一种http请求方式（get、post
    等），把对应的处理逻辑写进同名的成员方法中
'''


# 类比Django中的视图，处理请求
class IndexHandler(RequestHandler):
    "主页处理类"

    def get(self):
        "get请求方式"
        self.write('<a href="{}">cpp</a>'.format(self.reverse_url("cpp_url")))


if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()  # 不断的循环询问epoll
