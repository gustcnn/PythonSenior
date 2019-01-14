#--*--coding:utf-8
#Author:cnn
import re

re_str=r"\d+"
#re.findeall直接返回列表,不用加group了
result=re.findall(re_str,"阅读次数:9999,点赞数:6789")
print(result)
