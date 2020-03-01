# -*- coding: utf-8 -*- 
# @Time : 2020/2/29 23:02 
# @Author : LiChao
# @File : 有效的括号.py
## 题目描述：有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        if s =="":
            return True
        i = 0
        stack=[]
        while i< len(s):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) == 0:
                    return False
                elif stack.pop() != "(":
                    return False
            elif s[i] == "}":
                if len(stack) == 0:
                    return False
                elif stack.pop() != "(":
                    return False
            elif s[i] == "]":
                if len(stack) == 0:
                    return  False
                elif stack.pop() != "[":
                    return False
            i +=1
        if len(stack) !=0:
            return False
        else:
            return True
def main():
    s = "()"
    result = Solution().isValid(s)
    print(result)
if __name__ == '__main__':
    main()