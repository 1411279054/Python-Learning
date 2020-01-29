# -*- coding: utf-8 -*- 
# @Time : 2020/1/29 11:45 
# @Author : LiChao
# @File : C-4.12.py 
def mutiply_m_n(m,n):
    if m == 1:
        return n
    if n==1:
        return m
    return mutiply_m_n(m,n-1)+m
result=mutiply_m_n(8,7)
print(result)