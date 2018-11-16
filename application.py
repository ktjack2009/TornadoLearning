import tornado.web
import config
from views import index
from tornado.web import url


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler, {'word1': 'good', 'word2': 'nice'}),
            url(r'/link', index.LinkHandler, {'content': '点击后的内容'}, name='link_url'),
            (r'/json', index.JsonHandler, ),
            (r'/testP/(\w+)/(\w+)/', index.TestPHandler),
        ]
        super(Application, self).__init__(handlers=handlers, **config.settings)
