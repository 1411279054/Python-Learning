#class Solution:
    # 1.自己想的---超时
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) == 1:return s
    #     left,right = 0,len(s)-1
    #     nummax = 0
    #     strs = ""
    #     while left < right:
    #         left_demo = left
    #         right_demo = right
    #         num = 0
    #         i = 1
    #         while left_demo <= right_demo:
    #             if s[left_demo] == s[right_demo] and left_demo < right_demo:
    #                 left_demo +=1
    #                 right_demo -=1
    #                 num +=2
    #             elif s[left_demo] == s[right_demo] and left_demo == right_demo:
    #                 num +=1
    #                 break
    #             else:
    #                 num = 0
    #                 right_demo = right -i
    #                 left_demo = left
    #                 i +=1
    #         if num > nummax:
    #             nummax = num
    #             strs = s[left:nummax+left]
    #
    #         left +=1
    #     return strs
    #
###           2.没看懂！！！
        # def longestPalindrome(self, s: str) -> str:
        #     size = len(s)
        #     if size < 2:
        #         return s
        #
        #     dp = [[False for _ in range(size)] for _ in range(size)]
        #
        #     max_len = 1
        #     start = 0
        #
        #     for i in range(size):
        #         dp[i][i] = True
        #
        #     for j in range(1, size):
        #         for i in range(0, j):
        #             if s[i] == s[j]:
        #                 if j - i < 3:
        #                     dp[i][j] = True
        #                 else:
        #                     dp[i][j] = dp[i + 1][j - 1]
        #             else:
        #                 dp[i][j] = False
        #
        #             if dp[i][j]:
        #                 cur_len = j - i + 1
        #                 if cur_len > max_len:
        #                     max_len = cur_len
        #                     start = i
        #     return s[start:start + max_len]
####        3.中间扩散法
def longestPalindome(s:str)-> str:
    if s == None or len(s)<1 :return ''
    start,end = 0,0
    for i in range(len(s)):
        num1 = expandAroundCenter(s,i,i)
        num2 = expandAroundCenter(s,i,i+1)
        num = max(num1,num2)
        if(num > end - start):
            start = i - (num-1)//2
            end = i +num//2
    return s[start:end+1]
def expandAroundCenter(s,i,j):
    l,r = i,j
    while l>0 and r<len(s) and s[l]==s[r]:
        l -= 1
        r += 1
    return r-l -1
def main():
    s =  "bb"
    result =longestPalindome(s)
    print(result)
if __name__ == '__main__':
    main()
