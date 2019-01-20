#--*--coding:utf-8
#Author:cnn
import pymysql

#创建connection对象
conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="jing_dong",charset="utf8")
#获得cursor对象
cs=conn.cursor()
#执行sql
count=cs.execute("select * from goods")
print("查询记录条数:%d"%count)
#获得全部查询结果
# select_result=cs.fetchall()
# print(select_result[0])
#获得一条
# result=cs.fetchone()
# print(result)
#参数写几,获得几条
many=cs.fetchmany(3)
print(many)
#关闭游标对象
cs.close()
#关闭connect
conn.close()

