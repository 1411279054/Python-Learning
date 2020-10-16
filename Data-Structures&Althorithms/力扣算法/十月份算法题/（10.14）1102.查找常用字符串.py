# -*- coding: utf-8 -*- 
# @Time : 2020-10-15 13:26 
# @Author : LiChao
# @File : （10.14）1102.查找常用字符串.py
class Solution:
    def commonChars(self, A: list) -> list:
        minfreq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])

        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans

def main():
    A = ["bella", "label", "roller"]
    result = Solution().commonChars(A)
if __name__ == '__main__':
    main()