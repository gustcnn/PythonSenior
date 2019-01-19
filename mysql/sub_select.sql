--子查询(一个查询里面嵌套另一个查询)
  --查询最高的男生的信息
    --得到最高的男生
    select max(high) from students where gender=1;
    --显示最高的男生的额信息
    select * from students where high in (select max(high) from students where gender=1);
  mysql> select * from students where high in (select max(high) from students where gender=1);
+----+--------+------+--------+--------+----------+------------+-----------+
| id | name   | age  | high   | gender | class_id | birth      | is_delete |
+----+--------+------+--------+--------+----------+------------+-----------+
|  4 | durant |   30 | 198.00 | 男     |        3 | 1988-11-11 |           |
+----+--------+------+--------+--------+----------+------------+-----------+

--子查询,查询区
mysql> select * from province where province.pid=(select aid  from province where province.atitle="长春市");
+-----+--------+------+
| aid | atitle | pid  |
+-----+--------+------+
| 841 | 南关区 |  235 |
| 842 | 朝阳区 |  235 |
| 843 | 绿园区 |  235 |
| 844 | 农安县 |  235 |
| 845 | 榆树市 |  235 |
| 846 | 德惠市 |  235 |
| 847 | 宽城区 |  235 |
| 848 | 二道区 |  235 |
| 849 | 双阳区 |  235 |
| 850 | 九台市 |  235 |
+-----+--------+------+