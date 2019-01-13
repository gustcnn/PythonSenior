# --*--coding:utf-8
# Author:cnn
import os

def copy_file(src_path, dest_path):
    """拷贝文件"""
    if os.path.exists(src_path):
        #获取文件夹在的列表
        list_dir=os.listdir(src_path)
        #判断目的文件夹是否存在,不存在创建
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
        #循环列表中每个文件
        for dir in list_dir:
            #判断是否是文件
            if os.path.isfile(dir):
                #os.path.basename获得文件名
                print(os.path.basename(dir))
                src_file=open(dir,"r",encoding="utf8")
                dest_file = open(dest_path + "/" + os.path.basename(dir), "a+", encoding="utf8")
                try:
                    while True:
                        data=src_file.readline()
                        dest_file.write(data)
                        dest_file.flush()
                        if len(data)==0:
                            break
                finally:
                    dest_file.close()

            else:
                print("文件夹")
    else:
        print("文件夹不存在")
if __name__ == '__main__':
    copy_file("D:/python/script/PythonSenior/com/process","D:/python/script/PythonSenior/com/process_copy")

