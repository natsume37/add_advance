from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

pool = ThreadPoolExecutor()  # 默认有值


def task(name):
    print(name)
    time.sleep(3)
    return name +10
f_list = []
for i in range(50):
    p = pool.submit(task, i)
    f_list.append(p)


pool.shutdown()  # 关闭线程池、等待线程池中所有的任务全都运行完毕 （类似于线程的join()方法）


for i in f_list:
    print(i.result())
