import re,hashlib,json
import aiohttp_jinja2
from aiohttp import web
from aiowebserver.utils import get,post
from aiowebserver.api_errors import APIValueError,APIError
from models import User
from models.utils import next_id

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@get('/u/register')
def register_view(request):
    context = {'register': 'Andrew', 'surname': 'Svetlov'}
    response = aiohttp_jinja2.render_template('register.html',request,context)
    response.headers['Content-Language'] = 'ru'
    return response

@post('/u/register')
async def registe(*,username,password,request,**kw):
    email = kw.get('email',None)
    if not username or not username.strip():
        raise APIValueError('username')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not password or not _RE_SHA1.match(password):
        raise APIValueError('passwd')
    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, password)
    user = User(id=uid, name=username.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    await user.save()
    # make session cookie:
    r = web.Response()
    # r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

@get('/u/login')
def login_view(request):
    context = {'register': 'Andrew', 'surname': 'Svetlov'}
    response = aiohttp_jinja2.render_template('login.html',request,context)
    response.headers['Content-Language'] = 'ru'
    return response

@post('/u/login')
def login(request):
    context = {'register': 'Andrew', 'surname': 'Svetlov'}
    response = aiohttp_jinja2.render_template('register.html',request,context)
    response.headers['Content-Language'] = 'ru'
    return response