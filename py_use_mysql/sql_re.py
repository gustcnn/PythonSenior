#--*--coding:utf-8
#Author:cnn
import re
sql = "select * from customers where name=%s and passwd=%s"
sql_re=r"^s.*[\* =\%]*"
re_s=r"^s.*"
s="s.*\*"
r=r"s.*\*"
result=re.match(re_s,sql)
print(result.group())
# pwd_re=r"^[a-zA-Z][a-zA-Z0-9_]{8,20}$"
pwd_re=r"^[a-zA-Z][a-zA-Z0-9_]*$"
print(re.match(pwd_re,"aaaaaaaa1").group())