# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 20:18 
# @Author : LiChao
# @File : C-1.26.py 
def function(a,b,c):
    lists = [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]
    for list in lists:
        if list[0]+list[1] ==list[2]:
            print('{}+{}={}'.format(list[0],list[1],list[2]))
        if list[0]*list[1] == list[2]:
            print('{}*{}={}'.format(list[0],list[1],list[2]))
        if list[0] == list[1] -list[2]:
            print('{}={}-{}'.format(list[0],list[1],list[2]))
function(1,3,4)