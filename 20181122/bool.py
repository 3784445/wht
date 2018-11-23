#-*- coding:utf-8 -*-

'''布尔值只有Ture 和 False 两种值'''

# print(2>3)

# print(3>1)

'''运用运算符来算布尔值and,or,not'''

# print(True and True)
#
# print(True and False)
#
# print(False and False)
#
# print(1 and 1)
#
# print(1<2 and 2>1)

# print(True or True)
#
# print(True or False)
#
# print(False or False)
#
# print(not True)
#
# print(not False)
#
# '''实际应用条件判断'''
#
# # a = 17
# a = 19
# if a <= 18 :
#     print('未成年')
# else:
#     print('已成年')
'''变量'''
#
# a = 1 #a是一个整数
#
# are = 'ABc' #are是一个字符串
#
# zf = True  #zf是布尔值True
#
# print(a,are,zf)

# a='ABC'
# b =a
# a = 'XYZ'
# print(b)

'''
以上python解释器做了三件事儿:
1在内存创建了一个ABC的字符串，又在内存中创建了一个名为a的变量，并把它指向ABC
2在内存中创建了一个名为b的变量，并把它指向ABC
3在内存创建了一个XYZ的字符串，把变量a重新指向了XYZ
'''

'''运算符'''

# print(type(10/3))
# print(10/3,12/3)
# print(type(12/3)) #除法计算结果是浮点数，即使可以整除，结果也是浮点数

# print(type(10//3))
# print(10//3)
# print(type(12.12//3))
# print(12.12//3)  #两个整数相除无论结果是否有小数位，都只取整数部分，浮点数与整数相除结果类型为浮点数

print(12.13%2)  #只取余数

print(0.13%2)

print(10%2)

print(10%2.0)









