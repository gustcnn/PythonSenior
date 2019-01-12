#--*--coding:utf-8
#Author:cnn
from greenlet import greenlet
from time import sleep
"""greenlet应用,greenlet封装了yield"""
def task_01():
    while True:
        print("1")
        sleep(0.1)
        greenlet_02.switch()
def task_02():
    while True:
        print("2")
        sleep(0.1)
        greenlet_01.switch()
#创建greenlet对象
greenlet_01=greenlet(task_01)
greenlet_02=greenlet(task_02)

#切换到greenlet_01中运行
greenlet_01.switch()