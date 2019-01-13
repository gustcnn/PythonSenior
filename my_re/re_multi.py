# --*--coding:utf-8
# Author:cnn
import re

"""正则匹配多个字符"""

# {}表示紧挨着的即\d可以是1位,也可以是2位
re_str = r"速度与激情\d{1,2}"
result = re.match(re_str, "速度与激情1")
print(result.group())

result = re.match(re_str, "速度与激情19")
print(result.group())

# 匹配11位电话号码,{}前面的数字必须是连续的11位
re_telephone = r"\d{11}"
result=re.match(re_telephone,"13877778888")
print(result.group())

#匹配座机
re_tele=r"021-?\d{8}"
result=re.match(re_tele,"021-12345678")
print(result.group())

result=re.match(re_tele,"02112345678")
print(result.group())

#匹配3位或者4位区号,可有-也可没有,号码可以是7位也可8位
re_tele=r"\d{3,4}-?\d{7,8}"
result=re.match(re_tele,"01012345678")
print(result.group())

result=re.match(re_tele,"0438-1234567")
print(result.group())

content="""aaddsa
adfaf
adfasdf
fffff
sssssssss
wwwwwwwwwww
"""
#.匹配除了\n的任意一个字符,*表示它之前的字符可以有0,1,多个
re_str=r".*"
result=re.match(re_str,content)
print(result.group())
#re.S匹配非空白符
result=re.match(re_str,content,re.S)
print(result.group())

