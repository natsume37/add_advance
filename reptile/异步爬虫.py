# coding : utf-8
# 夏目&青一
# @name:异步爬虫
# @time: 2023/6/2  23:14

import asyncio
import requests
import time
import aiohttp

# stat = time.time()
#
#
# async def get(url):
#     return requests.get(url)
#
# async def request():
#     url = "https://www.httpbin.org/delay/5"
#     print('waiting',url)
#     response = await get(url)
#     print("获取结果", url,"response",response)
#
# tasks = [
#     asyncio.ensure_future(request()) for _ in range(10)
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# end = time.time()
# print(end - stat)


stat = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = "https://www.httpbin.org/delay/5"
    print('waiting', url)
    response = await get(url)
    print("获取结果", url, "response", response)


tasks = [
    asyncio.ensure_future(request()) for _ in range(10)
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end - stat)
