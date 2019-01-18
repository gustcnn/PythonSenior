--分页
  --limit start,count  limit 2,5 2为起始下标,5为数据个数
  --限制查询出来的数据个数
  select *from students where gender=1 limit 2;
  --查询前5个数据
  select *from students limit 5;
  mysql>  select *from students limit 5;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  2 | kobe   |   38 | 196.00 | 男     |        1 | 1979-09-01 |          |
|  3 | lbj    |   32 | 190.00 | 男     |        2 | 1988-08-08 |           |
|  4 | durant |   30 | 198.00 | 男     |        3 | 1988-11-11 |           |
|  5 | cnn    |   18 | 190.00 | 保密   |        1 | 1998-01-01 |           |
|  6 | allen  |   40 | 196.00 | 女     |        2 | 1999-10-10 |           |
+----+--------+------+--------+--------+----------+------------+-----------+
  --查询id6-10,包含10的书序
  select * from students group by id limit 5,5;
  mysql> select * from students;
+----+------------+------+--------+--------+----------+------------+----------
| id | name       | age  | high   | gender | class_id | birth      | is_delete
+----+------------+------+--------+--------+----------+------------+----------
|  2 | kobe       |   38 | 196.00 | 男     |        1 | 1979-09-01 | 
|  3 | lbj        |   32 | 190.00 | 男     |        2 | 1988-08-08 |
|  4 | durant     |   30 | 198.00 | 男     |        3 | 1988-11-11 |
|  5 | cnn        |   18 | 190.00 | 保密   |        1 | 1998-01-01 |
|  6 | allen      |   40 | 196.00 | 女     |        2 | 1999-10-10 |
|  7 | 崔天凯     |   70 | 179.00 | 男     |        1 | 1950-01-10 |
|  8 | 崔永元     |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
|  9 | 崔楠楠     |   18 | 160.00 | 女     |     NULL | 2000-01-01 |
| 10 | 崔峰       |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 11 | 崔永元     |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 12 | 崔楠楠     |   20 | 160.00 | 女     |        1 | 2000-01-01 |
| 13 | 峰崔       |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 14 | c          |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 15 | cuinn      |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 16 | 周星驰     |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 17 | 周         |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 18 | 周星       |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 19 | 周文王易经 |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 20 | 周驰       |    0 |   NULL | 保密   |     NULL | 2000-01-01 |
| 21 | 张爱玲     |   28 | 165.00 | 女     |     NULL | 2000-01-01 |
| 23 | gustcnn    |   20 | 160.00 | 女     |     NULL | 2000-01-01 |
| 24 | 金星       |    0 |   NULL | 中性   |     NULL | 2000-01-01 |
+----+------------+------+--------+--------+----------+------------+----------
22 rows in set (0.00 sec)

mysql> select * from students limit 0,5;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  2 | kobe   |   38 | 196.00 | 男     |        1 | 1979-09-01 |          |
|  3 | lbj    |   32 | 190.00 | 男     |        2 | 1988-08-08 |           |
|  4 | durant |   30 | 198.00 | 男     |        3 | 1988-11-11 |           |
|  5 | cnn    |   18 | 190.00 | 保密   |        1 | 1998-01-01 |           |
|  6 | allen  |   40 | 196.00 | 女     |        2 | 1999-10-10 |           |
+----+--------+------+--------+--------+----------+------------+-----------+
5 rows in set (0.00 sec)

mysql> select * from students limit 5,5;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  7 | 崔天凯 |   70 | 179.00 | 男     |        1 | 1950-01-10 |           |
|  8 | 崔永元 |    0 |   NULL | 保密   |     NULL | 2000-01-01 |           |
|  9 | 崔楠楠 |   18 | 160.00 | 女     |     NULL | 2000-01-01 |           |
| 10 | 崔峰   |    0 |   NULL | 保密   |     NULL | 2000-01-01 |           |
| 11 | 崔永元 |    0 |   NULL | 保密   |     NULL | 2000-01-01 |           |
+----+--------+------+--------+--------+----------+------------+-----------+

--每页显示2个,第1个页面
select * from students limit 0,2;
--每页显示2个,第2个页面;
select * from students limit 2,2;
--每页显示2个,第3个页面
select *from students limit 4,2;
--每页显示2个,第4个页面
select *from students limit 6,2;--->limit [第n页-1]*每页个数,每页个数;
mysql> select * from students limit 0,2;
+----+------+------+--------+--------+----------+------------+-----------+
| id | name | age  | high   | gender | class_id | birth      | is_delete |
+----+------+------+--------+--------+----------+------------+-----------+
|  2 | kobe |   38 | 196.00 | 男     |        1 | 1979-09-01 |          |
|  3 | lbj  |   32 | 190.00 | 男     |        2 | 1988-08-08 |           |
+----+------+------+--------+--------+----------+------------+-----------+
2 rows in set (0.00 sec)

mysql> select * from students limit 2,2;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  4 | durant |   30 | 198.00 | 男     |        3 | 1988-11-11 |           |
|  5 | cnn    |   18 | 190.00 | 保密   |        1 | 1998-01-01 |           |
+----+--------+------+--------+--------+----------+------------+-----------+
2 rows in set (0.00 sec)

mysql> select *from students limit 4,2;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  6 | allen  |   40 | 196.00 | 女     |        2 | 1999-10-10 |           |
|  7 | 崔天凯 |   70 | 179.00 | 男     |        1 | 1950-01-10 |           |
+----+--------+------+--------+--------+----------+------------+-----------+
2 rows in set (0.00 sec)

mysql> select *from students limit 6,2;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  8 | 崔永元 |    0 |   NULL | 保密   |     NULL | 2000-01-01 |           |
|  9 | 崔楠楠 |   18 | 160.00 | 女     |     NULL | 2000-01-01 |           |
+----+--------+------+--------+--------+----------+------------+-----------+

--每页显示2个,显示第6页的信息,按照年龄从小到大排序 2*(6-1)...limit 放在最后
select * from students order by age asc limit 10,2;