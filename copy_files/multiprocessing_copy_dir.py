"""多任务文件夹拷贝"""
import os
import multiprocessing

object_path = os.path.dirname(os.path.dirname(__file__))
def copy_file(file_name, src, dest):
    """
    完成文件拷贝
    :param file_name: 文件名
    :param src: 原路径
    :param dest: 目的路径
    :return:
    """
    # print(file_name)
    if os.path.exists(src):
        print("====文件拷贝====从%s,到%s,拷贝文件为:%s" % (src, dest, file_name))
        # 创建源文件file对象
        src_file = open(src + "/" + file_name, "r", encoding="utf8")
        # 创建目的文件对象
        dest_file = open(dest + "/" + file_name, "a+", encoding="utf8")

        while True:
            try:
                data = src_file.readline()
                dest_file.write(data)
                dest_file.flush()
                if len(data) == 0:
                    break
            finally:
                if dest_file != None:
                    dest_file.close()
                if src_file != None:
                    src_file.close()
    else:
        print("源文件不存在.")


def main():
    # 要拷贝文件夹名字
    # src_dir_names = input("请输入要拷贝文件夹名字:")
    src_dir_names = "D:/python/script/PythonSenior/com/process"

    # 获得文件夹中文件名列表
    file_list = os.listdir(src_dir_names)
    # print(file_list)
    # 文件夹名字
    dest_dir_name = src_dir_names + "multi_copy"
    # print(dest_dir_name)
    # 创建新文件夹
    try:
        os.mkdir(dest_dir_name)
    except:
        pass
    # 创建进程池
    p = multiprocessing.Pool(5)
    for file_name in file_list:
        p.apply_async(copy_file, args=(file_name, src_dir_names, dest_dir_name))
    p.close()
    p.join()


if __name__ == '__main__':
    # D:/python/script/PythonSenior/com/process
    # print(object_path)
    main()
