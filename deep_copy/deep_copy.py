#--*--coding:utf-8
#Author:cnn
import copy

a=[11,22,33,44]
b=a
#id(a)可以得到内存地址
print(id(a))
print(id(b))

c=copy.deepcopy(a)
print("deep",id(c))
print(id(a[0]))
print(id(c[0]))
a.append(55)
print(c)
print(a)

print(id(a[0]))
#浅拷贝拷完了之后,内容的内存地址不变
d=copy.copy(a)
print("浅拷贝",id(d))
print(id(d[0]))

aa=(11,22)
#因为元组是不可变类型
bb=copy.copy(aa)
print("aa",id(aa))
print("bb",id(bb))