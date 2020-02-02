# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 19:26 
# @Author : LiChao
# @File : C-1.24.py 

def yuan_yin(S):
    temp = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    num = 0
    for i in S:
        if i in temp:
            num += 1
    return num
S='abcde'
result = yuan_yin(S)
print(result)