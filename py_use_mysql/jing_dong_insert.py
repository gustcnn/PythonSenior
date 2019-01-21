# --*--coding:utf-8
# Author:cnn
import pymysql
import sys


class JDInsert(object):
    """向数据库中插入数据"""

    def __init__(self, h, p, u, passwd):
        # 创建连接
        self.conn = pymysql.connect(host=h, port=p, user=u, password=passwd,database="jing_dong",charset="utf8")
        # 获得cursor
        self.cursor = self.conn.cursor()
    def add_cates(self):
        item_name=input("请输入要添加的商品分类>>>:")
        if item_name=="q":
            sys.exit(0)
        sql="insert into goods_cates(name) values('%s')"%item_name
        self.cursor.execute(sql)
        self.conn.commit()
        print("添加%s成功."%item_name)
    def run(self):
        self.add_cates()
    def run_01(self):
        """插入数据"""
        sql = "insert into goods_update values(0,'商务笔记本',6,3,210,default,default)"
        self.cursor.execute(sql)
        sql = "insert into goods_update values(0,'游戏笔记本',6,3,180,default,default)"
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()
        sql = "insert into goods_cates values(0,'硬盘')"
        self.cursor.execute(sql)
        #回滚
        self.conn.rollback()

    def __del__(self):
        """销毁对象的时候关闭游标和连接"""
        self.cursor.close()
        self.conn.close()

    def main(self):
        while True:
            self.run()


if __name__ == '__main__':
    jd = JDInsert("localhost", 3306, "root", "root")
    jd.main()
