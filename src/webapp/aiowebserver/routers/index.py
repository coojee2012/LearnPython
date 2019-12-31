
import aiohttp_jinja2
from aiohttp_session import get_session
from aiowebserver.utils import get,post

from models.Blog import Blog

@get('/')
async def index(request):
    blogs = await Blog.findAll(limit=5)
    return {
        '__template__':'index.html',
        'blogs': blogs
    }

