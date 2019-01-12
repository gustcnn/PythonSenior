# --*--coding:utf-8
# Author:cnn
def create_num(num):
    current_num = 0
    a, b = 0, 1
    while current_num < num:
        yield a  # 当函数里面含有yield,就变成了生成器
        a, b = b, a + b
        current_num += 1


for num in create_num(10):
    print(num)
