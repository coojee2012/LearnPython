
import aiohttp_jinja2
from aiohttp_session import get_session
from aiowebserver.utils import get,post


@get('/')
async def index(request):
    # context = {'register': 'Andrew', 'surname': 'Svetlov'}
    # response = aiohttp_jinja2.render_template('index.html',request,context)
    # response.headers['Content-Language'] = 'ru'
    # return response
    session = await get_session(request)
    uid = session.get("uid")
    return {
        '__template__':'index.html',
        'not_login': not uid,
        'surname': 'Svetlov'
    }

