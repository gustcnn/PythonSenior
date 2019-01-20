#--*--coding:utf-8
#Author:cnn
import pymysql

print("1.所有的商品\r\n2.对应的商品的分类\r\n3.对应的商品品牌分类\r\n")
input_result=input("请输入要查询的内容>>>:")
sql_str=""
if input_result=="1":
    sql_str="select *from goods_update"
elif input_result=="2":
    sql_str="select g.id,c.name from goods_update as g " \
            "inner join goods_cates as c" \
            " on c.id=g.cate_id group by c.name order by id;"
elif input_result=="3":
    sql_str="select g.id,b.name from goods_update as g " \
            "inner join goods_brands as b " \
            "on g.brand_id=b.id group by b.name order by g.id;"
#创建连接
conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="jing_dong",charset="utf8")
#获得游标
cursor=conn.cursor()
#执行sql
count=cursor.execute(sql_str)
for i in range(count):
    # id,name=cursor.fetchone()
    # print(name)
    print(cursor.fetchone())

#关闭游标
cursor.close()
#关闭连接
conn.close()