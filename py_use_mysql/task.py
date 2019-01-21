# --*--coding:utf-8
# Author:cnn
import pymysql
import sys
import re


class Customer(object):
    h = "localhost"
    p = 3306
    u = "root"
    pwd = "root"

    def __init__(self):
        self.conn = pymysql.connect(host=Customer.h, port=Customer.p, user=Customer.u,
                                    password=Customer.pwd, database="jing_dong", charset="utf8")
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql, param):
        sql_re = r"^s.*"
        if re.match(sql_re, sql):
            self.cursor.execute(sql, param)
            self.conn.commit()
        else:
            self.cursor.execute(sql, param)

    def register(self):
        user_name = input("请输入用户名>>>:")
        user_address = input("请输入详细地址>>>:")
        user_tel = input("请输入电话号码>>>:")
        user_pwd = input("请输入密码>>>:")
        if len(user_pwd) < 8:
            print("密码长度不够")
            user_pwd = input("请重新输入密码>>>:")
        sql = "insert into customers(name,address,tel,passwd) values(%s,%s,%s,%s)"
        param_list = list()
        param_list.append(user_name)
        param_list.append(user_address)
        param_list.append(user_tel)
        param_list.append(user_pwd)
        # self.cursor.execute(sql, [user_name, user_address, user_tel, user_pwd])
        self.cursor.execute(sql, param_list)
        self.conn.commit()
        print("用户%s注册成功." % user_name)

    def login(self):
        user_name = input("请输入用户名>>>:")
        user_passwd = input("请输入密码>>>:")
        sql = "select * from customers where name=%s and passwd=%s"
        param_list = list()
        param_list.append(user_name)
        param_list.append(user_passwd)
        count = self.cursor.execute(sql, param_list)
        if count == 0:
            print("用户名不存在,请注册")
            # self.register()
        else:
            print("欢迎登录京东商城.")

    @staticmethod
    def print_menu():
        print("1.用户注册\r\n2.用户登录")

    def run(self):
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
