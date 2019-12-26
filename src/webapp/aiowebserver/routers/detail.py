from aiowebserver.utils import get,post


@get('/a/{id}')
def detail(id,request):
    # context = {'register': 'Andrew', 'surname': 'Svetlov'}
    # response = aiohttp_jinja2.render_template('detail.html',request,context)
    # response.headers['Content-Language'] = 'ru'
    # return response
    return {
        '__template__':'detail.html',
        'register': 'Andrew',
        'surname': 'Svetlov'
    }