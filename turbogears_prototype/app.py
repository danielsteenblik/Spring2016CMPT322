from wsgiref.simple_server import make_server
from tg import expose, TGController, AppConfig

class RootController(TGController):
     @expose()
     def index(self):
         return "<h1>Hello World</h1>"

class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World'

    @expose('hello.jinja')
    def hello(self, person=None):
        return dict(person=person)

config = AppConfig(minimal=True, root_controller=RootController())
config.renderers = ['jinja']
config.serve_static = True
config.paths['static_files'] = 'public'

import webhelpers2
import webhelpers2.text
config['helpers'] = webhelpers2

application = config.make_wsgi_app()

print "Serving on port 80..."
httpd = make_server('', 80, application)
httpd.serve_forever()
