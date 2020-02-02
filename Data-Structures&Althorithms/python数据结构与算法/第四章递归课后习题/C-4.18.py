# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 11:39 
# @Author : LiChao
# @File : C-4.18.py 
yuan_number = 0
fu_number = 0
def method(strs):
    if len(strs)==0:
        return None
    else:
        if strs[0].lower() in 'abcde':
            global yuan_number
            yuan_number +=1
        else:
            global fu_number
            fu_number +=1
        return method(strs[1:])
str='level'
method(str)
print(yuan_number)
print(fu_number)