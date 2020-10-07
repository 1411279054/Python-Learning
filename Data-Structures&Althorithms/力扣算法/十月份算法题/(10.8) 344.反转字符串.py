# -*- coding: utf-8 -*- 
# @Time : 2020-10-08 20:45 
# @Author : LiChao
# @File : (10.8) 344.反转字符串.py
class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        left,right = 0,len(s)-1
        while left <= right:
            if s[left]==s[right]:
                left += 1
                right -=1
            else:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -=1