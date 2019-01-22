--索引(哪些列常用,并且数据比较多的时候,可以考虑增加索引,提高查询效率)
  --创建索引,create index 索引名 on表名(字段(长度))
  create index index_name on test_index(title(30))
  --查看索引
  show index from test_index
  --删除索引
  drop index 索引名 on 表名