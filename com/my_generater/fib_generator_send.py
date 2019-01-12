# --*--coding:utf-8
# Author:cnn
def create_num(num):
    """send方式用的比较少,next()多一些"""
    current_num = 0
    a, b = 0, 1
    while current_num < num:
        res = yield a  # 当函数里面含有yield,就变成了生成器
        print(res)
        a, b = b, a + b
        current_num += 1


if __name__ == '__main__':
    obj = create_num(10)
    o1 = next(obj)
    print("o1", o1)

    o2 = obj.send("two")
    print("o2", o2)

    #o3 = next(obj)
    o3=obj.send("three")#将send的值three给 yield a左侧的res,o3接收的是yield 返回的值a得值
    #print("o3", o3)
