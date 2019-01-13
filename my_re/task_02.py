# --*--coding:utf-8
# Author:cnn
import re

"""匹配变量名是否有效"""
names = ["age1", "_name", "2age", "__name__","age!","a#ge"]

# 以[]里面任意一个字符开头,后面跟[a-zA-Z_\d]里面的0个1个多个字符都可,并且以[a-zA-Z_\d]里面的内容结尾
re_str = r"^[a-zA-Z_][a-zA-Z_\d]*$"
for name in names:
    result = re.match(re_str, name)
    try:
        print(result.group())
    except AttributeError:
        print(name, "为无效的变量名.")
        pass
