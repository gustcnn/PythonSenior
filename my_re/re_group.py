# --*--coding:utf-8
# Author:cnn
import re

"""分组"""
#()小括号是用来分组的,有几个(),就有几组,可以使用.group(1)取第一组的值
# (163|126|gmail|icloud|foxmail|qq)
email_list=["gustcnn@qq.com","cnn_cui@qq.com","q_123456@qq.com","233456@163.com","12@126.com"]
re_str=r"[a-zA-Z_\d]{4,20}@(163|126|gmail|icloud|foxmail|qq)\.com$"
qq_count=0
for email in email_list:
    result=re.match(re_str,email)
    if result:
        print("%s符合邮箱标准."%email)
        if result.group(1)=="qq":
            qq_count+=1
    else:
        print("%s不符合邮箱标准."%email)
print("符合标准的qq邮箱个数:%d"%qq_count)