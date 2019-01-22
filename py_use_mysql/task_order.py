# --*--coding:utf-8
# Author:cnn
from py_use_mysql.task_customer import *
import datetime

class Order(object):
    """订单类"""
    h = "localhost"
    p = 3306
    u = "root"
    pwd = "root"

    def __init__(self):
        self.conn = pymysql.connect(host=Customer.h, port=Customer.p, user=Customer.u,
                                    password=Customer.pwd, database="jing_dong", charset="utf8")
        self.cursor = self.conn.cursor()
        #购买商品列表
        self.buy_list = list()

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

    def buy_goods(self, user_id):
        """
        购买商品
        :param user_id: 哪个用户购买商品
        :return:
        """
        while True:
            user_order_list = list()
            # 输入商品列表
            input_list = list()
            buy_good = input("请输入购买的商品id>>>:")
            if buy_good=="q":
                print("您购买的商品列表为:%s,欢迎下次光临." % self.buy_list)
                break
            sql = "select * from goods_update where id=%s"
            input_list.append(buy_good)
            count = self.execute_sql(sql, input_list)
            #如果count>0，说明数据库中有次条记录
            if count > 0:
                self.buy_list.append(buy_good)
                buy_sql = "insert into orders(order_date_time,customer_id) values(%s,%s)"
                dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # 将购买日期和用户id插入列表中
                user_order_list.append(dt)
                user_order_list.append(user_id)
                self.execute_sql(buy_sql, user_order_list)
                print("商品%s成功加入购物车." % buy_good)
            else:
                print("对不起,您想要购买的商品不存在,请重新选择.")

    def main(self):
        self.buy_goods(9)


if __name__ == '__main__':
    order = Order()
    order.main()
