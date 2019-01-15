#--*--coding:utf-8
#Author:cnn
import copy

a=[11,22]
b=[33,44]
c=[a,b]
c.append(55)
d=c[:]
#切片是浅拷贝
print(id(d),id(d[0]))
print(id(c),id(c[0]))
print(d)
print(c)