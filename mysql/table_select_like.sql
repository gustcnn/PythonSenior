--模糊查询..通配符
  --like
  --查询出所有以崔开头的名字
  select * from students where name like "崔%";
  --查询出所有名字是崔*的人
  select * from students where name like "崔_";
  --查询出所有名字中带崔的人
  select * from students where name like "%崔%";
  --查询有2个字的名字
  select * from students where name like "__";
  --查询有3个字的名字
  select * from students where name like "___";
  --查询名字至少有2个字的
  select * from students where name like "__%";
  --rlike 正则
  --查询以周开头的姓名
  select * from students where name rlike "^周.*";
  mysql> select * from students where name rlike "^周.*";
+----+------------+------+------+--------+----------+------------+-----------+
| id | name       | age  | high | gender | class_id | birth      | is_delete |
+----+------------+------+------+--------+----------+------------+-----------+
| 16 | 周星驰     |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
| 17 | 周         |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
| 18 | 周星       |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
| 19 | 周文王易经 |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
| 20 | 周驰       |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
+----+------------+------+------+--------+----------+------------+-----------+
  --查询以周开头,以驰结尾的姓名
  select * from students where name rlike "^周.*驰$";
  mysql> select * from students where name rlike "^周.*驰$";
+----+--------+------+------+--------+----------+------------+-----------+
| id | name   | age  | high | gender | class_id | birth      | is_delete |
+----+--------+------+------+--------+----------+------------+-----------+
| 16 | 周星驰 |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
| 20 | 周驰   |    0 | NULL | 保密   |     NULL | 2000-01-01 |           |
+----+--------+------+------+--------+----------+------------+-----------+
