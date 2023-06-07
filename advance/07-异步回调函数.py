from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

pool = ProcessPoolExecutor()  # 默认有值


def task(name):
    print(name)
    time.sleep(3)
    return name + 10


def call_back(res):
    print("call_back", res.result())



if __name__ == '__main__':
    f_list = []
    for i in range(50):
        pool.submit(task, i).add_done_callback(call_back)
