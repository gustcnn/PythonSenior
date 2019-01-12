# --*--coding:utf-8
# Author:cnn
"""递归实现斐波那契数列"""


# F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

if __name__ == '__main__':
    print(fib(10))