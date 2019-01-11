# --*--coding:utf-8
# Author:cnn
import multiprocessing


# 多进程通信--queue,因为进程之间是独立的,通信需要使用queue,完成进程间数据共享
def download_from_web(q):
    """模拟下载数据"""
    data = [11, 22, 33, 44]
    # 循环列表,将数据放入队列中
    for temp in data:
        q.put(temp)
    print("------数据下载完毕,放入队列中-------")


def analysis_data(q):
    """模拟处理数据"""
    # 存储数据列表
    analysis_data_list = list()
    # 循环从队列中获取数据,追加到队列中,当队列为空时,停止获取数据
    while True:
        data = q.get()
        analysis_data_list.append(data)
        if q.empty():
            break
    print(analysis_data_list)


def main():
    #创建队列对象
    q = multiprocessing.Queue()
    #创建进程对象,将队列对象做为实参传入
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    #创建并启动进程
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
# --*--coding:utf-8
