# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 11:48 
# @Author : LiChao
# @File : C-4.19.py 
def change_odd_even(lists,i,j):
    if i >= j:
        return None
    else :
        while i< j and lists[i]%2==1:
            i += 1
        while i< j and lists[j]%2==0:
            j -=1
        lists[i],lists[j] =lists[j],lists[i]
        return change_odd_even(lists,i,j)

lists = [1,2,3,4,5,6,7,8,9]
change_odd_even(lists,0,8)
print(lists)
