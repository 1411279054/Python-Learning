# -*- coding: utf-8 -*- 
# @Time : 2020/1/30 10:23 
# @Author : LiChao
# @File : C-4.15.py




def get_subset(S,mark,n,i):
        if n == i:
            print("{",end=' ')
            for k in range(i):
                if mark[k] == 1 :
                    print(S[k],end=' ')
            print("}")
            return
        mark[n] = 0
        get_subset(S,mark,n+1,i)
        mark[n] = 1
        get_subset(S,mark,n+1,i)
mark = [0,0,0,0]
S=[1,2,3,4]
get_subset(S,mark,0,4)