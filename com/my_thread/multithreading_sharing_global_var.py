# --*--coding:utf-8
# Author:cnn
"""
多线程共享全局变量
"""
num = 100
from threading import Thread


class GlobalVariable(Thread):
    def update(self):
        # 声明num为全局变量的那个num
        global num
        num += 100

    def run(self):
        self.update()


if __name__ == '__main__':
    gv_01 = GlobalVariable()
    gv_02 = GlobalVariable()
    gv_01.start()  # 执行后num为200
    print(num)
    gv_02.start()
    print(num)  # 执行后num为300,多线程共享全局变量
