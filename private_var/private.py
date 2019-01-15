# --*--coding:utf-8
# Author:cnn
# 一个下划线的变量名,import的时候禁止导入
_age = 18


class Person(object):
    def __init__(self, name,age,no):
        self.__name = name
        self.no=no
        self._age=age
