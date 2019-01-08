# --*--coding:utf-8
# Author:cnn
from threading import Thread
import threading
from time import sleep


class MyThread(Thread):
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

    def main(self):
        t1 = threading.Thread(target=self.sing)
        t1.setName("张三")
        t2 = threading.Thread(target=self.dance)
        t2.setName("李四")
        t1.start()
        t2.start()


if __name__ == "__main__":
    my_thread = MyThread()
    # # 创建线程
    # t1 = threading.Thread(target=my_thread.sing)
    # t1.setName("王凯")
    # t2 = threading.Thread(target=my_thread.dance)
    # t2.setName("陈伟霆")
    # # 开启线程
    # t1.start()
    # t2.start()
    my_thread.main()
    # 当前运行线程数
    thread_count = len(threading.enumerate())
    print("当前运行的线程数:%d" % thread_count)
