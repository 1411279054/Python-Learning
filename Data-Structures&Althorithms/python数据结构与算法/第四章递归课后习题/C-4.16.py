# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 10:38 
# @Author : LiChao
# @File : C-4.16.py 

def reverse(S,start=0):
    if len(S) ==0:
        return ''
    else:
        return reverse(S[start+1:],start)+S[start]
S = 'abcd'
result = reverse(S)
print(result)
