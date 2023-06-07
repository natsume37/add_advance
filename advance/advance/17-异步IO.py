# coding : utf-8
# 夏目&青一
# @name:异步IO
# @time: 2023/5/24  23:41

import asyncio
import time
from threading import current_thread


#
#
# def recv():
#     print("开始")
#     asyncio.sleep(2)
#     print("结束")
#
#
# async def f1():
#     print(f'任务：f1 开始 {current_thread().name}')
#     data = await recv()
#     print(data)
#     print(f'任务：f1 结束 {current_thread().name}')
#
#
# async def f2():
#     print(f'任务：f1 开始 {current_thread().name}')
#     await recv()
#     print(f'任务：f1 结束 {current_thread().name}')
#
#
# tasks = [f2(), f2()]
#
# asyncio.run(asyncio.wait(tasks))

async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main(name):
    # Create a "cancel_me" Task
    print(name, current_thread(),'任务：线程号')
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


asyncio.run(asyncio.wait(main("任务1"), main('任务2')))
