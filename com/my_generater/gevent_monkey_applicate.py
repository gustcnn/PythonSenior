# --*--coding:utf-8
# Author:cnn
from gevent import monkey
import gevent
from time import sleep
# 打补丁,开始后,会自动检查是否有延时,有延时自动换成gevent的延时
monkey.patch_all()


def f1(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        sleep(0.01)

if __name__ == '__main__':
    # g1 = gevent.spawn(f1, 100)
    # g2 = gevent.spawn(f1, 100)
    # g3 = gevent.spawn(f1, 100)
    #
    # g1.join()
    # g2.join()
    # g3.join()
    gevent.joinall(
        [gevent.spawn(f1,100),
        gevent.spawn(f1,100),
        gevent.spawn(f1,100)]
    )
