引言 = '''
以Django为代表的python web应用部署时采用wsgi协议与服务器对接（被服务器托管），
而这类服务器通常都是基于多线程的，也就是说每一个网络请求服务器都会有一个对应的线
程来用web应用（如Django）进行处理。

两类场景：
	1. 用户量大、高并发
	2. 大量的HTTP持久连接
	对于这两种情况，通常基于多线程的服务器很难应对。

C10K问题：并发10000个连接，对于单台服务器而言，根本无法承担，而采用多台服务器分布式又意味着高昂的成本。

Tornado使用了单线程事件循环，所以意味着所有的应用代码必须是异步非阻塞的

异步（协程）的写法：
from tornado.httpclient import AsyncHTTPClient

async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

老版本的写法：
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

@gen.coroutine
def async_fetch_gen(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)

协程起到的作用类似于：
from tornado.concurrent import Future
def async_fetch_manual(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    def on_fetch(f):
        my_future.set_result(f.result().body)
    fetch_future.add_done_callback(on_fetch)
    return my_future
'''

L_1 = '''
Tornado特点：
	1. 轻量级web框架，拥有异步非阻塞IO的处理方式
	2. 出色的抗负载能力

tornado.web:
    > 基础web框架模块
tornado.ioloop:
    > tornado的核心io循环模块，封装了Linux的epoll和BSD的kqueue，高性能的基石
tornado.httpserver:
    > tornado的HTTP服务器实现
app.listen:
    > 这个方法只能用在单进程中
Application：
    > web应用框架的核心，是与服务器对接的接口，里面保存了路由信息表，其初始化第一个参数就是一个路由信息映射元祖的列表
RequestHandler:
    > 封装了对应一个请求的所有信息和方法，write（响应信息）就是写响应的一个方法；对应每一种http请求方式
        （get、post等），把对应的处理逻辑写进同名的成员方法中
    
关于多进程：
    > 虽然tornado提供了一次开启多个进程的方法，但由于每个子进程都会从父进程中复制一份IOLoop实例，那么会影响到每一个子进程，
    势必会干扰到子进程IOLoop的工作
    > 所有进程是由一个命令一次开启的，也就无法做到在不停服务的情况下更新代码
    > 所有进程共享同一个端口，想要分别单独监控每一个进程就很困难
    > 不建议使用这种多进程的方式，而是手动开启多个进程，并且绑定不同的端口

options:
    > tornado为我们提供了一个便捷的工具，tornado.options模块——全局参数定义、存储、转换
tornado.options.define()
    > name: 选项变量名，须保证全局唯一性
    > default: 选项变量的默认值
    > type: 
'''
L_2 = '''
接口调用顺序：
    > set_default_headers() 如果抛出异常，需要再调用一次，修改header信息
    > initialize() 初始化
    > prepare() 预处理方法，类似middleware
    > http方法：get/post/head/delete/put/patch/optionss
    > write_error(): 抛出异常后，调用
    > on_finish: http方法完成后调用
'''

L_3 = '''
模版：
    > 配置路径：template_path
    > 渲染模版 self.render('index.html')
    > 变量与表达式可以传函数
    > 流程控制：if/for/while 和Django类似 {% if 表达式 %} {% elif 表达式2 %} {% else %} {% end %}
    > 转义：默认开启，关闭转义使用 {% raw str %}(关闭一行) {% autoescape None %}(页面关闭)
        开启转义：escape()函数
    > 继承：{% block main %}{% end %} {% extends "base.html" %}
    
静态文件：
    > 配置路径：static_path
    > StaticFileHandler：可以用来映射静态文件

数据库：
    > 没有自带的ORM，对于数据库需要自己去适配
'''

L_4 = '''
应用安全：
    > cookie
    > XSRF：跨站请求伪造（同源策略）
    > 用户验证
'''
