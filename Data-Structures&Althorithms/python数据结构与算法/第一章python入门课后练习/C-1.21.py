# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 18:43 
# @Author : LiChao
# @File : C-1.21.py 

def inputTest():
    lst=[]
    try:
        while True:
            lst.append(input('please input:'))
    except EOFError:
        for i in lst[::-1]:
            print(i)
inputTest()