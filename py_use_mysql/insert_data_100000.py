#--*--coding:utf-8
#Author:cnn
import pymysql
class Data(object):
    def __init__(self):
        #创建连接
        self.conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="jing_dong",charset="utf8")
        #获得cursor对象
        self.cursor=self.conn.cursor()
    def main(self):
        #向test_index表插入10万条数据
        for i in range(100000):
            self.cursor.execute("insert into test_index values('ha-%d')"%i)
        #提交数据
        self.conn.commit()
if __name__ == '__main__':
    d=Data()
    d.main()