from aiohttp import web
import json


async def handle():
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))
