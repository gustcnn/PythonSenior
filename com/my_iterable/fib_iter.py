# --*--coding:utf-8
# Author:cnn
from collections import Iterable


class Fibnacci(object):
    """使用迭代器实现斐波那契数列"""
    """0 1 1 2 3 5 8 13 21 34 55 89"""

    def __init__(self, num):
        self.num = num
        #控制fib的个数
        self.current_num = 0
        self.num_a = 0
        self.num_b = 1

    def __iter__(self):
        return self

    def __next__(self):
        """调用的时候生成值,节省内存空间"""
        if self.current_num < self.num:
            ret = self.num_a
            self.num_a, self.num_b = self.num_b, self.num_a + self.num_b
            self.current_num+=1
            return ret
        else:
            raise StopIteration


if __name__ == '__main__':
    fib = Fibnacci(10)
    print("判断对象是否是可迭代的", isinstance(fib, Iterable))
    for num in fib:
        print(num)
