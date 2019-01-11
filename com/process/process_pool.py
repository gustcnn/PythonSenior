# --*--coding:utf-8
# Author:cnn

from multiprocessing import Pool
import os
from time import sleep
import time

def do_work(msg):
    start_time=time.time()
    print("您好,%d,进程id:%d" %(msg,os.getpid()))
    sum=0
    for i in range(0,msg):
        sum+=i
    for i in range(0,sum):
        sum+=i
    end=time.time()
    total_time=end-start_time
    print("花费%s秒"%total_time)
    sleep(1)

def main():
    #在进程池中最多创建3个进程
    po=Pool(3)
    for i in range(0,100):
        #向进程池提交目标请求
        po.apply_async(do_work,(i,))
    po.close()
    #等待进程池中的do_worker进程执行完毕
    po.join()

if __name__ == '__main__':
    main()