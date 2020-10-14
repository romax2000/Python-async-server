import random
import asyncio
from aiohttp import web


async def async_sum(request):
    a = request.match_info.get('a')
    b = request.match_info.get('b')
    result = int(a) + int(b)
    await server_sleep()
    return web.Response(text=str(result))


async def server_sleep():
    await asyncio.sleep(random.randint(0, 5))


app = web.Application()
app.add_routes([web.get('/sum/{a}/{b}', async_sum)])


if __name__ == '__main__':
    web.run_app(app)
