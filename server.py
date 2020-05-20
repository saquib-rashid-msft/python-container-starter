from aiohttp import web
import os
from dotenv import load_dotenv
load_dotenv()

async def handle(request):      
    name = request.match_info.get('name', "World!")
    text = "Hello, " + name
    secret = os.getenv('SECRET_MESSAGE')
    fulltext = text + "\nSecret: " + secret + " (shhhhh)"
    print('received request, replying with "{}".'.format(text))
    return web.Response(text=fulltext)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, port=5858)