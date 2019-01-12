# --*--coding:utf-8
# Author:cnn
import gevent

"""网络应用的并发库,gevent封装了greenlet"""


def fib(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        # print(a)
        print(gevent.getcurrent(), a)
        a, b = b, a + b
        current_num += 1
        #gevent.sleep(0.1)


# 创建对象
g1 = gevent.spawn(fib, 10)
g2 = gevent.spawn(fib, 10)
g3 = gevent.spawn(fib, 10)
# 等待g1执行完毕
g1.join()
g2.join()
g3.join()
