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
    #TODO
    def __iter__(self):
        """重写迭代方法,Classmate对象是可迭代的"""
        return ClassmateIterator(self)


class ClassmateIterator(object):
    def __init__(self,obj):
        self.obj=obj
        self.current_num=0
    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num<len(self.obj.names):
            ret=self.obj.names[self.current_num]
            self.current_num+=1
            return ret
        else:
            raise StopIteration


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("kobe")
    classmate.add("lbj")
    classmate.add("allen")
    print("验证classmate对象是否是可迭代的:", isinstance(classmate, Iterable))
    for name in classmate:
        print(name)