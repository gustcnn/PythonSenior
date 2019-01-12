# --*--coding:utf-8
# Author:cnn
import re

"""正则表达式"""
str = "hello world"
# 验证字符串是否是以h开头,以d结尾...r""表示是正则
re_str = r"^h.+d$"
result = re.match(re_str, str)
print(result)
