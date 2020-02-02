# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 14:34 
# @Author : LiChao
# @File : C-4.21.py 

def get_two_int(S,i,j,k):
    # if i>=j:
    #     return None
    # else:
    #     if i < j and S[i]+S[j]==k:
    #             return S[i],S[j]
    #     if i< j and S[i] +S[j]<k:
    #             get_two_int(S,i+1,j,k)
    #     if i< j and S[i] +S[j]>k:
    #             get_two_int(S,i,j-1,k)
    while i<=j:
        if S[i]+S[j] == k:
            print(S[i],S[j])
        elif S[i]+S[j]>k:
            return get_two_int(S,i,j-1,k)
        else :
            return get_two_int(S,i+1,j,k)
    print("没找到！！！")


S=[1,2,3,4,5,6,7]
get_two_int(S,0,6,100)

