import random
import time
from threading import Thread, Lock, current_thread
from multiprocessing import Process

#
# import time
#
#
# def task():
#     res = 0
#     for i in range(100000000):
#         res += 1
#
#
# if __name__ == '__main__':
#     l = []
#     ps = time.time()
#     for i in range(8):
#         # p = Process(target=task) # 16.27019715309143
#         p = Thread(target=task) # 31.66116213798523
#         p.start()
#         l.append(p)
#     for p in l:
#         p.join()
#     pe = time.time()
#     print(pe - ps)

# import time
# from threading import Thread, Lock, current_thread, RLock
# from multiprocessing import Process
#
# mutex1 = Lock()
# mutex2 = Lock()
#
#
# def test():
#     mutex1.acquire()
#     print(f"{current_thread().name} 抢到了锁1")
#     mutex2.acquire()
#     print(f"{current_thread().name} 抢到了锁2")
#     mutex2.release()
#     mutex1.release()
#
#     mutex2.acquire()
#     print(f"{current_thread().name} 抢到了锁1")
#     time.sleep(1) # 为了更直接展示
#     mutex1.acquire()
#     print(f"{current_thread().name} 抢到了锁2")
#     mutex1.release()
#     mutex2.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=test)
#         t.start()

# from threading import Thread, Semaphore
# import time
# import random
#
# sp = Semaphore(5)
#
# def task(name):
#     sp.acquire()
#     print(name, "抢到了锁")
#     time.sleep(random.randint(3,5))
#     sp.release()
#
# if __name__ == '__main__':
#     for i in range(25):
#         t = Thread(target=task, args=(f"bike{i+1}号",))
#         t.start()

from threading import Thread, Event
import time

even = Event()


def bus():
    print("公交车即将到站")
    time.sleep(3)
    print("公交车到站了")
    even.set()  # 发射了一个信号、车来了赶快上车
    print()


def passenger(name):
    print(name, "正在等车")
    even.wait()  # 等待公交车来
    print(name, "上车了")


if __name__ == '__main__':
    t = Thread(target=bus())
    t.start()
    for i in range(10):
        pa = Thread(target=passenger, args=(f"person{i + 1}",))
        pa.start()
