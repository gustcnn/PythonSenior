# --*--coding:utf-8
# Author:cnn

import threading

# 全局变量是定义在外部的变量
g_num = 0
# 全局常量
G_NUM = 0


class MutilthreadingProblem(object):
    """
    多线程共享全局变量,存在资源竞争,导致值不准确
    """
    def update(self, num):
        global g_num
        for i in range(num):
            g_num += 1

    def main(self):
        # 创建线程对象,并传入参数
        t1 = threading.Thread(target=self.update, args=(100000,))
        t2 = threading.Thread(target=self.update, args=(100000,))
        t1.start()
        print(g_num)
        t2.start()
        print(g_num)


if __name__ == '__main__':
    mp = MutilthreadingProblem()
    mp.main()
