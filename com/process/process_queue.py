# --*--coding:utf-8
# Author:cnn
import multiprocessing

# 创建进程队列对象
q = multiprocessing.Queue(3)
#判断是否为空
print(q.empty())
#向队列中装入数据
q.put(11)
q.put("111")
q.put([11, 22, 33])
#判断队列是否为满
print(q.full())

#从队列中取数据
print(q.get())
print(q.get())
print(q.get())
#当没有数据的时候,通过异常来通知
q.get_nowait()
