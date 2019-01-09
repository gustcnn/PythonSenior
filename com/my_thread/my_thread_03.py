# --*--coding:utf-8
# Author:cnn
from threading import Thread
import threading
from time import sleep


class MyThread(Thread):
    """
    比较复杂的,调用多个方法,就用继承,重写run()
    """
    def __init__(self):
        super().__init__()

    def sing(self):
        for i in range(1, 6):
            print(threading.current_thread().getName() + "...开始唱歌...")
            sleep(1)

    def dance(self):
        for i in range(1, 6):
            print(threading.current_thread().getName() + "...开始跳舞...")
            sleep(1)

    def run(self):
        self.sing()
        self.dance()

if __name__ == "__main__":
    #创建线程对象
    my_thread_01=MyThread()
    my_thread_02 = MyThread()
    my_thread_01.setName("王凯")
    my_thread_02.setName("陈伟霆")
    #创建线程,start调用run
    my_thread_01.start()
    # 创建线程
    my_thread_02.start()


