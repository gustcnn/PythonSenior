#--*--coding:utf-8
#Author:cnn
import pymysql
import sys


class SqlInsert(object):
    """向数据库中插入数据"""

    def __init__(self, h, p, u, passwd):
        # 创建连接
        self.conn = pymysql.connect(host=h, port=p, user=u, password=passwd,database="jing_dong",charset="utf8")
        # 获得cursor
        self.cursor = self.conn.cursor()
    def show_goods_by_name(self):
        """根据名称查询商品"""
        item_name=input("请输入要查询的商品名称>>>:")
        if item_name=="q":
            sys.exit(0)
        #不安全方式
        sql="select * from goods_update where name='%s'"%item_name
        #%%得到%1
        #sql="select * from goods_update where name like '%%%s%%'"%item_name
        #为了能够清晰看到调试结果,不要只打印%s
        print("---------->%s<-----------"%sql)
        count=self.cursor.execute(sql)
        if count==0:
            print("对不起,您查找的商品不存在.")
        for item in self.cursor.fetchall():
            print(item)
    def __del__(self):
        """销毁对象的时候关闭游标和连接"""
        self.cursor.close()
        self.conn.close()

    def main(self):
        while True:
            self.show_goods_by_name()


if __name__ == '__main__':
    jd = SqlInsert("localhost", 3306, "root", "root")
    jd.main()
