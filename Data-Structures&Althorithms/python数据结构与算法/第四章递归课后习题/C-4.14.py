# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 9:26 
# @Author : LiChao
# @File : C-4.14.py

##将所有的盘子从a移到b
i = 1
def move(n,a,b):
    global i
    print('第{0}步是：{1}->{2}'.format(i,a,b))
    i +=1
def hanoni(n,a,b,c):

    if n==1:
        move(n,a,b)
    else:
        hanoni(n-1,a,c,b)
        move(n,a,b)
        hanoni(n-1,c,b,a)

hanoni(1,'a','b','c')