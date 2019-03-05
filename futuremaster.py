#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/3/6

filepath = "D:\\test.txt"

#1.读取D盘根目录下文件test.txt的内容
with open(filepath,'r',encoding='utf-8') as rf:
    filedata=rf.read()
    print(filedata)


# 2.遍历所有行，得到邮箱格式的每一行
with open(filepath,'r',encoding='utf-8') as rf:
    emaillist = [] # 保存邮箱格式的每一行到此数组
    for line in rf:
        #判断得到正确邮箱格式的每一行
        if "@" in line and ".com" in line:
            print(line,end='')
            emaillist.append(line.replace("\n",""))
    print(emaillist)


#3.对所有行按长度进行排序
with open(filepath, 'r', encoding='utf-8') as rf:
    lines_list = rf.readlines() #读取每一行内容,存放于列表中
    lines_list.sort(key=lambda x:len(x),reverse=False)
    for l in lines_list:
        print(l,end='')


#4.把所有行写入新文件test_new.txt
with open(filepath,'r',encoding='utf-8') as rf,\
        open('D:\\test_new.txt', 'w', encoding='utf-8') as wf:
    for line in rf:
        wf.write(line)

