
import asyncio, os, inspect, logging, functools,sys,re
from web.RequestHandler import RequestHandler

from aiohttp import web
from db.Dmysql import mysql

class Server:
    def __init__(self):
       self.app = None
       self.loop = None
    
    def start(self):
        self.loop = asyncio.get_event_loop()
        self.app = web.Application(loop=self.loop, middlewares=[])
        routeDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'web','routers')
        self.add_routes_dir(routeDir)
        self.add_static()

        self.app.on_startup.append(self.init_pre)
        self.app.on_cleanup.append(self.on_close)

        web.run_app(self.app, host='0.0.0.0', port=9000)
        print('server is done!')


    async def init_pre(self,app):
        '''
        启动前的初始化工作
        '''
        print(app,self.app)
        await mysql.initpool(loop=self.loop,user='root', password='root', database='awesome')
    
    async def on_close(self,app):
        print('close....',app)
        await mysql.closepool()

    def add_static(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','www', 'static')
        self.app.router.add_static('/static/', path)
        logging.info('add static %s => %s' % ('/static/', path))
    
    def add_route(self,fn):
        method = getattr(fn, '__method__', None)
        path = getattr(fn, '__route__', None)
        if path is None or method is None:
            raise ValueError('@get or @post not defined in %s.' % str(fn))
        if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
            fn = asyncio.coroutine(fn)
        logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
        self.app.router.add_route(method, path, RequestHandler(self.app, fn))

    def add_routes(self,module_name):
        n = module_name.rfind('.')
        if n == (-1):
            mod = __import__(module_name, globals(), locals())
        else:
            name = module_name[n+1:]
            mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
        for attr in dir(mod):
            if attr.startswith('_'):
                continue
            fn = getattr(mod, attr)
            if callable(fn):
                method = getattr(fn, '__method__', None)
                path = getattr(fn, '__route__', None)
                if method and path:
                    self.add_route(fn)


    def add_routes_dir(self,rootDir):
        '''
        将routers目录下的所有路由模块加入到路由中
        '''
        old_path = os.path.dirname(os.path.abspath(__file__))
        for dirName, subdirList, fileList in os.walk(rootDir):
            sys.path.append(dirName)
            for fname in fileList:
                if re.match(r'[_,a-z,A-Z]+.py$', fname):
                    mod_name = fname.split('.')[0]
                    self.add_routes(mod_name)          
            if len(subdirList) > 0:
                subdirList = subdirList[1:]
        sys.path.append(old_path)

server = Server()