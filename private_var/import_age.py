#--*--coding:utf-8
#Author:cnn
from private_var.private import *

class Student(Person):
    #print(_age)
    pass

if __name__ == '__main__':
    student=Student("cnn",18,200740204104)
    print(student.no)
    print(student._age)
    #print(student.__name)