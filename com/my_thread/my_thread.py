# --*--coding:utf-8
# Author:cnn
import threading
from time import sleep


class MyThread(threading.Thread):
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


if __name__ == "__main__":
    my_thread = MyThread()
    # 创建线程
    t1 = threading.Thread(target=my_thread.sing)
    t1.setName("王凯")
    t2 = threading.Thread(target=my_thread.dance)
    t2.setName("陈伟霆")
    # 开启线程
    t1.start()
    t2.start()
