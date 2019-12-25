
import aiohttp_jinja2
from aiowebserver.utils import get,post


@get('/')
def index(request):
    context = {'register': 'Andrew', 'surname': 'Svetlov'}
    response = aiohttp_jinja2.render_template('index.html',request,context)
    response.headers['Content-Language'] = 'ru'
    return response

