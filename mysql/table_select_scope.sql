--范围查询
  --查询年龄为18或者32的姓名
  --in 表示非连续的范围内
  select name,age from students where age=18 or age=32;
  --2
  select name,age from students where age in (18,32);
  --查询年龄不在18和32的姓名
  --not in 不非连续的范围内
  select name,age from students where age not in (18,32);
  --between..and 连续的范围内
  --查询年龄在18~38之间的信息
  select name,age from students where age between 18 and 38;
  --2
  select name,age from students where age >=18 and age<=38;
  --not between and 不在连续的范围内
  --查询年龄不在18~38之内的人的姓名
  select name,age from students where age not between 18 and 38;