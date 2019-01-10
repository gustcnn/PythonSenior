# --*--coding:utf-8
# Author:cnn
import threading
from time import sleep

# 创建2个锁对象
mutex_a = threading.Lock()
mutex_b = threading.Lock()


class MyThread1(threading.Thread):
    def print_name(self):
        """
        a锁中包含b锁
        :return:
        """
        mutex_a.acquire()
        print("%s" % threading.current_thread().getName() + "do 1 up")
        sleep(1)
        mutex_b.acquire()
        print("%s" % threading.current_thread().getName() + "do 1 down")
        mutex_b.release()
        sleep(1)
        mutex_a.release()

    def run(self):
        self.print_name()



class MyThread2(threading.Thread):
    def print_name(self):
        """
        b锁中包含a锁
        :return:
        """
        mutex_b.acquire()
        print("%s" % threading.current_thread().getName() + "do 1 up")
        mutex_a.acquire()
        print("%s" % threading.current_thread().getName() + "do 1 down")
        mutex_a.release()
        sleep(1)
        mutex_b.release()

    def run(self):
        self.print_name()


if __name__ == '__main__':
    m1 = MyThread1()
    m3 = MyThread1()
    m2 = MyThread2()
    m4 = MyThread2()
    m1.start()
    sleep(1)
    m2.start()
    m3.start()
    m4.start()
