import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
	"主页处理类"
	def get(self):
		"get请求方式"
		self.write("hello itcast")


if __name__ == '__main__':
	# web应用框架的核心
	app = tornado.web.Application([
			('/', IndexHandler)
		])
	app.listen(8000)	# 绑定，没有监听
	tornado.ioloop.IOLoop.current().start()