# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 15:51 
# @Author : LiChao
# @File : P-4.27.py 
import os
def new_walk(path):
    lists = []
    list1 =[]
    list2 = []
    items = os.listdir(path)
    for item in items:
        item = path +'\\'+ item
        if os.path.isdir(item):
            list1.append(item)
        if os.path.isfile(item):
            list2.append(item)
    lists.append(path)
    lists.append(list1)
    lists.append(list2)
    return lists
lists = new_walk("C:\\Users\\Administrator\\Desktop\\pycharm")
print(lists)