#--*--coding:utf-8
#Author:cnn
import re
#正则
re_str="\d+"
#匹配出文章阅读数量,search不会从头匹配
result=re.search(re_str,"阅读数量为:9999")
print(result.group())
