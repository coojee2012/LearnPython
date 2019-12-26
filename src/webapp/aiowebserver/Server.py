
import asyncio, os, inspect,json, logging, functools,sys,re
from aiowebserver.RequestHandler import RequestHandler
from config import config
from aiohttp import web
# import jinja2,aiohttp_jinja2
from jinja2 import Environment, FileSystemLoader
from db.Dmysql import mysql
from db.Dredis import redis
from aiohttp_session import setup, get_session
from aiohttp_session.redis_storage import RedisStorage

class Server:
    def __init__(self):
       self.app = None
       self.loop = None
    
    def start(self):
        self.loop = asyncio.get_event_loop()
        self.app = web.Application(loop=self.loop, middlewares=[
            logger_factory,
            data_factory
        ])

        self.add_routes_dir(config.app.routedir)
        self.add_static(config.app.static)
        self.init_jinja2()
        # aiohttp_jinja2.setup(self.app, loader=jinja2.FileSystemLoader(config.app.templetdir))

        self.app.on_startup.append(self.init_pre)
        self.app.on_cleanup.append(self.on_close)

        web.run_app(self.app, host=config.app.host, port=config.app.port)
        print('server is done!')


    def init_jinja2(self, **kw):
        logging.info('init jinja2...')
        options = dict(
            autoescape = kw.get('autoescape', True),
            block_start_string = kw.get('block_start_string', '{%'),
            block_end_string = kw.get('block_end_string', '%}'),
            variable_start_string = kw.get('variable_start_string', '{{'),
            variable_end_string = kw.get('variable_end_string', '}}'),
            auto_reload = kw.get('auto_reload', True)
        )
        # path = kw.get('path', None)
        # if path is None:
        #     path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
        # logging.info('set jinja2 template path: %s' % path)
        env = Environment(loader=FileSystemLoader(config.app.templetdir), **options)
        filters = kw.get('filters', None)
        if filters is not None:
            for name, f in filters.items():
                env.filters[name] = f
        self.app['__templating__'] = env
    
    async def init_pre(self,app):
        '''
        启动前的初始化工作
        '''
        await mysql.initpool(loop=self.loop)
        await redis.init_pool(loop=self.loop)
        redis_pool = redis.get_pool()
        storage = RedisStorage(redis_pool)
        setup(app, storage)
        app.middlewares.append(response_factory) #一定要放在session的后面  先执行这个
    
    async def on_close(self,app):
        await mysql.closepool()
        await redis.close()

    def add_static(self,path):
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


async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # await asyncio.sleep(0.3)
        return (await handler(request))
    return logger

async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        return (await handler(request))
    return parse_data

async def response_factory(app, handler):
    async def response(request):
        logging.info('Response handler...')
        r = await handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and r >= 100 and r < 600:
            return web.Response(r)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response
server = Server()