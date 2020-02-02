# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 19:31 
# @Author : LiChao
# @File : C-1.25.py 
import re
def del_symbol(str):
    lists = list(str)
    strs =''
    for i in lists:
        if 'a'<=i.lower()<='z':
                strs +=i
    return strs
def del_symbol2(str):
    pattern ='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    result = re.sub(pattern,'',str)
    return result
str = "let's go!"
result=del_symbol2(str)
print(result)
