#--*--coding:utf-8
#Author:cnn
--表中数据的增删改查
--students 的表结构  desc students
+----------+-------------------------------+------+-----+------------+----------------+
| Field    | Type                          | Null | Key | Default    | Extra          |
+----------+-------------------------------+------+-----+------------+----------------+
| id       | int(10) unsigned              | NO   | PRI | NULL       | auto_increment |
| name     | varchar(30)                   | YES  |     | NULL       |                |
| age      | tinyint(3) unsigned           | YES  |     | 0          |                |
| high     | decimal(5,2)                  | YES  |     | NULL       |                |
| gender   | enum('男','女','中性','保密') | YES  |     | 保密       |                |
| class_id | int(10) unsigned              | YES  |     | NULL       |                |
| birth    | date                          | YES  |     | 2000-01-01 |                |
+----------+-------------------------------+------+-----+------------+----------------+

--向表中插入数据,id为0表示自增长
  insert into students values(0,"kobe",38,196,"男",1,"1979-09-01");
  insert into students values(null,"lbj",32,190,"男",2,"1988-08-08");
  insert into students values(default,"durant",30,198,"男",3,"1988-11-11");
  insert into students(name,age,high,gender,class_id,birth) values("cnn",18,190,default,1,"1998-01-01");
  --枚举中的下标从1开始 1-->男,2-->女...
  insert into students(name,age,high,gender,class_id,birth) values("allen",40,196,1,2,"179-10-10");
  --修改表中数据
  update students set gender=1 where id=1;
  --查询数据
  select * from students where name="gust";
  select * from students where id>5;
  select * from students where id >5 or name="gust";
  select * from students where id=1 and name="gust";
  select name as 姓名 from students;
  select name as 姓名,gender as 性别 from students;
  --查询表中记录数
  select count(*) as 数量 from students;
  --删除表中数据,物理删除如下:
  delete from students where name="gust";
  --删除表中数据,逻辑删除如下:
  --增加删除标记,默认值是0
  alter table students add is_delete bit default 0;
+-----------+-------------------------------+------+-----+------------+----------------+
| Field     | Type                          | Null | Key | Default    | Extra          |
+-----------+-------------------------------+------+-----+------------+----------------+
| id        | int(10) unsigned              | NO   | PRI | NULL       | auto_increment |
| name      | varchar(30)                   | YES  |     | NULL       |                |
| age       | tinyint(3) unsigned           | YES  |     | 0          |                |
| high      | decimal(5,2)                  | YES  |     | NULL       |                |
| gender    | enum('男','女','中性','保密') | YES  |     | 保密       |                |
| class_id  | int(10) unsigned              | YES  |     | NULL       |                |
| birth     | date                          | YES  |     | 2000-01-01 |                |
| is_delete | bit(1)                        | YES  |     | b'0'       |                |
+-----------+-------------------------------+------+-----+------------+----------------+

mysql> select * from students where is_delete=0;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  2 | kobe   |   38 | 196.00 | 男     |        1 | 1979-09-01 |           |
|  3 | lbj    |   32 | 190.00 | 男     |        2 | 1988-08-08 |           |
|  4 | durant |   30 | 198.00 | 男     |        3 | 1988-11-11 |           |
|  5 | cnn    |   18 | 190.00 | 保密   |        1 | 1998-01-01 |           |
|  6 | allen  |   40 | 196.00 | 男     |        2 | 0179-10-10 |           |
+----+--------+------+--------+--------+----------+------------+-----------+

--修改kobe为删除状态
update students set is_delete=1 where name="kobe";
mysql> select * from students;
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  2 | kobe   |   38 | 196.00 | 男     |        1 | 1979-09-01 | 1         |
|  3 | lbj    |   32 | 190.00 | 男     |        2 | 1988-08-08 |           |
|  4 | durant |   30 | 198.00 | 男     |        3 | 1988-11-11 |           |
|  5 | cnn    |   18 | 190.00 | 保密   |        1 | 1998-01-01 |           |
|  6 | allen  |   40 | 196.00 | 男     |        2 | 0179-10-10 |           |
+----+--------+------+--------+--------+----------+------------+-----------+
