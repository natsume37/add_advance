# coding : utf-8
# 夏目&青一
# @name:Queue_add
# @time: 2023/5/24  11:31

import queue

# 先进先出queue
# q = queue.Queue()
# q.put()
# q.get()
# q.put_nowait()
# q.get_nowait()
# q.put(timeout=3)
# q.full()
# q.empty()

# 后进先出queue
# q = queue.LifoQueue()  # last in fist out
# q.put("a1")
# q.put("a2")
#
# print(q.get())
# print(q.get())

# a2
# a1


# 优先级queue
q = queue.PriorityQueue()

q.put((2, "2",))
q.put((0, "0",))
q.put((6, "6",))
q.put((23, "23",))
q.put((-3, "3",))

for i in range(5):
    print(q.get())

