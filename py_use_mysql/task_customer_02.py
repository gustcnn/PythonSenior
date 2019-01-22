# --*--coding:utf-8
# Author:cnn
import pymysql
import sys
import re
from py_use_mysql.task_order import *

class Customer(object):
    """顾客类"""
    h = "localhost"
    p = 3306
    u = "root"
    pwd = "root"

    def __init__(self):
        self.conn = pymysql.connect(host=Customer.h, port=Customer.p, user=Customer.u,
                                    password=Customer.pwd, database="jing_dong", charset="utf8")
        self.cursor = self.conn.cursor()
        self.order=Order()

    def execute_sql(self, sql, param):
        """执行sql语句"""
        sql_re = r"^s.*"
        # 判断是否以s开头,如果不是,需要commit
        if re.match(sql_re, sql):
            num = self.cursor.execute(sql, param)
        else:
            num = self.cursor.execute(sql, param)
            self.conn.commit()
        return num

    def register(self):
        """用户注册"""
        # 存储注册信息
        param_list = list()
        while True:
            user_name = input("请输入用户名>>>:")
            select_sql = "select * from customers where name=%s"
            select_count = self.execute_sql(select_sql, [user_name])
            if select_count != 0:
                print("用户名已存在,请重新输入.")
            else:
                param_list.append(user_name)
                break
        user_address = input("请输入详细地址>>>:")
        param_list.append(user_address)
        user_tel = input("请输入电话号码>>>:")
        param_list.append(user_tel)
        # 密码以字母开头
        pwd_re = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        while True:
            user_pwd = input("请输入密码>>>:")
            if len(user_pwd) < 8:
                print("密码长度不够,请重新输入.")
            if len(user_pwd) >= 8:
                # 满足8位,判断是否包含字母数字下划线,包括以上则跳出循环
                if re.match(pwd_re, user_pwd):
                    param_list.append(user_pwd)
                    break
                else:
                    print("密码需为字母、数字、下划线组合,请重新输入密码.")
        # select_sql="select * from customers where name=%s"
        # select_count=self.execute_sql(select_sql,[user_name])
        sql = "insert into customers(name,address,tel,passwd) values(%s,%s,%s,%s)"
        # self.cursor.execute(sql, [user_name, user_address, user_tel, user_pwd])
        self.execute_sql(sql, param_list)
        print("用户%s注册成功." % user_name)

    def get_login_user_id(self, user_name):
        """
        获得登录用户id
        :param user_name: 登录用户名
        :return:
        """
        sql = "select id from customers where name=%s"
        login_user_list = list()
        login_user_id = None
        login_user_list.append(user_name)
        count = self.execute_sql(sql, login_user_list)
        print("login user 数量", count)
        # 获得登录用户的id
        for user_id in self.cursor.fetchone():
            login_user_id = user_id
        print(login_user_id)
        print(user_name)
        return login_user_id

    def show_all_goods(self):
        """显示所有商品"""
        print("商品列表:")
        sql = "select *from goods_update"
        self.execute_sql(sql,[])
        for good in self.cursor.fetchall():
            print(good)

    def login(self):
        """用户登录"""
        param_list = list()
        user_name = input("请输入用户名>>>:")
        user_passwd = input("请输入密码>>>:")
        sql = "select * from customers where name=%s and passwd=%s"
        param_list.append(user_name)
        param_list.append(user_passwd)
        count = self.execute_sql(sql, param_list)
        if count == 0:
            print("用户名不存在.")
            # self.register()
        else:
            print("欢迎登录京东商城.")
            id=self.get_login_user_id(user_name)
            self.show_all_goods()
            self.order.buy_goods(id)


    @staticmethod
    def print_menu():
        """打印菜单"""
        print("1.用户注册\r\n2.用户登录\r\n")

    def run(self):
        """选择菜单"""
        while True:
            input_result = input("请输入操作>>>:")
            if input_result == "1":
                self.register()
            elif input_result == "2":
                self.login()
            elif input_result == "q":
                sys.exit(0)
            else:
                print("操作错误,请重新输入.")

    def main(self):
        self.print_menu()
        self.run()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    customer = Customer()
    customer.main()
