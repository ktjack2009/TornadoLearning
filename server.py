import tornado.ioloop
import tornado.httpserver
from config import settings
from application import Application

if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)  # 创建服务器
    http_server.bind(settings['port'])  # 服务器绑定到指定端口
    http_server.start(num_processes=1)  # 开启多进程，num_processes默认为1，None 或 <=0则根据cpu
    tornado.ioloop.IOLoop.current().start()  # 不断的循环询问epoll
