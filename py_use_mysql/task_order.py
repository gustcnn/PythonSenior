# --*--coding:utf-8
# Author:cnn
import mysql
from py_use_mysql.task_customer import *


class Order(object):
    """订单类"""

    def __init__(self):
        customer=Customer()
        customer.cursor()

    def run(self):
        pass

    def main(self):
        pass


if __name__ == '__main__':
    order = Order()
    order.main()
