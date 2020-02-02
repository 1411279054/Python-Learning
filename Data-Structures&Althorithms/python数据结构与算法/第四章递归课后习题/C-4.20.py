# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 12:04 
# @Author : LiChao
# @File : C-4.20.py 
def new_list(S,k,i,j):
    if i >= j:
        return None
    else:
        while i<j and S[i] < k:
            i +=1
        while i < j and S[j] > k:
            j -=1
        S[i],S[j]=S[j],S[i]
        return new_list(S,k,i,j)
S=[9,8,7,6,5,4,3,2,1]
new_list(S,5,0,8)
print(S)