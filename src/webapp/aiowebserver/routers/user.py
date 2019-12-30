import re,hashlib,json
import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session
from aiowebserver.utils import get,post
from aiowebserver.api_errors import APIValueError,APIError
from models.User import User
from models.utils import next_id

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')
_RE_PASSWORD = re.compile(r'^[0-9a-f]{6,40}$')

@get('/u/register')
def register_view(request):
    # context = {'register': 'Andrew', 'surname': 'Svetlov'}
    # response = aiohttp_jinja2.render_template('register.html',request,context)
    # response.headers['Content-Language'] = 'ru'
    # return response
    return {
        '__template__':'register.html',
        'register': 'Andrew',
        'surname': 'Svetlov'
    }

@post('/u/register')
async def registe(*,username,password,request,**kw):
    email = kw.get('email',None)
    if not username or not username.strip():
        raise APIValueError('username')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not password:
        raise APIValueError('password')
    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, password)
    user = User(id=uid, name=username.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    await user.save()
    user.passwd = '******'
    return user

@get('/u/login')
def login_view(request):
    return {
        '__template__':'login.html',
        'register': 'Andrew',
        'surname': 'Svetlov'
    }

@get('/u/logout')
async def login_out(request):
    session = await get_session(request)
    session['uid'] = None
    return {
        '__template__':'index.html',
        'not_login': True,
        'surname': 'Svetlov'
}

@post('/u/login')
async def login(*,username,password,request):
    if not username or not username.strip():
        raise APIValueError('username')
    if not password:
        raise APIValueError('password')
    
    users = await User.findAll('name=?', [username])
    if len(users) < 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    
    uid = users[0]["id"]
    sha1_passwd = '%s:%s' % (uid, password)
    passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest()

    if users[0]['passwd'] == passwd:
        session = await get_session(request)
        session['uid'] = uid
        return {
           'success':True
        }
    # make session cookie:
    result = {'success':False}
    return result