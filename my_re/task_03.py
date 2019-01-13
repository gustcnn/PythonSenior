# --*--coding:utf-8
# Author:cnn
import re

"""需求：匹配出163的邮箱地址,且@之前有4-20位英文字母数字下划线"""
# gust@163.com

email_list=["gust@163.com","gust_123_@163.com","56163.com",
            "gust@163","gust@.com","123456789abcdefghjkl@163.com"]
re_str = r"([a-zA-Z\d_]{4,20})@163\.com$"
for email in email_list:
    result=re.match(re_str,email)
    if result:
        print("%s 符合要求"%email)
    else:
        print("%s 不符合要求"%email)

