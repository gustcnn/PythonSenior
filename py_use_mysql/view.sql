--三张表关联查询
select *from goods_update as g
    left join goods_cates as c on g.cate_id=c.id
    left join goods_brands as b on g.brand_id=b.id order by g.id
--三张表关联查询,去掉多于的id
select g.*,c.name as cate_name,b.name as brand_name from goods_update as g
    left join goods_cates as c on g.cate_id=c.id
    left join goods_brands as b on g.brand_id=b.id order by g.id
mysql> select g.*,c.name as cate_name,b.name as brand_name from goods_update as g
    ->     left join goods_cates as c on g.cate_id=c.id
    ->     left join goods_brands as b on g.brand_id=b.id order by g.id;
+----+-----------------------+---------+----------+----------+---------+------------+------------+------------+
| id | name                  | cate_id | brand_id | price    | is_show | is_saleoff | cate_name  | brand_name |
+----+-----------------------+---------+----------+----------+---------+------------+------------+------------+
|  1 | r510vc 15.6英寸笔记本 |       5 |        2 | 3399.000 |        |            | 笔记本     | 华硕       |
|  2 | y400n 14.0英寸笔记本  |       5 |        1 | 5000.000 |        |            | 笔记本     | 联想       |
|  3 | g150th 15.6英寸游戏本 |       4 |        3 | 8499.000 |        |            | 游戏本     | 雷神       |
|  4 | x550cc 15.6英寸笔记本 |       5 |        2 | 2799.000 |        |            | 笔记本     | 华硕       |
|  5 | x240 超级本           |       7 |        1 | 6000.000 |        |            | 超级本     | 联想       |
|  6 | r520vc 15.6英寸笔记本 |       5 |        2 | 3399.000 |        |            | 笔记本     | 华硕       |
|  7 | y410n 14.0英寸笔记本  |       5 |        1 | 4999.000 |        |            | 笔记本     | 联想       |
|  8 | g160th 15.6英寸游戏本 |       4 |        3 | 8500.000 |        |            | 游戏本     | 雷神       |
|  9 | E550cc 15.6英寸笔记本 |       5 |        2 | 2799.000 |        |            | 笔记本     | 华硕       |
| 10 | x260 超级本           |       7 |        1 | 4880.000 |        |            | 超级本     | 联想       |
| 11 | 电脑背包              |       6 |        1 |   98.000 |        |            | 笔记本配件 | 联想       |
| 12 | 键盘                  |       6 |        3 |  210.000 |        |            | 笔记本配件 | 雷神       |
| 13 | 鼠标                  |       6 |        3 |  180.000 |        |            | 笔记本配件 | 雷神       |
| 14 | 商务笔记本            |       6 |        3 |  210.000 |        |            | 笔记本配件 | 雷神       |
| 15 | 游戏笔记本            |       6 |        3 |  180.000 |        |            | 笔记本配件 | 雷神       |
+----+-----------------------+---------+----------+----------+---------+------------+------------+------------+

--创建视图(虚拟表)
create view v_goods_c_b as
    select g.*,c.name as cate_name,b.name as brand_name from goods_update as g
    left join goods_cates as c on g.cate_id=c.id
    left join goods_brands as b on g.brand_id=b.id order by g.id
mysql> create view v_goods_c_b as
    ->     select g.*,c.name as cate_name,b.name as brand_name from goods_update as g
    ->     left join goods_cates as c on g.cate_id=c.id
    ->     left join goods_brands as b on g.brand_id=b.id order by g.id;
Query OK, 0 rows affected (0.04 sec)

mysql> show tables;
+---------------------+
| Tables_in_jing_dong |
+---------------------+
| customers           |
| goods               |
| goods_brands        |
| goods_cates         |
| goods_update        |
| order_details       |
| orders              |
| v_goods_c_b         |
+---------------------+
mysql> desc v_goods_c_b;
+------------+------------------+------+-----+---------+-------+
| Field      | Type             | Null | Key | Default | Extra |
+------------+------------------+------+-----+---------+-------+
| id         | int(10) unsigned | NO   |     | 0       |       |
| name       | varchar(40)      | NO   |     | NULL    |       |
| cate_id    | int(10) unsigned | NO   |     | NULL    |       |
| brand_id   | int(10) unsigned | NO   |     | NULL    |       |
| price      | decimal(10,3)    | YES  |     | NULL    |       |
| is_show    | bit(1)           | YES  |     | b'1'    |       |
| is_saleoff | bit(1)           | YES  |     | b'0'    |       |
| cate_name  | varchar(40)      | YES  |     | NULL    |       |
| brand_name | varchar(40)      | YES  |     | NULL    |       |
+------------+------------------+------+-----+---------+-------+

