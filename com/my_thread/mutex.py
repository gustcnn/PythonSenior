# --*--coding:utf-8
# Author:cnn
# 互斥锁
import threading
from time import sleep

# 定义全局变量
g_num = 0
# 创建一个锁对象
mutex = threading.Lock()


class Mutex(threading.Thread):
    def update(self, num):
        global g_num
        #上锁,如果没有上锁,则上锁,否则等待
        mutex.acquire()
        for i in range(0, num):
            g_num += 1
        #释放锁
        mutex.release()
        print(g_num)

    def run(self):
        self.update(2000000)
        # def main(self):
        #     t1=threading.Thread(target=self.update,args=(100000,))
        #     t2 = threading.Thread(target=self.update, args=(200000,))
        #     t1.start()
        #     sleep(1)
        #     t2.start()


if __name__ == '__main__':
    m1 = Mutex()
    m2 = Mutex()
    # m.main()
    m1.start()
    sleep(1)
    m2.start()
    sleep(5)
    #等几秒之后再打印,否则可能打印函数先执行了
    print(g_num)
