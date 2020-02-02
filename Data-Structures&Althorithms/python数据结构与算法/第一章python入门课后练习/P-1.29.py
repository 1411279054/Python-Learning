# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 10:06 
# @Author : LiChao
# @File : P-1.29.py 

from itertools import permutations
def function(temp):
    print(list(map(lambda x:x,permutations(temp))))
    print(len(list(map(lambda x:x,permutations(temp)))))

temp=[1,2,3,4]
function(temp)