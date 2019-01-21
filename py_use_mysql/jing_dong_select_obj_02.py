# --*--coding:utf-8
# Author:cnn
import pymysql
import sys


# 用面向对象的思想来做查询

class JD(object):
    def __init__(self, h, p, u, passwd):
        # 创建连接
        self.conn = pymysql.connect(host=h, port=p, user=u, password=passwd, database="jing_dong", charset="utf8")
        # 获得游标
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for result in self.cursor.fetchall():
            print(result)

    def show_all_items(self):
        """显示所有数据"""
        sql_str = "select * from goods_update"
        self.execute_sql(sql_str)

    def show_goods_cates(self):
        """显示商品对应的分类"""
        sql_str = "select g.id,c.name from goods_update as g " \
                  "inner join goods_cates as c" \
                  " on c.id=g.cate_id group by c.name order by id;"
        self.execute_sql(sql_str)

    def show_goods_brands(self):
        """显示商品对应的品牌"""
        sql_str = "select g.id,b.name from goods_update as g " \
                  "inner join goods_brands as b " \
                  "on g.brand_id=b.id group by b.name order by g.id;"
        self.execute_sql(sql_str)

    # def print_menu(self):
    #     print("1.所有的商品\r\n2.对应的商品的分类\r\n3.对应的商品品牌分类\r\n")
    #     input_result = input("请输入要查询的内容>>>:")
    #     return input_result
    @staticmethod
    def print_menu():
        """静态方法,打印菜单"""
        print("1.所有的商品\r\n2.对应的商品的分类\r\n3.对应的商品品牌分类\r\n")
        input_result = input("请输入要查询的内容>>>:")
        return input_result

    def run(self):
        """"""
        while True:
            input_result = self.print_menu()
            sql_str = ""
            if input_result == "1":
                self.show_all_items()
            elif input_result == "2":
                self.show_goods_cates()
            elif input_result == "3":
                self.show_goods_brands()
            elif input_result == "q":
                print("退出系统")
                sys.exit(0)
            else:
                print("输入错误,请重新输入.")

    def __del__(self):
        """销毁对象的时候会关闭游标,关闭连接"""
        self.cursor.close()
        self.conn.close()

    def main(self):
        """做为接口"""
        self.run()


if __name__ == '__main__':
    jd = JD("localhost", 3306, "root", "root")
    jd.main()
