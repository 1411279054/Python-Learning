# -*- coding: utf-8 -*- 
# @Time : 2020/1/29 11:01 
# @Author : LiChao
# @File : C-4.10.py 
def log2(n):
    if n//2==0:
        return 0
    else:
        return 1+log2(n//2)
num=log2(12)
print(num)