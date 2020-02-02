# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 10:18 
# @Author : LiChao
# @File : P-1.30.py 

def function(num):
    count = 0
    while num >= 2:
        num = num / 2
        count +=1
    return count
num = 4
result = function(num)
print(result)