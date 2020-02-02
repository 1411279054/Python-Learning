# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 15:09 
# @Author : LiChao
# @File : P-4.23.py
import  os
def find(path,filename):
    newpath = path +"\\"+filename
    if os.path.isfile(newpath):
        print(newpath)
    else:
        lists = os.listdir(newpath)
        for item in lists:
            find(newpath,item)
print(find('C:\\Users\\Administrator\\Desktop','pycharm'))