import re,hashlib,json,os
import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session

from aiowebserver.utils import get,post,short_uuid
from aiowebserver.api_errors import APIValueError,APIError
from config import config

from models.Blog import Blog

@get('/b/write')
def detail(request):
    return {
        '__template__':'content.html',
    }

@post('/b/{id}')
async def save_content(*,id,title,content,request):
    if not title or not title.strip():
        raise APIValueError('title')
    if not content or not content.strip():
        raise APIValueError('content')
    session = await get_session(request)
    uid = session.get('uid')
    if not uid:
        return {'success':False,'msg':'please login.'}
    if id == '0':
        blog = Blog(
            user_id = uid,
            user_name = '',
            user_image = '',
            name = title,
            summary = '',
            content = content
        )
        await blog.save()
        return {'success':True,'blog_id':blog.id}
    else:
        blogs = await Blog.findAll('id=?', [id])
        if len(blogs) != 1:
            raise APIError('update:failed', 'id', 'id is not find.')
        blog = blogs[0]
        blog.name = title
        blog.content = content
        await blog.update()
        return {'success':True,'blog_id':blog.id}

@post('/upload')
async def storefile(request):
    try:
        reader = await request.multipart()
        file = await reader.next()

        exts = ['.jpg','.jpeg','.png','.gif','.bpm']
        filename = file.filename if file.filename else 'undefined'
        suffix = os.path.splitext(filename)
        filename = '{}{}'.format(short_uuid(),suffix[1])
        filepath = '{}/{}'.format(config.app.uploaddir,filename)
        size = 0
        with open(filepath, 'wb') as f:
            while True:
                chunk = await file.read_chunk()  # 默认是8192个字节。
                if not chunk:
                    break
                size += len(chunk)
                f.write(chunk)
        text = {'res': '上传成功','filename':'{}{}'.format('/static/uploads/',filename)}
        result = text
        return result
    except Exception as e:
        print(e)
        result = {'success':False,'error': e}
        return result
