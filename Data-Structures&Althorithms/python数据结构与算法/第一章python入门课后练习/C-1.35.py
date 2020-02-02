# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 12:15 
# @Author : LiChao
# @File : C-1.35.py 

import random

def birthday_question(n):
    big_month = [1,3,5,7,8,10,12]
    small_month = [4,6,9,11]
    lists =[]
    month_list = random.choices([1,2,3,4,5,6,7,8,9,10,11,12],k=n)
    for i in range(n):
        if month_list[i] in big_month:                          #在大月份里
            day = random.choice(list(range(1,32)))
            strs = str(month_list[i])+'月'+str(day)+'日'
            lists.append(strs)
        elif month_list[i] in small_month:                       #在小月份里
            day = random.choice(list(range(1, 31)))
            strs = str(month_list[i])+'月'+str(day)+'日'
            lists.append(strs)
        else:                                                   #二月作为特殊月份
            day = random.choice(list(range(1, 29)))
            strs = str(month_list[i])+'月'+str(day)+'日'
            lists.append(strs)
    print(lists)
    for i in range(len(lists)):
        for j in range(i+1,len(lists)):
            if lists[i] ==lists[j]:
                print(lists[i])
                return True
    return False
def test(n,num):                                #测试代码
    i = 1
    count =0
    while i <= n:
        print('============================第{}次======================='.format(i))
        result = birthday_question(num)
        if result == True:
            count +=1
        i +=1
    print("{}个人中生日相同的概率是{}:".format(num,count/n))
test(10000,23)
