# --*--coding:utf-8
# Author:cnn
from time import sleep

"""使用协程完成多任务"""
g_num = 0


def task_01(num):
    global g_num
    for i in range(num):
        g_num += 1
        #print("task_01", g_num)
        yield g_num
    sleep(0.1)
    #yield


def task_02(num):
    global g_num
    for i in range(num):
        g_num += 1
        #print("task_02", g_num)
        yield g_num
    sleep(0.1)


def main():
    #创建生成器对象
    t1=task_01(100)
    t2=task_02(10)
    while True:
        try:
            #调用next(),获得yield g_num的返回值 g_num
            d1=next(t1)
            print("d1",d1)
        except StopIteration as si:
            break

        try:
            #调用next(),获得yield g_num的返回值 g_num
            d2=next(t2)
            print("d2",d2)
        except StopIteration as si:
            break


if __name__ == '__main__':
    main()
