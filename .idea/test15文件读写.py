# coding:utf-8
# 文件 的读取
data =open('./util/ceshi',"r")   # r表示读取文件
print data.read()
print data.readline()   # 不写参数表示读一行
print data.readline(4)  # 写数字表示读取几个字符
print data.readlines()