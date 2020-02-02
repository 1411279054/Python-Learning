# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 12:48 
# @Author : LiChao
# @File : P-1.36.py
def count_word(lists):
    dictionary={}
    for i in range(len(lists)):
        count = 1
        for j in range(i+1,len(lists)):
            if lists[i] != ' ' and lists[i] == lists[j]:
                count += 1
        if lists[i] not in dictionary:
            dictionary[lists[i]] = count
    return dictionary
lists = ['aa','aa','aaa',';falsk','aaa,af']
result = count_word(lists)
print(result)


##  https://blog.csdn.net/Harrytsz/article/details/86645857
def function36():
    import string
    temp = input("Please input a string: \n").strip(string.punctuation).split(" ")
    keys = list(set(temp))
    result = dict(zip(keys,[0]*len(keys)))
    for item in temp:
        result[item] += 1
    return result
