#--*--coding:utf-8
#Author:cnn
import urllib.request
import os

object_path=os.path.dirname(os.path.dirname(__file__))
#print(object_path)
"""csdn爬虫"""
def crawler(url):
    req=urllib.request.urlopen(url)
    url_split=url.split("/")
    # name=url_split[-1].split(".")[0]
    name = url_split[-1]
    lagou_content=req.read()
    file_name=object_path+"/csdn/"+name+".html"
    # if
    file=open(file_name,"wb")
    file.write(lagou_content)
    file.flush()
    file.close()

if __name__ == '__main__':
    crawler("https://blog.csdn.net/zd147896325/article/details/78957901")