--判断空
  --判断class_id不为空的姓名
  select name,class_id from students where class_id is not null;
+--------+----------+
| name   | class_id |
+--------+----------+
| kobe   |        1 |
| lbj    |        2 |
| durant |        3 |
| cnn    |        1 |
| allen  |        2 |
| 崔天凯 |        1 |
+--------+----------+
--判断class_id为空的姓名
  select name,class_id from students where class_id is null;
mysql> select name,class_id from students where class_id is null;
+------------+----------+
| name       | class_id |
+------------+----------+
| 崔永元     |     NULL |
| 崔楠楠     |     NULL |
| 崔峰       |     NULL |
| 崔永元     |     NULL |
| 崔楠楠     |     NULL |
| 峰崔       |     NULL |
| c          |     NULL |
| cuinn      |     NULL |
| 周星驰     |     NULL |
| 周         |     NULL |
| 周星       |     NULL |
| 周文王易经 |     NULL |
| 周驰       |     NULL |
+------------+----------+
