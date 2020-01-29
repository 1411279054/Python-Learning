# -*- coding: utf-8 -*- 
# @Time : 2020/1/29 11:17 
# @Author : LiChao
# @File : C-4.11.py 
def unique(S,index=0):
    if index == len(S)-1:
        return False
    if unique(S,index+1):
        for i in range(index+1,len(S)):
            if S[index]==S[i]:
                return False
        return True
    else :
        return False
S=[1,2,3,4,5,6,7,7,77,77]
result=unique(S,0)
print(result)
