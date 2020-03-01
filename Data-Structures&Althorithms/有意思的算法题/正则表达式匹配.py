# -*- coding: utf-8 -*- 
# @Time : 2020/2/26 10:04 
# @Author : LiChao
# @File : 正则表达式匹配.py
#


##题目描述：求满足'.'和'*'匹配模式的正则表达式


### 官方题解1：递归方法
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
### 官方题解2：动态规划
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
def main():
    s = "b"
    p = "a*b"
    result=Solution().isMatch(s,p)
    print(result)
if __name__ == '__main__':
    main()

