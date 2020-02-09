# -*- coding: utf-8 -*- 
# @Time : 2020/2/7 22:44 
# @Author : LiChao
# @File : 无重复字符最长字串.py 

#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

def lengthOfLongestSubstring(s: str) -> int:
    lists=[]
    max = lists.copy()
    for i in range(len(s)):
        if s[i] not in lists:
            lists.append(s[i])
        else:
            if(len(max)<len(lists)):
                max = lists.copy()
                lists.clear()
                lists.append(s[i])
            else:
                lists.clear()
                lists.append(s[i])
    if len(max)>len(lists):
        return len(max)
    else:
        return len(lists)
s ="dvdf"
result = lengthOfLongestSubstring(s)
print(result)