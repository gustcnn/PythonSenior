# --*--coding:utf-8
# Author:cnn
from time import sleep
import multiprocessing

g_num = 0
# 创建进程锁
mutex = multiprocessing.Lock()


# 多任务--进程
class MutiProcess(multiprocessing.Process):
    def print_name(self, num):
        global g_num
        for i in range(0, num + 1):
            # 上锁
            mutex.acquire()
            g_num += i
            mutex.release()
        print(g_num)
        sleep(1)

    def run(self):
        self.print_name(100)


if __name__ == '__main__':
    mu1 = MutiProcess()
    mu2 = MutiProcess()
    mu1.start()
    mu2.start()
# --*--coding:utf-8
