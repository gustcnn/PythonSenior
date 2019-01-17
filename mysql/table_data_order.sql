--排序
  --order by asc升序  从小到大
  select * from students order by id asc;
  --order by desc降序 从大到小
  select * from students order by id desc;
  --查询年龄在18~38之间的男性,并按照年龄从小到大排序
  select name,age,gender from students where (age between 18 and 38) and gender=1 order by age asc;
  select name,age,gender from students where age between 18 and 38 and gender=1 order by age asc;
  mysql> select name,age,gender from students where age between 18 and 38 and gender=1 order by age;
+--------+------+--------+
| name   | age  | gender |
+--------+------+--------+
| durant |   30 | 男     |
| lbj    |   32 | 男     |
| kobe   |   38 | 男     |
+--------+------+--------+
  --查询年龄不在18~38之间的男性,并按照年龄从大到小排序
  select name,age,gender from students where age not between 18 and 38 and gender=1 order by age desc;
  mysql>   select name,age,gender from students where age not between 18 and 38 and gender=1 order by age desc;
+--------+------+--------+
| name   | age  | gender |
+--------+------+--------+
| 崔天凯 |   70 | 男     |
+--------+------+--------+

  mysql> update students set age=18,high=160,gender=2 where name="崔楠楠";
  --查询年龄在18到38岁之间的女性,身高从高到矮排序
  select name,age,high from students where age between 18 and 38 and gender=2 order by high desc;
  mysql> select name,age,high from students where age between 18 and 40 and gender=2 order by high desc;
+--------+------+--------+
| name   | age  | high   |
+--------+------+--------+
| allen  |   40 | 196.00 |
| 崔楠楠 |   18 | 160.00 |
| 崔楠楠 |   18 | 160.00 |
+--------+------+--------+
  --order by 多个字段
  --查询年龄在18~40岁之间的女性,身高从高到矮排序,如果身高相同的情况下按照年龄从小到大排序
  select name,age,gender,high from students where age between 18 and 40 and gender=2 order by high desc,age asc;
  --查询年龄在18~40岁之间的女性,身高从高到矮排序,如果身高相同的情况下按照年龄从小到大排序,如果年龄也相同,按照id从大到小排序
  select name,age,gender,high from students where age between 18 and 40 and gender=2 order by high desc,age asc,id desc;
  mysql> select id,name,age,gender,high from students where age between 18 and 40 and gender=2 order by high desc,age asc,id desc;
+----+---------+------+--------+--------+
| id | name    | age  | gender | high   |
+----+---------+------+--------+--------+
|  6 | allen   |   40 | 女     | 196.00 |
| 21 | 张爱玲  |   28 | 女     | 165.00 |
|  9 | 崔楠楠  |   18 | 女     | 160.00 |
| 23 | gustcnn |   20 | 女     | 160.00 |
| 12 | 崔楠楠  |   20 | 女     | 160.00 |
+----+---------+------+--------+--------+

  --按照年龄从小到大,身高从高到矮
  select * from students order by age asc,high desc;
