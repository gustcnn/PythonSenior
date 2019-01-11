# --*--coding:utf-8
# Author:cnn
from collections import Iterable


class Classmate(object):
    def __init__(self):
        # 定义一个对象属性
        self.names = list()

    def add(self, name):
        """增加姓名"""
        self.names.append(name)

    def __iter__(self):
        """重写迭代方法,Classmate对象是可迭代的"""
        return self.names


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("kobe")
    classmate.add("lbj")
    classmate.add("allen")
    print("验证classmate对象是否是可迭代的:", isinstance(classmate, Iterable))
    for name in classmate.names:
        print(name)
