import tornado.web
import config
from views import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler),
        ]
        super(Application, self).__init__(handlers=handlers, **config.settings)
