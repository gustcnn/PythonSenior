# --*--coding:utf-8
# Author:cnn
import re
import sys

"""需求：匹配出163的邮箱地址,且@之前有4-20位英文字母数字下划线"""
# gust@163.com
#\.转义.
re_str = r"([a-zA-Z\d_]{4,20})@163\.com$"
while True:
    email=input("请输入邮箱地址>>>:")
    if email=="q":
        sys.exit()
    result=re.match(re_str,email)
    if result:
        print("%s 符合要求"%email)
    else:
        print("%s 不符合要求"%email)


