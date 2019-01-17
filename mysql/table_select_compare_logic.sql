--数据库准备
  --创建数据库
  create database students charset=utf8;
  --使用数据库
  use students;
  --显示当前使用数据库
  select database();
  --创建一个表
  create table students(
    id tinyint unsigned  not null primary key auto_increment,
    name varchar(30),
    age int unsigned
    );
  --向表中插入数据(插入多个)
  insert into students values
  (0,"gust",18),
  (0,"kobe",30),
  (0,"lbj",28),
  (0,"heihei",10);
--查询
  --查询所有字段
  select * from students;
  --查询指定字段
  select id,name,age students;
  --别名
  select id as 编号,name 姓名,age 年龄 from students;
  mysql> select s.id,s.name,s.age from students as s;
+----+--------+------+
| id | name   | age  |
+----+--------+------+
|  2 | kobe   |   38 |
|  3 | lbj    |   32 |
|  4 | durant |   30 |
|  5 | cnn    |   18 |
|  6 | allen  |   40 |
+----+--------+------+
  --查询,去除重复数据
  select distinct gender from students;
--条件查询
  --比较运算符
  select * from students where age >18;
  select * from students where age<20;
  select * from students where age!=30;
  select * from students where age>=20;
  select * from students where age<=30;
  select * from students where age=32;

  --逻辑运算符
  --逻辑与
  --18到32岁之间
  select * from students where age>18 and age<=32;
  --18岁以上的女生
  select * from students where age>=18 and gender=2;
  --逻辑或
  --18岁以上的或者身高在188以上的
  select * from students where age>=18 or high>=188;
  --32岁以上的或者名字叫kobe的
  select * from students where age>32 or name="kobe";
  --逻辑非
  --不在18岁以上女性的范围内
  select * from students where not (gender=2 and age>18);
  --18岁以上的女性
  select * from students where gender=2 and age>18;
  --年龄不是<=18的 并且是女性...not 否定挨着的,可以加小括号提升优先级
  select * from students where not age<=18 and gender=2;
  select * from students where not (age<=18) and gender=2;

