# --*--coding:utf-8
# Author:cnn
from collections import Iterable


class Classmate(object):
    """迭代器类,迭代器一定是可迭代的(__iter__(self)),迭代器实现__iter__(self)和__next__(self)方法"""

    def __init__(self):
        self.names = list()
        self.count_num = 0

    def add(self, name):
        """添加姓名"""
        self.names.append(name)

    def __iter__(self):
        """
        迭代方法
        :return: #返回我自己,调用我自己的__next__()
        """
        return self

    def __next__(self):
        if self.count_num < len(self.names):
            ret = self.names[self.count_num]
            self.count_num += 1
            return ret
        else:
            raise StopIteration


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("kobe")
    classmate.add("乔丹")
    classmate.add("张三疯")
    for name in classmate:
        print(name)
