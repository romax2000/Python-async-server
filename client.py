import time
import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


loop = asyncio.get_event_loop()
start_time = time.time()
coroutines = [get("http://0.0.0.0:8080/sum/8/2") for i in range(1000)]
results = loop.run_until_complete(asyncio.gather(*coroutines))
(print("--- %s seconds ---" % (time.time() - start_time)))

