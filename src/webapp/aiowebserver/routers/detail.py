from aiowebserver.utils import get,post

from models.Blog import Blog

@get('/a/{id}')
async def detail(id,request):
    blogs = await Blog.findAll('id=?', [id],limit=1)

    return {
        '__template__':'detail.html',
        'blog': blogs[0]
    }