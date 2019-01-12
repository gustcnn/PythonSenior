# --*--coding:utf-8
# Author:cnn
from com.my_iterable.fib_iter import *

# 除了for循环能接受可迭代对象,list和tuple也可以
list_iter = list(Fibnacci(10))
print(list_iter)

tuple_iter = tuple(Fibnacci(15))
print(tuple_iter)
