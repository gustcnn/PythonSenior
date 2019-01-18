--聚合函数
  --查询女生有多少人
  select count(*) from students where gender=2;
  mysql> select * from students where gender=2;
+----+---------+------+--------+--------+----------+------------+-----------+
| id | name    | age  | high   | gender | class_id | birth      | is_delete |
+----+---------+------+--------+--------+----------+------------+-----------+
|  6 | allen   |   40 | 196.00 | 女     |        2 | 1999-10-10 |           |
|  9 | 崔楠楠  |   18 | 160.00 | 女     |     NULL | 2000-01-01 |           |
| 12 | 崔楠楠  |   20 | 160.00 | 女     |        1 | 2000-01-01 |           |
| 21 | 张爱玲  |   28 | 165.00 | 女     |     NULL | 2000-01-01 |           |
| 23 | gustcnn |   20 | 160.00 | 女     |     NULL | 2000-01-01 |           |
+----+---------+------+--------+--------+----------+------------+-----------+
mysql> select count(*) from students where gender=2;
+----------+
| count(*) |
+----------+
|        5 |

mysql> select count(*) as 女性人数 from students where gender=2;
+----------+
| 女性人数   |
+----------+
|        5 |
+----------+
--最大值
  select max(age) as 年龄最大值 from students;
  mysql> select max(age) as 年龄最大值 from students;
  +------------+
  | 年龄最大值 |
  +------------+
  |         70 |
  +------------+
--最小值
  select min(age) as 最小值 from students;
  mysql> select min(age) as 最小值 from students;
  +--------+
  | 最小值 |
  +--------+
  |      0 |
  +--------+
  --查询女性的最高身高
  select max(high) from students where gender=2;
  mysql> select max(high) from students where gender=2;
+-----------+
| max(high) |
+-----------+
|    196.00 |
+-----------+
1 row in set (0.02 sec)

mysql> select * from students where gender=2;
+----+---------+------+--------+--------+----------+------------+-----------+
| id | name    | age  | high   | gender | class_id | birth      | is_delete |
+----+---------+------+--------+--------+----------+------------+-----------+
|  6 | allen   |   40 | 196.00 | 女     |        2 | 1999-10-10 |           |
|  9 | 崔楠楠  |   18 | 160.00 | 女     |     NULL | 2000-01-01 |           |
| 12 | 崔楠楠  |   20 | 160.00 | 女     |        1 | 2000-01-01 |           |
| 21 | 张爱玲  |   28 | 165.00 | 女     |     NULL | 2000-01-01 |           |
| 23 | gustcnn |   20 | 160.00 | 女     |     NULL | 2000-01-01 |           |
+----+---------+------+--------+--------+----------+------------+-----------+
--计算所有人的年龄总和
select sum(age) from students;
--平均值
select avg(age) from students;
--2年龄平均值
select sum(age)/count(*) from students;
--四舍五入 round(123.23,1)保留1位小数
--计算所有人的平均年龄,保留2位小数
  select round(sum(age)/count(*),2) from students;
  select round(sum(age)/count(*),2) as 年龄平均值2位小数 from students;
  mysql> select round(sum(age)/count(*),2) as 年龄平均值2位小数 from students;
  +-------------------+
  | 年龄平均值2位小数    |
  +-------------------+
  |             14.95 |
  +-------------------+
--计算男性的平均年龄,保留2位小数
select round(avg(age),2) from students where gender=1;
mysql> select round(avg(age),2) from students where gender=1;
+-------------------+
| round(avg(age),2) |
+-------------------+
|             42.50 |
+-------------------+

--分组...分组和聚合函数一起用,否则一点意义都没有
--group by
--按照性别分组,显示所有性别
--select ... from students group by gender ...是能够唯一标识这个组的,count(*)是对分组的结果计算结果
select gender from students group by gender;

mysql> select gender,count(*) from students group by gender;
+--------+----------+
| gender | count(*) |
+--------+----------+
| 男     |        4 |
| 女     |        5 |
| 保密   |       12 |
+--------+----------+
--分组与聚合函数一起用才有意义,不然没什么卵用...
--按照性别分组,显示每个分组中的平均年龄
  select gender,avg(age) from students group by gender;
  mysql> select gender,avg(age) from students group by gender;
+--------+----------+
| gender | avg(age) |
+--------+----------+
| 男     |  42.5000 |
| 女     |  25.2000 |
| 保密   |   1.5000 |
+--------+----------+
--每个性别分组中的年龄综合
  select gender,sum(age) from students group by gender;
  mysql> select gender,sum(age) from students group by gender;
+--------+----------+
| gender | sum(age) |
+--------+----------+
| 男     |      170 |
| 女     |      126 |
| 保密   |       18 |
+--------+----------+
--查询同种性别中的姓名
  select gender,group_concat(name) from students group by gender;
  mysql> select gender,group_concat(name) from students group by gender;
+--------+--------------------------------------------------------------------+
| gender | group_concat(name)                                                 |
+--------+--------------------------------------------------------------------+
| 男     | kobe,lbj,durant,崔天凯                                             |
| 女     | 张爱玲,崔楠楠,崔楠楠,gustcnn,allen                                 |
| 保密   | cnn,周驰,周文王易经,周星,周,周星驰,cuinn,c,峰崔,崔永元,崔峰,崔永元 |
+--------+--------------------------------------------------------------------+
--计算男性的人数
select gender,count(*) from students where gender=1 group by gender;
--查询平均年龄大于30岁的分组,并显示人员姓名
select gender,avg(age),group_concat(name)from students group by gender having avg(age)>30;
mysql> select gender,avg(age),group_concat(name)from students group by gender having avg(age) >30;
+--------+----------+------------------------+
| gender | avg(age) | group_concat(name)     |
+--------+----------+------------------------+
| 男     |  42.5000 | kobe,lbj,durant,崔天凯 |
+--------+----------+------------------------+
--where 和having的区别:where是对原始表的判断,having是对结果进行判断

--查询每种性别中的人数多于2个的信息
select gender,count(*),group_concat(name) from students group by gender having count(*)>2;
mysql> select gender,count(*) from students group by gender having count(*)>2;
+--------+----------+
| gender | count(*) |
+--------+----------+
| 男     |        4 |
| 女     |        5 |
| 保密   |       12 |
+--------+----------+
3 rows in set (0.00 sec)

mysql> select gender,count(*),group_concat(name) from students group by gender having count(*)>2;
+--------+----------+--------------------------------------------------------------------+
| gender | count(*) | group_concat(name)                                                 |
+--------+----------+--------------------------------------------------------------------+
| 男     |        4 | kobe,lbj,durant,崔天凯                                               |
| 女     |        5 | 张爱玲,崔楠楠,崔楠楠,gustcnn,allen                                     |
| 保密   |       12 | cnn,周驰,周文王易经,周星,周,周星驰,cuinn,c,峰崔,崔永元,崔峰,崔永元          |
+--------+----------+--------------------------------------------------------------------+
