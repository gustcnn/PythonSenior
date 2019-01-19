--查询cate_name为超极本的所有信息
  select * from goods where cate_name="超极本";
  mysql> select * from goods where cate_name="超极本";
+----+-------------+-----------+------------+----------+---------+------------+
| id | name        | cate_name | brand_name | price    | is_show | is_saleoff |
+----+-------------+-----------+------------+----------+---------+------------+
|  5 | x240 超极本 | 超极本    | 联想       | 4880.000 |        |            |
| 10 | x260 超极本 | 超极本    | 联想       | 4880.000 |        |            |
+----+-------------+-----------+------------+----------+---------+------------+
--查询所有商品的种类
  select cate_name from goods group by cate_name;
  mysql> select cate_name from goods group by cate_name;
+-----------+
| cate_name |
+-----------+
| 游戏本    |
| 笔记本    |
| 超极本    |
+-----------+

--2查询所有商品的种类
  select distinct cate_name from goods;
  mysql> select distinct cate_name from goods;
+-----------+
| cate_name |
+-----------+
| 笔记本    |
| 游戏本    |
| 超极本    |
+-----------+
--查询每种商品的名称
select cate_name,group_concat(name) from goods group by cate_name;
mysql> select cate_name,group_concat(name) from goods group by cate_name;
+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
| cate_name | group_concat(name)                                                                                                                |
+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
| 游戏本    | g150th 15.6英寸游戏本,g160th 15.6英寸游戏本                                                                                       |
| 笔记本    | r510vc 15.6英寸笔记本,y400n 14.0英寸笔记本,x550cc 15.6英寸笔记本,r520vc 15.6英寸笔记本,y410n 14.0英寸笔记本,E550cc 15.6英寸笔记本 |
| 超极本    | x240 超极本,x260 超极本                                                                                                           |
+-----------+-----------------------------------------------------------------------------------------------------------------------------------+
--求所有电脑的平均价格,并保留2位小数
select round(avg(price),2) as 平均价格 from goods;
mysql> select round(avg(price),2) as 平均价格 from goods;
+----------+
| 平均价格 |
+----------+
|  4915.20 |
+----------+
--显示每种商品的平均价格
select cate_name as 商品,avg(price) as 平均价格 from goods group by cate_name;
mysql> select cate_name as 商品,avg(price) as 平均价格 from goods group by cate_name;
+--------+--------------+
| 商品   | 平均价格     |
+--------+--------------+
| 游戏本 | 8499.0000000 |
| 笔记本 | 3732.3333333 |
| 超极本 | 4880.0000000 |
+--------+--------------+
--2
select cate_name as 商品,round(avg(price),2) as 平均价格 from goods group by cate_name;
mysql> select cate_name as 商品,round(avg(price),2) as 平均价格 from goods group by cate_name;
+--------+----------+
| 商品   | 平均价格 |
+--------+----------+
| 游戏本 |  8499.00 |
| 笔记本 |  3732.33 |
| 超极本 |  4880.00 |
+--------+----------+
--查询每种类型的商品中最贵,最便宜,平均价,数量
select cate_name as 商品类型,max(price) as 最贵,min(price) as 最便宜,avg(price) as 平均价,count(*) as 数量 from goods group by cate_name;
mysql> select cate_name as 商品类型,max(price) as 最贵,min(price) as 最便宜,avg(price) as 平均价,count(*) as 数量 from goods group by cate_name;
+----------+----------+----------+--------------+------+
| 商品类型 | 最贵     | 最便宜   | 平均价       | 数量 |
+----------+----------+----------+--------------+------+
| 游戏本   | 8499.000 | 8499.000 | 8499.0000000 |    2 |
| 笔记本   | 4999.000 | 2799.000 | 3732.3333333 |    6 |
| 超极本   | 4880.000 | 4880.000 | 4880.0000000 |    2 |
+----------+----------+----------+--------------+------+
--查询所有价格大于平均价格的商品,并按价格降序排序
  select *from goods where price >(select avg(price) from goods) order by price desc;
mysql> select *from goods where price >(select avg(price) from goods) order by price desc;
+----+-----------------------+-----------+------------+----------+---------+------------+
| id | name                  | cate_name | brand_name | price    | is_show | is_saleoff |
+----+-----------------------+-----------+------------+----------+---------+------------+
|  3 | g150th 15.6英寸游戏本 | 游戏本    | 雷神       | 8499.000 |        |            |
|  8 | g160th 15.6英寸游戏本 | 游戏本    | 雷神       | 8499.000 |        |            |
|  2 | y400n 14.0英寸笔记本  | 笔记本    | 联想       | 4999.000 |        |            |
|  7 | y410n 14.0英寸笔记本  | 笔记本    | 联想       | 4999.000 |        |            |
+----+-----------------------+-----------+------------+----------+---------+------------+
--查询每种类型中最贵的电脑信息
select * from goods as g inner join (select cate_name,max(price) as max_price from goods group by cate_name) as g_new on g.cate_name=g_new.cate_name and g.price=g_new.max_price;
--格式化后
select * from goods as g
			inner join (select cate_name,max(price) as max_price from goods group by cate_name) as g_new
			on g.cate_name=g_new.cate_name and g.price=g_new.max_price;
mysql> select * from goods as g
    ->                  inner join (select cate_name,max(price) as max_price from goods group by cate_name) as g_new
    ->                  on g.cate_name=g_new.cate_name and g.price=g_new.max_price;
+----+-----------------------+-----------+------------+----------+---------+------------+-----------+-----------+
| id | name                  | cate_name | brand_name | price    | is_show | is_saleoff | cate_name | max_price |
+----+-----------------------+-----------+------------+----------+---------+------------+-----------+-----------+
|  2 | y400n 14.0英寸笔记本  | 笔记本    | 联想       | 5000.000 |        |            | 笔记本    |  5000.000 |
|  5 | x240 超极本           | 超极本    | 联想       | 6000.000 |        |            | 超极本    |  6000.000 |
|  8 | g160th 15.6英寸游戏本 | 游戏本    | 雷神       | 8500.000 |        |            | 游戏本    |  8500.000 |
+----+-----------------------+-----------+------------+----------+---------+------------+-----------+-----------+
