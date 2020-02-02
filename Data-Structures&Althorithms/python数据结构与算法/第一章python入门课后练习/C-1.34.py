# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 11:57 
# @Author : LiChao
# @File : C-1.34.py


##https://blog.csdn.net/weixin_45519487/article/details/100726716
from random import choices,choice
from time import sleep
def get_space_index(sample):
    sample=list(sample)  #sample转换成list列表
    space_index_list=[]  #定义一个空列表
    while ' ' in sample:    #当sample中有空格时
        index=sample.index(' ')  #将sample空格的索引赋值给index
        space_index_list.append(index+len(space_index_list))  #在space_index_list 列表中添加索引和长度
        sample.pop(index)
    return space_index_list
def punish_write():
    sample=list(" I will never spam my friends again.")
    cnt=0
    wrong_cnt=8
    wrong_index_list=choices(list(range(100)),k=8)#拼写错误的索引组成的列表
    print(wrong_index_list)
    space_index_list=get_space_index(sample)
    print(space_index_list)#调用上述定义的函数，创造sample中含有的空格的索引列表
    wrong_times=0 #错误0次
    while cnt<100:
        if cnt in wrong_index_list:#如果当前的索引在错误列表索引中
            wrong_times+=1
            while True:
                wrong=choice(range(len(sample)))#选择在sample列表的任意一部分出错的索引，并将之赋值给wrong
                if wrong not in space_index_list:#如果出现错误的地方不在空格列表中
                    sample[wrong]=choice([chr(i) for i in range(65,65+26)]+[chr(i) for i in range(97,97+26)]+[',','.'])#错误出现在字母拼写中
                    break
            for i in sample:
                print(i,end='')
                sleep(0.05)
            print(' |{:3d}| \twrong {}'.format(cnt+1,wrong_times),end='\n')
            sleep(0.1)
        else:
            for i in sample:
                print(i,end='')
                sleep(0.03)
            print('|{:3d}|'.format(cnt+1),end='\n')
            sleep(0.1)
        cnt+=1
        sample=list(" I will never spam my friends again.")
punish_write()