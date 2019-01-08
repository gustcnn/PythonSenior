#--*--coding:utf-8
#Author:cnn

class My(object):
    def sing(self):
        for i in range(1,6):
            print("...唱歌5秒...")

    def dance(self):
        for i in range(1,6):
            print("...跳舞5秒...")
if __name__=="__main__":
    my=My()
    my.sing()
    my.dance()
