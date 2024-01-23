import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/Profile/alice">Alice</a><br>')
        self.write('<a href="/Profile/bob">Bob</a><br>')
        self.write('<a href="/Profile/carol">Carol</a><br>')
        self.write('<a href="/Profile/dave">Dave</a><br>')
