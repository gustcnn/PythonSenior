# --*--coding:utf-8
# Author:cnn
import re

html_str = "<h1>欢迎使用系统</h1>"
re_str = r"<\w*>(.*)</\w*>"
result = re.match(re_str, html_str)
# 取出所有匹配内容
print(result.group())
# 取出分组内容
print(result.group(1))
# 一个()是一个分组
re_str_02 = r"<(\w*)>(.*)</\1>"
result_02 = re.match(re_str_02, html_str)
print(result_02.group(2))

html_content="<body><h1>欢迎光临</h1></body>"
re_str_03=r"<\w*><\w*>.*</\w*></\w*>"
result_03=re.match(re_str_03,html_content)
print(result_03.group())

#</\2></\1>表示跟前面的分组一致
re_str_03=r"<(\w*)><(\w*)>(.*)</\2></\1>"
result_03=re.match(re_str_03,html_content)
print(result_03.group(3))