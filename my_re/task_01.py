#--*--coding:utf-8
#Author:cnn
import re

"""匹配变量名是否有效"""
names=["name1","_name","2_name","__name__"]

#以[]里面任意一个字符开头,后面跟0个1个多个字符都可
re_str=r"^[a-zA-Z_].*"
for i in range(0,len(names)):
    result=re.match(re_str,names[i])
    try:
        print(result.group())
    except AttributeError:
        print(names[i],"为无效的变量名.")
        pass