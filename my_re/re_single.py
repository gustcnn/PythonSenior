# --*--coding:utf-8
# Author:cnn
import re

# 匹配单个字符,\d匹配一位数字0-9
re_str = r"速度与激情\d"
result = re.match(re_str, "速度与激情1")
print(result.group())
result = re.match(re_str, "速度与激情8")
print(result.group())
# 匹配[12345678]里面任意一个字符,都算匹配
re_str = r"速度与激情[12345678]"
result = re.match(re_str, "速度与激情5")
print(result.group())

# 匹配[1-8]里面任意一个字符,都算匹配,数字是连续的才可用1-8
re_str = r"速度与激情[1-8]"
result = re.match(re_str, "速度与激情6")
print(result.group())
# 匹配不连续的
re_str = r"速度与激情[123678]"
result = re.match(re_str, "速度与激情7")
print(result.group())
# 匹配不连续的
re_str = r"速度与激情[1-36-8]"
result = re.match(re_str, "速度与激情7")
print(result.group())

# 匹配数字和字母
re_str = r"速度与激情[1-8a-zA-Z]"
result = re.match(re_str, "速度与激情7")
print(result.group())
result = re.match(re_str, "速度与激情a")
print(result.group())
result = re.match(re_str, "速度与激情A")
print(result.group())
result = re.match(re_str, "速度与激情z")
print(result.group())
result = re.match(re_str, "速度与激情Z")
print(result.group())

# \w匹配数字和字母和下划线
re_str = r"速度与激情[\w]"
result = re.match(re_str, "速度与激情_")
print(result.group())

# \s匹配空白字符
re_str = r"速度与激情\s\d"
result = re.match(re_str, "速度与激情 8")
print(result.group())

# .匹配任意一个字符,相当于linux里面的*
re_str = r"速度与激情."
result = re.match(re_str, "速度与激情1")
print(result.group())
result = re.match(re_str, "速度与激情a")
print(result.group())
result = re.match(re_str, "速度与激情A")
print(result.group())
result = re.match(re_str, "速度与激情哈")
print(result.group())
result = re.match(re_str, "速度与激情！")
print(result.group())
result = re.match(re_str, "速度与激情#")
print(result.group())