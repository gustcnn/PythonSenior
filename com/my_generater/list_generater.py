# --*--coding:utf-8
# Author:cnn
# 列表生成式,求0-11的平方
nums = [a ** 2 for a in range(12)]
print(nums)

# 生成器
nums = (a ** 2 for a in range(12))
print(nums)
