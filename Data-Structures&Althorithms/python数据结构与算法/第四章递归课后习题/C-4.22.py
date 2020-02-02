# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 15:00 
# @Author : LiChao
# @File : C-4.22.py 
def new_power(num,n):
    answer=1
    while n != 0:
        answer *=num
        n -=1
    return answer
result = new_power(2,5)
print(result)