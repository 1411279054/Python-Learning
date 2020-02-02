# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 18:55 
# @Author : LiChao
# @File : C-1.23.py 
def IndexError(S,i):
    try:
        print(S[i])
    except BaseException :
        print("Don't try buffer overflow attacks in Python!")
S=[1, 2,3,4]
IndexError(S,4)