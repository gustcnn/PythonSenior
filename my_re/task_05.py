# --*--coding:utf-8
# Author:cnn
import re
import sys

"""需求：匹配邮箱地址,且@之前有4-20位英文字母数字下划线....完善匹配其它邮箱"""
# gust@163.com,gustcnn@qq.com,gustcnn@gmail.com.cn
#\.转义.
re_str = r"([a-zA-Z\d_]{4,20})@[a-z\d]*\.[a-z]{3}(\.[a-z]{2})?$"
while True:
    email=input("请输入邮箱地址>>>:")
    if email=="q":
        sys.exit()
    result=re.match(re_str,email)
    if result:
        print("%s 符合要求"%email)
    else:
        print("%s 不符合要求"%email)


