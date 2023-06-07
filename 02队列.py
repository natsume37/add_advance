# coding : utf-8
# 夏目&青一
# @name:队列
# @time: 2023/5/23  17:47

from multiprocessing import Queue

q = Queue(6)
q.put("a")
q.put(3)

v1 = q.get()
v2 = q.get()
print(v1, v2)