# coding : utf-8
# 夏目&青一
# @name:03-生产者消费者模式
# @time: 2023/5/23  18:17

from multiprocessing import Queue, Process, JoinableQueue
import time
import random


def producer(name, food, q):
    for i in range(8):
        time.sleep(random.randint(2, 4))
        q.put(food)
        print(f"{name} 做了{food}{i}")


def consumer(name, q):
    while True:
        v = q.get()
        time.sleep(random.randint(1,3))
        print(f"{name} 吃了{v}")


        q.task_done()  # 告诉队列、我们已经拿走了一个数据、并且已经处理完了

'''
JoinableQueue
在Queue的基础上多了一个计数器机制，每put一个数据，计数器就加一
每调用一次task_done,计数器就减
当计数器为0的时候，就会走q.join后面的代码
'''

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=("小当家", "黄金炒饭", q))
    p2 = Process(target=producer, args=("神厨小福贵", "佛跳墙", q))
    c1 = Process(target=consumer, args=("八戒", q))

    c1.daemon = True # 设置守护进程、主进程死后、子进程也要死、而不是等待。

    p1.start()
    p2.start()
    c1.start()

    p1.join() # 必须加
    p2.join() # 必须加（保证每个数据全部处理完）

    q.join()

    # 主进程死了、子进程也要陪葬。（设置守护进程）