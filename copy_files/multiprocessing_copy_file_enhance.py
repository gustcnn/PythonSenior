# --*--coding:utf-8
# Author:cnn
import multiprocessing
import os


class CopyDirFile(object):
    """拷贝文件夹下的文件"""

    def copy_file(self, file_name, src, dest):
        if os.path.exists(src):
            src_file = open(src + "/" + file_name, "r", encoding="utf8")
            dest_file = open(dest + "/" + file_name, "a+", encoding="utf8")

            while True:
                try:
                    data = src_file.readline()
                    dest_file.write(data)
                    dest_file.flush()
                finally:
                    if dest_file != None:
                        dest_file.close()
                    if src_file != None:
                        src_file.close()

        else:
            print("源文件不存在.")


    def main(self):
        # 需要拷贝文件的文件夹名
        src_dir_name = "D:/python/script/PythonSenior/com/process"
        # 获取拷贝文件名列表
        names_list = os.listdir(src_dir_name)
        # 目的文件夹名字
        dest_dir_name = src_dir_name + "mul_enhance_copy"
        # 创建目的文件夹
        try:
            os.mkdir(dest_dir_name)
        except:
            pass
        # 创建进程池
        p = multiprocessing.Pool(5)
        # 向进程池中提交数据
        for file_name in names_list:
            p.apply_async(self.copy_file, args=(file_name, src_dir_name, dest_dir_name))
        p.close()
        # 等待所有进程执行完毕
        p.join()


if __name__ == '__main__':
    cdf = CopyDirFile()
    cdf.main()
