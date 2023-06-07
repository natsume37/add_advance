# coding : utf-8
# 夏目&青一
# @name:08-协程
# @time: 2023/5/24  18:06
import time


# def f1():
#     n = 0
#     for i in  range(100000000):
#         n +=1
#
# def f2():
#     n = 0
#     for i in  range(100000000):
#         n +=1
# start  = time.time()
# f1()
# f2()
# end = time.time()
# print(end - start)

# 7.474103927612305

# def f1():
#     n = 0
#     for i in  range(100000000):
#         n +=1
#         yield
#
# def f2():
#     g = f1()
#     n = 0
#     for i in  range(100000000):
#         n +=1
#         next(g)
# start  = time.time()
# f2()
# end = time.time()
# print(end - start)
#
# # 17.651402950286865