# --*--coding:utf-8
# Author:cnn
from time import sleep
import multiprocessing

g_num = 0
# 创建进程锁
mutex = multiprocessing.Lock()


# 多任务--进程,第二种实现方式
class MutiProcess(object):
    def update(self, num):
        global g_num
        for i in range(0, num + 1):
            # 上锁
            mutex.acquire()
            g_num += i
            mutex.release()
        print(g_num)
        sleep(1)

    def main(self):
        m1 = multiprocessing.Process(target=self.update, args=(100,))
        m2 = multiprocessing.Process(target=self.update, args=(200,))
        m1.start()
        m2.start()


if __name__ == '__main__':
    mu = MutiProcess()
    mu.main()
