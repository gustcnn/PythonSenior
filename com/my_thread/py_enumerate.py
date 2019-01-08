# --*--coding:utf-8
# Author:cnn
names = ["kobe", "allen", "lbj"]
for i, name in enumerate(names):  # i,name将元组拆包
    print(i, name)

# enumerate(),将列表生成元组
for name in enumerate(names):
    print(name)
