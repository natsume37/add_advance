# coding : utf-8
# 夏目&青一
# @name:09-gevent
# @time: 2023/5/24  18:23

from gevent import monkey  # 打补丁

monkey.patch_all()  # 检测所有的IO操作
from gevent import spawn
import time


def da():
    for i in range(3):
        print('da')
        time.sleep(2)


def ma():
    for i in range(3):
        print('damai')
        time.sleep(2)


def buyao():
    for i in range(3):
        print('不要')
        time.sleep(3)


s = time.time()
g1 = spawn(da)
g2 = spawn(ma)
g3 = spawn(buyao)

g1.join()  # 加时间等待
g2.join()  # 加等待
g3.join()

en = time.time()
print(en - s)
