#--*--coding:utf-8
#Author:cnn
--mysql数据库的操作
  --连接数据库
    mysql -uroot -p
  --退出
    quit or exit
  --查看所有数据库
    show databases;
  --显示当前数据库的时间
    select now();
  --查看数据库版本
    select version();
  --创建数据库
    create database python_mysql charset=utf8;
  --查看创建数据库的语句
    show create database python_mysql;
  --删除数据库
    drop database python_mysql;
  --如果数据库里面含有-,如python-08,删除时如下:``是tab键上头的,表示一个整体
    drop database `python-08`
  --查看当前使用的数据库
    select database();
  --使用某个数据库
    use python;--切换到python数据库

--数据表的操作
  --查看当前数据库有哪些表
  show tables;
  --创建一个表
  --枚举类型,给出那么多值,从里头选
  create table students(
      id int unsigned primary key not null auto_increment,
      name varchar(30),
      age tinyint unsigned default 0,
      high decimal(5,2),
      gender enum("男","女","中性","保密") default "保密",
      class_id int unsigned
  );
  --创建一个带约束的表
  create table student(id int primary key not null auto_increment,name varchar(30));
  create table course(
        id int primary key not null auto_increment,
        name varchar(20)
  );
  --查看表结构
  desc students;

  --向表中插入数据
  insert into students values(1,"gust",18,188.88,"女",0)
  --查询表中数据
  select * from students;
  --创建一个班级表
  create table classes(
      id int unsigned primary key not null auto_increment,
      name varchar(30) not null
  );
  --向表中插入数据
  insert into classes values(1,"计算机科学与技术");
  --查询表中数据
  select * from classes where id=1;
  --修改表结构
  --增加字段
  --alter table 表名 add 列名 字段类型
  alter table students add birthday datetime;
  --修改字段--不重命名(不修改字段名字,只修改类型)
  alter table students modify birthday date;
  --修改字段--重命名(修改字段名字)
  alter table students change birthday birth date default '2000-09-20';
  alter table students modify birth date default "2000-01-01";
  --删除字段,尽量别删
  alter table students drop high;

  --删除一张表
  drop  table students;
  --查看创建表的信息
  show create table students;

