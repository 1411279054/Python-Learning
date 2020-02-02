# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 18:51 
# @Author : LiChao
# @File : C-1.22.py 

def mutiply(S1,S2):
    S3=[]
    for i in range(len(S1)):
        S3.append(S1[i]*S2[i])
    return S3
S1 = [1,2,3,4,5,6,7,8,9]
result = mutiply(S1,S1)
print(result)