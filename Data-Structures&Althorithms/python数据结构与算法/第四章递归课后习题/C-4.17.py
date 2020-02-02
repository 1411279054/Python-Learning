# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 11:35 
# @Author : LiChao
# @File : C-4.17.py 
def YesorNot(strs):
    if len(strs)==1:
        return True
    else:
        if strs[0] == strs[-1]:
            return YesorNot(strs[1:-2])
        else:
            return False
strs = 'abba'
result = YesorNot(strs)
print(result)