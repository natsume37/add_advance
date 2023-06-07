# coding : utf-8
# 夏目&青一
# @name:异步迭代器
# @time: 2023/5/31  14:32

# 普通的
class MyRange(object):
    def __init__(self, start, end=None):
        if end:
            self.count = start - 1
            self.end = end
        else:
            self.count = -1
            self.end = start

    def add_count(self):
        self.count += 1
        if self.count == self.end:
            return None
        return self.count

    def __iter__(self):
        return self

    def __next__(self):
        value = self.add_count()
        if value is None:
            raise StopIteration
        return value


# 测试迭代器
for i in MyRange(10):
    print(i)
