# --*--coding:utf-8
# Author:cnn
# --*--coding:utf-8
# Author:cnn
from gevent import monkey
import gevent
import urllib.request
import os

"""gevent网络图片下载"""
object_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

monkey.patch_all()


def img_downloader(url):
    # url = "https://rpic.douyucdn.cn/asrpic/190112/522898_1712.jpg/dy1"
    print("Get url %s" % url)
    # 根据/分隔url地址
    img_split = url.split("/")
    # 获取图片名字
    img_name = img_split[-2]
    # print(img_name)
    # 打开url,返回req对象
    req = urllib.request.urlopen(url)
    # 读取url中的内容
    img_content = req.read()
    print("图片%s下载完毕" % img_name)
    with open(object_path + "/images/" + img_name, "wb") as img_file:
        img_file.write(img_content)
        img_file.flush()


def main():
    gevent.joinall([gevent.spawn(img_downloader, "https://rpic.douyucdn.cn/asrpic/190112/522898_1712.jpg/dy1"),
                    gevent.spawn(img_downloader, "https://rpic.douyucdn.cn/asrpic/190112/1097164_1938.jpg/dy1")
                    ])


if __name__ == '__main__':
    main()
