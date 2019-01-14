#--*--coding:utf-8
#Author:cnn
import re

#将找到的内容进行替换
re_str=r"\d+"
#根据正则表达式,将匹配到的内容替换为中间的"1024"的内容
result=re.sub(re_str,"1024","python=998,c++=889")
print(result)
