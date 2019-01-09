# --*--coding:utf-8
# Author:cnn
"""
多线程共享全局变量,带参数
"""
from threading import Thread

num = 100


class MutilGlobalArgs(Thread):
    def update(self, times):
        global num
        num += times

    def run(self):
        self.update(20)


if __name__ == '__main__':
    t1 = MutilGlobalArgs()
    t2 = MutilGlobalArgs()
    t1.start()
    print(num)
    t2.start()
    print(num)

