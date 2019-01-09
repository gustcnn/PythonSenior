# --*--coding:utf-8
# Author:cnn
"""
多线程共享全局变量,带参数
"""
import threading

num = 20


class MutilGlobalArgs(object):
    def update(self, times):
        global num
        num += times

    def main(self):
        #创建线程对象,并传入参数
        t1=threading.Thread(target=self.update,args=(num,))
        t2 = threading.Thread(target=self.update, args=(num,))
        #创建线程并启动
        t1.start()
        print(num)
        t2.start()
        print(num)

if __name__ == '__main__':
    t= MutilGlobalArgs()
    t.main()
    #print(num)

