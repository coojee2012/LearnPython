import re,hashlib,json,os
import aiohttp_jinja2
from aiohttp import web
from aiowebserver.utils import get,post,short_uuid
from aiowebserver.api_errors import APIValueError,APIError
from config import config

@get('/b/write')
def detail(request):
    return {
        '__template__':'content.html',
        'register': 'Andrew',
        'surname': 'Svetlov'
    }

@post('/b/{id}')
async def save_content(*,id,title,content,request):
    result = {'success':False}
    return result

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
